from django.db import connections
from Utilites.dbconnection.constant import DEFAULT_DB


class DbConnector:

    def __init__(self, *args, **kwargs):
        self.query = args[0]
        self.database = args[1]
        super(DbConnector, self).__init__(*args, **kwargs)

    @staticmethod
    def get_data_from_db(query: str, database: str):
        """
        Utility Method to get data of rows from table in database
        :param query:
        :param database:
        :return: tuple of row data
        """
        cursor = connections[database].cursor()
        cursor.execute(query)
        return cursor.fetchall()

    @staticmethod
    def get_data_from_db_with_columns(query: str, database: str):
        """
        Utility method to get row data and columns
        :param query:
        :param database:
        :return: list of column name and tuple or row data
        """
        cursor = connections[database].cursor()
        cursor.execute(query)
        column_names = list(cursor.description)
        row_data = cursor.fetchall()
        return column_names, row_data

    @staticmethod
    def get_cursor(database: str):
        """
        Utility method to get cursor in row/table
        :param database:
        :return:
        """
        return connections[database].cursor()
