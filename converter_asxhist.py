import pandas as pd

column_names = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']


class FormatConverter():
    """
    converts file "upload" format into "upload1"
    Useful for files downloaded in one format to be processed with the  latest systems.
    """
    def __init__(self, start_date, file_name='data.csv'):
        self.start_date = start_date
        self.column_names = column_names
        self.file_name = file_name

    def read(self):
        df_orig = pd.read_csv(self.file_name, delimiter=',')
        df_orig.columns = column_names
        df_result = df_orig[['Ticker', 'Date', 'Close']]
        df_result.columns = ['symbol', 'date', 'close']
        df_result.to_csv('downloads/df_converter.csv')
        df_result.set_index('symbol')
        symbols = df_result.symbol.unique()
        # symbols = df_result.groupby('symbol').nunique()
        print(f'type={type(symbols)}, symbols={symbols}')
        # for s in symbols:
        #     ticker = df_result[df_result['symbol'] == s]
        #     ticker = ticker.set_index('symbol')
        #     ticker.to_csv(f'downloads/{s}.csv')

        # symbols_only.to_csv('downloads/symbols')
        # df_result.reset_index('symbol')

        return df_result
