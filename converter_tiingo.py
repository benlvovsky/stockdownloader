import pandas as pd


class FormatConverter:
    """
    converts file "upload" format into "upload1"
    Useful for files downloaded in one format to be processed with the  latest systems.
    """
    column_names = ["symbol", "date", "close", "high", "low", "open", "volume", "adjClose", "adjHigh", "adjLow",
                    "adjOpen", "adjVolume", "divCash", "splitFactor"]

    def __init__(self, start_date, symbols, download_path='downloads'):
        self.download_path = download_path
        self.start_date = start_date
        self.symbols = symbols

    def read(self):
        df_arr = []
        df_orig = None
        for s in self.symbols:
            try:
                print(f'reading {s} from file {self.download_path}/{s}.csv...', end='')
                ticker_df = pd.read_csv(f'{self.download_path}/{s}.csv')
                df_arr.append(ticker_df)
                print(f'read')
            except Exception as e:
                print(f'failed: {e}')

        print(f'merging all...', end='')
        # for dtf in df_arr:
        #     print(f'type(dtf) = {type(dtf)}')
        df_orig = pd.concat(df_arr, sort=False)
        print(f'done')

        df_result = df_orig[['symbol', 'date', 'adjClose']]
        df_result.columns = ['symbol', 'date', 'close']
        df_result.to_csv(f'{self.download_path}/df_converter_tiingo.csv')
        df_result.set_index('symbol')
        symbols = df_result.symbol.unique()
        print(f'type={type(symbols)}, symbols={symbols}, length={len(symbols)}')

        return df_result
