import yfinance as yf


def data_download(ticker, ticker_start_date, ticker_end_date, ticker_interval):
    ticker_download = yf.download(ticker, start=ticker_start_date, end=ticker_end_date, interval=ticker_interval)
    return ticker_download

def save_data(filename, data):
    data.to_csv(filename, index=False)

if __name__ == "__main__":
    ticker = "NVDA"
    start_date = "2024-01-11"
    end_date= "2024-07-11"
    interval = "5d"
    data = data_download(ticker, start_date, end_date, interval)
    save_data('StockMarketAnalysis/data/raw/nvda_stock_data.csv', data)

    


