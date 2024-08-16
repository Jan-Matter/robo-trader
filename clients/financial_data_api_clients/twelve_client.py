from clients.financial_data_api_clients.client_abc import FinancialDataAPIClientABC

from twelvedata import TDClient

class TwelveClient(FinancialDataAPIClientABC):

    def __init__(self, api_key: str):
        self.__client = TDClient(apikey=api_key)
    

    def get_financial_data(self, ticker: str, year: int, quarter: int) -> dict:
        pass



if __name__ == '__main__':
    from dotenv import load_dotenv, find_dotenv
    import os

    load_dotenv(find_dotenv())
    api_key = os.getenv("TWELVE_API_KEY")
    client = TDClient(apikey=api_key)
    fres = client.get_balance_sheet(
        symbol='AAPL'
    )
    fres_df = fres.as_pandas()
    
    print(fres_df)

