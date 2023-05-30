import psycopg2.pool

import configparser
config = configparser.ConfigParser()
config.read('/home/aron/Vídeos/postgres_config.ini')

dbconfig = {
    "host":config.get('postgres', 'host'),
    "port":config.get('postgres', 'port'),
    "user":config.get('postgres', 'user'),
    "password":config.get('postgres', 'pass'),
    "database":config.get('postgres', 'database'),
}

class PostgresPool(object):
    """
    create a pool when connect postgresql, which will decrease the time spent in 
    request connection, create connection and close connection.
    """
    def __init__(self):             
        self.pool = self.create_pool(pool_name='task_pool', pool_size=3)

    def create_pool(self, pool_name, pool_size):
        """
        Create a connection pool, after created, the request of connecting 
        PostgreSQL could get a connection from this pool instead of request to 
        create a connection.
        :param pool_name: the name of pool, default is "mypool"
        :param pool_size: the size of pool, default is 3
        :return: connection pool
        """
        pool = psycopg2.pool.SimpleConnectionPool(
            pool_name=pool_name,
            maxconn=pool_size,
            **dbconfig)
        return pool

    def close(self, conn, cursor):
        """
        A method used to close connection of postgresql.
        :param conn: 
        :param cursor: 
        :return: 
        """
        cursor.close()
        conn.close()

    def execute(self, sql, args=None, commit=False):
        """
        Execute a sql, it could be with args and with out args. The usage is 
        similar with execute() function in module pymysql.
        :param sql: sql clause
        :param args: args need by sql clause
        :param commit: whether to commit
        :return: if commit, return None, else, return result
        """
        # get connection form connection pool instead of create one.
        conn = self.pool.getconn()
        cursor = conn.cursor()
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)
        if commit is True:
            conn.commit()
            self.close(conn, cursor)
            return cursor
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)
            return res

    def executemany(self, sql, args, commit=False):
        """
        Execute with many args. Similar with executemany() function in pymysql.
        args should be a sequence.
        :param sql: sql clause
        :param args: args
        :param commit: commit or not.
        :return: if commit, return None, else, return result
        """
        # get connection form connection pool instead of create one.
        conn = self

