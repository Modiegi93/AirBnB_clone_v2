#!/usr/bin/python3
from models.state import State
from models.engine.db_storage import DBStorage
import unittest
import MySQLdb
import pep8
import os


class TestDBStorage(unittest.TestCase):
    """A class to test db storage"""

    @classmethod
    def setUpClass(cls):
        """Set up MySQL"""
        cls.db = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user='hbnb_test',
                                 passwd='hbnb_test_pwd',
                                 db='hbnb_test_db',
                                 charset='utf8')
        cls.cur = cls.db.cursor()
        cls.storage = DBStorage()
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        """Tear down MySQL"""
        cls.cur.close()
        cls.db.close()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db')
    def test_pep8_DBStorage(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db')
    def test_add(self):
        """Test add method"""
        self.cur.execute("""
            INSERT INTO states (id, created_at, updated_at, name)
            VALUES (1, '2017-11-10 00:53:19', '2017-11-10 00:53:19',
                    "California")
            """)
        self.db.commit()
        self.cur.execute('SELECT * FROM states')
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)


if __name__ == "__main__":
    unittest.main()
