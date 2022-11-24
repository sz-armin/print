import unittest
from src.main import CSVPrinter

DATA_F= 'data/test.csv'
class TestCSVPrinter(unittest.TestCase):
    def test_one(self):
        printer = CSVPrinter(DATA_F)
        l = printer.read()
        self.assertEqual(3, len(l))

    def test_two(self):
        printer = CSVPrinter(DATA_F)
        l = printer.read()
        f = open(DATA_F, 'r')
        for line1, line2 in zip(l, f):
            self.assertEqual(line1, line2.strip().split(','))
        f.close()

    def test_three(self):
        with self.assertRaises(FileNotFoundError):
            printer = CSVPrinter('data/nonexistent.csv')
            printer.read()
