"""connection handler"""

from sqlalchemy import create_engine

class DBConnectionHandler:
    """class responsible for handling the database connection
    """
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None

    def connect_to_db(self):
        """create the engine
        """
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        """get engine
        """
        return self.__engine

db_connection_handler = DBConnectionHandler()