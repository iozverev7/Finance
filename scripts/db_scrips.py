import pandas as pd

SIMPLE_SELECT_QUERY = """SELECT * FROM operation"""


class DBQuery:

    def __init__(self, connection):
        self.query = None
        self.connection = connection

    def select(self, fields, table):
        self.query = SIMPLE_SELECT_QUERY
        # print(kwargs['fields'])
        # self.query.format(fields=fields, table=table)

    def select_all_fields(self, table: str = None):
        self.select(fields='*', table=table)
        return pd.read_sql(self.query, self.connection)

    def select_several_fields(self, table: str = None, fields: list[str] = None):
        self.select(fields=','.join(fields), table=table)
        return pd.read_sql(self.query, self.connection)
