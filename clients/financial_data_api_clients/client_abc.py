from abc import ABC, abstractmethod



class FinancialDataAPIClientABC(ABC):
    

    def __init__(self, api_key: str):
        self.api_key = api_key