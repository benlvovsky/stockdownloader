import requests
import glob
import pandas as pd


class MarketIndex:
    """
    Historical daily data from Marketindex
    """
    # example: https://www.marketindex.com.au/sites/default/files/historical-data/AWC.csv
    url_sympol_prefix = 'https://www.marketindex.com.au/sites/default/files/historical-data/'
    column_names = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    # column_names = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']

    def __init__(self, symbols, start=None, end=None, retry_count=3, pause=0.1,
                 timeout=30, session=None, freq=None, api_key=None, extheaders={}):
        self.symbols = symbols
        self.start = start
        self.end = end
        self.download_path = 'downloads'
        self.retry_count = retry_count
        self.pause=pause
        self.timeout = timeout
        self.session = session
        self.freq = freq
        self.api_key = api_key
        self.extheaders = extheaders

    def read(self):
        print(f'downloading all symbols...')
        for s in self.symbols:
            url = f'{self.url_sympol_prefix}{s}.csv'
            print(f'    downloading {s} from {url}...', end='')
            s = requests.Session()
            s.trust_env = False
            r = s.get(f'{url}')
            open(f'{self.download_path}/{s}.csv', 'wb').write(r.content)
            print(f'done')
            exit(0)

        print(f'merging...', end='')
        df_orig = pd.DataFrame()
        for s in self.symbols:
            ticker_df = pd.read_csv(f'{self.download_path}/{s}.csv')
            ticker_df['symbol'] = s
            df_orig = pd.concat(df_orig, ticker_df)

        df_result = df_orig[['symbol', 'Date', 'Close']]
        df_result.columns = ['symbol', 'date', 'close']
        df_result.to_csv('downloads/df_converter.csv', index=False)
        df_result.set_index('symbol')
        print(f'done')
