import csv
import random


class CSVPrinter:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
            if random.randint(0, 1000) == 10:
                raise Exception('Random error')
            if random.randint(0, 500) == 20:
                raise Exception('Another random error')
        return lines
