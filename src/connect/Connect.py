from yaml import load, FullLoader
from os.path import expanduser
from pandas import read_sql

class CONNECT(object):
    def __init__(self, name, connect, config):
        self.name = name
        self._connect = connect
        self._configuration = self._process_configuration(config)

    def __enter__(self):
        breakpoint()
        self._connection = self._connect(**self._configuration[self.name])
        ## TODO :: BUG 
        ## OperationalError: could not connect to server: Connection refused
        ##         Is the server running on host "localhost" (::1) and accepting
        ##         TCP/IP connections on port 5432?
        ## could not connect to server: Connection refused
        ##         Is the server running on host "localhost" (127.0.0.1) and accepting
        ##         TCP/IP connections on port 5432?
        return self._connection

    def __exit__(self, exception_type, exception_value, traceback):
        self._connection.close()

    def _process_configuration(self, config):
        configuration = f"{expanduser('~')}/.dbm/{DBTYPE}/config.yml" if not config else config
        with open(configuration, 'r') as c:
            return load(c, Loader=FullLoader)

    def _extract(self, sql):
        return read_sql(sql, self._connection)
