from src.database.PostgreSQL import PostgresSQL
from src.database.Snowflake import Snowflake

## Use default dict object to ressolve incorrcetly specified Database Sting object.
class connect(object):
    databases =  {
                    "PostgresSQL" : PostgresSQL,
                    "Snowflake"   : Snowflake
                  }
    def __init__(self, database, name, config):
        ## Database Object.
        self.connection = connect.databases[database](name, config)
