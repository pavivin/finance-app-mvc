import yfinance as yf

from exceptions import NotFoundError

class InvestService:
    @staticmethod
    def get_current_data_by_ticker(ticker_name: str):
        ticker = yf.Ticker(ticker_name)
        info = ticker.info

        return {
            'currency': info['currency'],
            'summary': info['longBusinessSummary'],
            'short_name': info['shortName'],
            'recommendation_key': info['recommendationKey'],
            'last_divident_date': info['exDividendDate'],
            'previous_close': info['previousClose'],
            'logo_url': info['logo_url']
        }

    @staticmethod
    def get_history_data_by_ticker(ticker_name: str, period: str, interval: str):
        """
        Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                Either Use period parameter or use start and end
        interval : str
            Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            Intraday data cannot extend last 60 days
        """
        ticker = yf.Ticker(ticker_name)
        if ticker.session is None:
            return NotFoundError()
        data = ticker.history(period=period, interval=interval)
        return data.to_dict()
