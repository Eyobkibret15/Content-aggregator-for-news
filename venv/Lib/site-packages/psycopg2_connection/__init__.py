'''
Psycopg2 Connection is a very light module which makes some abstractions on top of the psycopg2
package. The goal is to help you write SQL code right into your python program, without needing
to worry about opening and closing connections to postgres.
'''
from .psycopg2_connection import PgDbConnector

__version__ = "0.1.1.1"
