import pandas as pd

from models.db_models import Operation
from settings.db_connection import Session

SIMPLE_SELECT_QUERY = """SELECT {fields} FROM {table1}"""
JOIN = """JOIN {table2} on {table1}.{join_field1}={table2}.{join_field2}"""


class DBQuery:

    def __init__(self, connection):
        self.query = None
        self.connection = connection

    def select(self, **kwargs):
        self.query = SIMPLE_SELECT_QUERY.format(fields=kwargs['fields'], table1=kwargs['table'])

    def select_all_fields(self, table: str = None):
        self.select(fields='*', table=table)
        return pd.read_sql(self.query, self.connection)

    def select_several_fields(self, table: str = None, fields: list[str] = None):
        self.select(fields=','.join(fields), table=table)
        return pd.read_sql(self.query, self.connection)

class InserWhitsSQLAlchemy:

    def add_operation(self, operation):
        try:
            db_session = Session()
            db_session.add(operation)
        except Exception as e:
            raise e
