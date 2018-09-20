import sqlite3
import contextlib

connect = sqlite3.connect('/tmp/database.sqlite')
# try:
#     try:
#         cursor = connect.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS person (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 firstname varchar,
#                 lastname varchar)
#         """)
#         connect.commit()
#     except Exception:
#         connect.rollback()
#     try:
#         cursor = connect.cursor()
#         cursor.execute('INSERT INTO person(firstname, lastname) VALUEES (?, ?)', ('Beatrice', 'CARLES'))
#         connect.commit()
#     except Exception:
#         connect.rollback()
# finally:
#     connect.close()

# ecriture equivalente du haut avec context manager

@contextlib.contextmanager
def transaction(conn):
    try:
        print("J'ouvre un curseur")
        cursor = conn.cursor()
        yield cursor
        print("Je commit ma transaction")
        conn.commit()
    except Exception:
        print("Je rollback ma transaction")
        conn.rollback()

# deuxieme facon d'ecrire un context manager avec la creatioon d'une classe
# class Transaction:
#     def __init__(self,conn):
#         self.conn
#     def __enter__(self):
#         return self.conn.cursor()
#     def __exit__(selfself, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.conn.commit()
#         else:
#             self.conn.rollback()

with sqlite3.connect('/tmp/database.sqlite') as conn:
    with transaction(conn) as cur:
        cur.execute("""...""")
        cur.execute('INSERT INTO person(firstname, lastname) VALUES (?,?)', ('Beatrice', 'CARLES'))

@contextlib.contextmanager
def raises(ExceptionType):
    try:
        yield
        raise Exception('On attendait une exception')
    except ExceptionType:
        pass

