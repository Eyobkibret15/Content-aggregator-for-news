'''
Module with helper functions for making connections to the postgres database
'''
import psycopg2

class PgDbConnector:
    '''
    Has methods that makes connections to the DB a little cleaner.
    You will need to add the following class attributes to connect to your database:
        host = 'Your host name'
        dbname = 'Your database name'
        user = 'Your username'
        password = 'Your password'
    '''
    host = str()
    dbname = str()
    user = str()
    password = str()

    def connect_to_db(self):
        '''
        Connects the database and returns a connection.
        '''
        conn = psycopg2.connect(
            host=self.host,
            dbname=self.dbname,
            user=self.user,
            password=self.password,
        )
        return conn

    def fetch_records(self, sql):
        '''
        Return results of a select query.
        '''
        conn = self.connect_to_db()
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
        conn.close()


    def execute_and_commit(self, sql):
        '''
        Updates records based on an sql query.
        '''
        conn = self.connect_to_db()
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                conn.commit()
        conn.close()

    def copy_from_file(self, io_file, pg_table, *table_columns):
        '''
        Copies from a file-like object to a postgres table.
        '''
        conn = self.connect_to_db()
        with conn:
            with conn.cursor() as cur:
                cur.copy_from(
                    io_file,
                    pg_table,
                    columns=table_columns)
                conn.commit()
        conn.close()

    def copy_to_file(self, io_file, pg_table, *table_columns):
        '''
        Copies to a file-like object from a postgres table.
        '''
        conn = self.connect_to_db()
        with conn:
            with conn.cursor() as cur:
                cur.copy_to(
                    io_file,
                    pg_table,
                    columns=table_columns)
                conn.commit()
        conn.close()
        