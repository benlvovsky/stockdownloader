import datetime as dt
import time
import settings as st
import pandas as pd
import os
import tiingoext            as cv_tiingo
import converter_invest     as cv_invest
import converter_asxhist    as cv_asxhist
import requests
import quandlreader as qr
import marketindex as mi
import marketdata as md
import numpy as np
import pytz

utc = pytz.UTC

class FinDownloader:
    """
    Historical daily data downloader
    """

    def __init__(self, source, retry_count=3, pause=0.1,
                 timeout=30):
        self.source = source
        self.retry_count = retry_count
        self.pause = pause
        self.timeout = timeout

        self.datasource     = st.config['downloaders'][source]['datasource']
        self.max_sparseness = st.config['downloaders'][source]['maxSparseness']
        self.symbolColumn   = st.config['downloaders'][source]['symbolColumn']
        self.dateColumn     = st.config['downloaders'][source]['dateColumn']
        self.priceColumn    = st.config['downloaders'][source]['priceColumn']
        self.directory      = st.config['downloaders'][source]['directory']
        self.access_key     = st.config['downloaders'][source].get('access_key', '')
        self.inputfilename  = st.config['downloaders'][source].get('inputfilename', '')
        self.date_format    = st.config['downloaders'][source]['dateFormat']

    def downloadInstruments(self, symbols, start_date, final_date):
        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        millis = int(round(time.time() * 1000))
        downloadFileName = '{}.csv'.format(str(millis))

        symbolsArray = symbols.split(',')
        print(f'datasource ={self.datasource  }')
        print(f'symbolName ={self.symbolColumn}')
        print(f'dateColumn ={self.dateColumn  }')
        print(f'priceColumn={self.priceColumn }')
        print(f'date_format={self.date_format }')
        print(f'symbols.split={symbolsArray}')
        print(f'start_date={start_date}, final_date={final_date}, downloadFileName={downloadFileName}')

        session = requests.session()
        session.headers = requests.utils.default_headers()
        session.headers[
            'Accept'] = 'text/html,application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        session.headers['Accept-Encoding'] = 'gzip, deflate, br'
        session.headers['Accept-Language'] = 'en,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7'
        session.headers['Cache-Control'] = 'max-age=0'
        session.headers['Connection'] = 'keep-alive'
        session.headers['Upgrade-Insecure-Requests'] = '1'
        session.headers[
            'User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
        session.headers['Content-Type'] = 'application/json'
        session.headers['Authorization'] = 'Token {}'.format(self.access_key)
        # print 'using headers v.6'

        downloaders = {
            "marketdata": md.MarketData(symbolsArray, start_date, final_date, session=session),
            "converter_invest": lambda: cv_invest.FormatConverter(start_date, self.inputfilename),
            "converter_asxhist": lambda: cv_asxhist.FormatConverter(start_date, self.inputfilename),
            "tiingo": lambda: cv_tiingo.TiingoExt(symbolsArray, start_date, final_date, api_key=self.access_key,
                                                  retry_count=10, pause=0.3, extheaders=session.headers),
            "quandl": lambda: qr.Quandl(symbolsArray, start_date, final_date, api_key=self.access_key,
                                        retry_count=10, pause=0.3, extheaders=session.headers),
            "marketindex": lambda: mi.MarketIndex(symbolsArray, start_date, final_date, api_key=self.access_key,
                                                  retry_count=10, pause=0.3, extheaders=session.headers)
        }

        allColumnsOrigDf = downloaders[self.source]().read()
        allColumnsNoIndexDf = allColumnsOrigDf.reset_index()

        # allColumnsOrigDf.to_csv('downloads/allColumnsOrigDf.csv')

        print(f'Columns list from DataReader: {allColumnsNoIndexDf.columns.values}')
        print(f'Index from DataReader: {allColumnsNoIndexDf.index}')
        if self.priceColumn in allColumnsNoIndexDf:
            dataDf = allColumnsNoIndexDf[[self.symbolColumn, self.dateColumn, self.priceColumn]]
        else:
            print(f'Column {self.priceColumn} doesn''t exist. Trying fallback for using [''Symbol'', ''Date'', ''Close'']')
            dataDf = allColumnsNoIndexDf[['Symbol', 'Date', 'Close']]
        dataDf.to_csv('downloads/downloadedInstrumentsOnlyOnePriceColRaw.csv')
        newDf = self.pivot(dataDf, start_date, final_date)

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        earliest_date = start_date + dt.timedelta(days=7)
        newDf = newDf[newDf.index >= earliest_date]
        existing_earliest_date = newDf.index.min()
        # existing_earliest_date = newDf.loc(newDf.index >= earliest_date).index.min()
        print(f'earliest_date = {earliest_date}, existing_earliest_date = {existing_earliest_date}')
        cols_to_exclude = newDf.loc[:existing_earliest_date].isnull().all()
        cols_to_keep = ~cols_to_exclude
        print(f'Earliest date to compare: {str(existing_earliest_date)}')
        newDf = newDf.loc[:, cols_to_keep]
        newDf.to_csv(self.directory + '/before_dropna_' + downloadFileName)
        # newDf.dropna(axis=0, inplace=True)
        newDf.dropna(axis=1, inplace=True)
        newDf.to_csv(self.directory + '/' + downloadFileName)
        print('instruments download finished')
        return self.directory + '/' + downloadFileName

    def pivot(self, dataDf, start_date, final_date):
        symbolsArray = dataDf[self.symbolColumn].unique()
        # print 'symbols in data: {}'.format(symbolsArray)
        df_list=[]

        for i, sym in enumerate(symbolsArray):
            newSymData = dataDf.loc[dataDf[self.symbolColumn] == sym][[self.dateColumn, self.priceColumn]]
            newSymData[self.dateColumn] = pd.to_datetime(newSymData[self.dateColumn], format=self.date_format)
                                                         # infer_datetime_format=True)
            newSymData = newSymData.set_index(self.dateColumn)
            newSymData.sort_index(inplace=True)
            earliest_date = newSymData.index.min()
            # earliest_date = pd.to_datetime(newSymData[self.dateColumn], format=self.date_format, infer_datetime_format=True).min()
            if start_date >= utc.localize(earliest_date):
                print(f'{i}.\tAdding sym=\'{sym}\': required {start_date.strftime("%Y-%m-%d")} >= '
                      f'earliest {earliest_date.strftime("%Y-%m-%d")}')

                # newSymData.dropna(axis=(0, 1), inplace=True)
                # newSymData.drop_duplicates(inplace=True)
                newSymData = newSymData[~newSymData.index.duplicated(keep='first')]
                if newSymData.empty:
                    print('\t\tSkipped as empty')
                elif len(newSymData.index) < 200:
                    # newSymData.to_csv('downloads/too_short_{}.csv'.format(sym))
                    print('\t\tSkipped as too short ({})'.format(len(newSymData.index)))
                elif final_date - dt.timedelta(days=7) >= utc.localize(newSymData.index.max()):
                    print(f'\t\tSkipped as latest date {newSymData.index.max()} is too far back')
                    print(f'\t\t\t{final_date} - 7 days >= {utc.localize(newSymData.index.max())}')
                else:
                    newSymData.index.names = [self.dateColumn]
                    newSymData.index = newSymData.index.tz_localize(pytz.utc)
                    newSymData.columns = [sym]
                    newSymData.to_csv('downloads/{}.csv'.format(sym))
                    newSymData = newSymData[newSymData.index >= start_date]
                    df_list.append(newSymData)
            else:
                print('{}.\tSkipped. sym=\'{}\': required {:%Y-%m-%d} < earliest {:%Y-%m-%d}'
                      .format(i, sym, start_date, earliest_date))

        df_ret = pd.concat(df_list, axis=1, join='outer')
        df_ret.to_csv('downloads/df_before_dropna_tresh.csv')
        df_ret.replace(r'^\s*$', np.nan, regex=True, inplace = True)
        sparseness = df_ret.isnull().sum() / len(df_ret.index)
        print('max_sparseness={}, type(max_sparseness)={}'.format(self.max_sparseness, type(self.max_sparseness)))
        cols_to_keep = sparseness < self.max_sparseness
        cols_to_drop = ~cols_to_keep
        df_ret = df_ret.loc[:, cols_to_keep]
        print('cols_to_drop:')
        print(cols_to_drop[cols_to_drop == True])
        df_ret.sort_index(inplace=True)
        df_ret.to_csv('downloads/df_after_dropna_tresh.csv')
        df_ret = df_ret.fillna(method='bfill').fillna(method='ffill')
        df_ret.index.names = ['date']
        df_ret.to_csv('downloads/df_ret.csv')
        return df_ret
