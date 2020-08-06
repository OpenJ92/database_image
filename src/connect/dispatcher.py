from src.connect.PostgreSQL import PostgresSQL

class connect(object):
    databases =  {
                    "PostgresSQL" : PostgresSQL,
                  }
    def __init__(self, database, name, config):
        self.connection = connect.databases[database](name, config)
