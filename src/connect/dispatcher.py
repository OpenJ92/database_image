from src.database.PostgreSQL import PostgresSQL
from src.database.Snowflake import Snowflake

class connect(object):
    databases =  {
                    "PostgresSQL" : PostgresSQL,
                    "Snowflake"   : Snowflake
                  }
    def __init__(self, database, name, config):
        self.connection = connect.databases[database](name, config)
