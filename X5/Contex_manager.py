import sqlite3
from contextlib import contextmanager


# Type 1
class DataConn:

    def __init__(self, db_name):
        """Конструктор"""
        self.db_name = db_name

    def __enter__(self):
        """
        Открываем подключение с базой данных.
        """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Закрываем подключение.
        """
        self.conn.close()
        if exc_val:
            raise


# Type 1
# if __name__ == '__main__':
#    db = 'test.db'
#
#    with DataConn(db) as conn:
#       cursor = conn.cursor()

# Type 2

class Resource:
    def __init__(self, db_name):
        """Конструктор"""
        self.db_name = db_name

    def open(self):
        print("open")

    def close(self):
        print('close')


@contextmanager
def open_resource():
    resource = None
    try:
        resource = Resource('test')
        resource.open()
        yield resource
    except:
        raise
    finally:
        if resource:
            resource.close()


open_resource()
