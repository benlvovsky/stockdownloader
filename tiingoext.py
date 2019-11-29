import pandas_datareader as pdr
from pandas_datareader.tiingo import TiingoDailyReader, TiingoQuoteReader
import requests


class TiingoExt(TiingoDailyReader):
    """
    Historical daily data from Tiingo on equities, ETFs and mutual funds
    """

    downloads_folder = 'downloads'

    def __init__(self, symbols, start=None, end=None, retry_count=3, pause=0.1,
                 timeout=30, session=None, freq=None, api_key=None, extheaders={}):
        super(TiingoExt, self).__init__(symbols, start=start, end=end, retry_count=retry_count,
                                        pause=pause, timeout=timeout, session=session, freq=freq, api_key=api_key)
        self.extheaders = extheaders

    def _read_one_data(self, url, params):
        """ read one data from specified URL """
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Token ' + self.api_key}
        headers.update(self.extheaders)
        print(f'url={url}')
        except_to_throw = None
        for i in range(self.retry_count):
            try:
                out = self._get_response(url, params=params, headers=headers).json()
                df = self._read_lines(out)
                df.to_csv(f'{self.downloads_folder}/{self._symbol}.csv')
                return df
            except requests.exceptions.ConnectionError as e:
                print('Exception {}'.format(e))
                except_to_throw = e
            except Exception as ee:
                print(f'Unexpected exception {ee}')
                except_to_throw = ee
                break   # on such exception no reason to retry

        print(f'Symbol skipped due to exception: {except_to_throw}')
        return None

    def read(self):
        df_orig = super(TiingoExt, self).read()
        df_orig = df_orig.reset_index()
        df_orig.to_csv(f'{self.downloads_folder}/df_orig_tiingo.csv')
        column_names = ['symbol', 'date', 'adjClose', 'adjHigh', 'adjLow', 'adjOpen', 'adjVolume', 'close', 'divCash', 'high', 'low', 'open', 'splitFactor', 'volume']
        df_orig.columns = column_names
        df_result = df_orig[['symbol', 'date', 'adjClose']]
        df_result.columns = ['symbol', 'date', 'close']
        df_result.to_csv(f'{self.downloads_folder}/df_tiingo_converted.csv')
        return df_result
