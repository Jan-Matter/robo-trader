import pyodbc
import urllib
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

class SQLConnectorBase:

    def __init__(self, conn_str: str) -> None:
        self.__conn_str = conn_str

    @property
    def conn_str(self) -> str:
        return self.__conn_str
    
    @conn_str.setter
    def conn_str(self, conn_str: str) -> None:
        self.__conn_str = conn_str

    @property
    def sqlalchemy_db_uri(self) -> str:
        pass


    def connect(self) -> pyodbc.Connection:
        return pyodbc.connect(self.conn_str)
        

class PostgresqlConnector(SQLConnectorBase):
    
    def __init__(self, conn_str: str) -> None:
        super().__init__(conn_str)
    
    @property
    def sqlalchemy_db_uri(self) -> str:
        return f'postgresql+psycopg2://{self.conn_str}'
    

class MSSQLConnector(SQLConnectorBase):

    def __init__(self, conn_str: str) -> None:
        super().__init__(conn_str)
    
    @property
    def sqlalchemy_db_uri(self) -> str:
        return f'mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(self.conn_str)}'
    
    
class SQLLiteConnector(SQLConnectorBase):

    def __init__(self, conn_str: str) -> None:
        super().__init__(conn_str)
    
    @property
    def sqlalchemy_db_uri(self) -> str:
        return f'sqlite:///{self.conn_str}'
    
    def create_sqlite_db(self) -> None:
        if os.path.exists(self.conn_str):
            pass
        else:
            create_engine(self.sqlalchemy_db_uri, echo=True)
            Base = declarative_base()
            Base.metadata.create_all(create_engine(self.sqlalchemy_db_uri, echo=True))
            

    
if __name__ == '__main__':
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    connector = SQLLiteConnector(conn_str=os.getenv('DEV_POSTGRES_CONN_STR'))
    connection = connector.connect()
    cursor = connection.cursor()
        