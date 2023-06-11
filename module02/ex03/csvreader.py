'''Context manager
An object which controls the environment seen in a with statement
by defining __enter__() and __exit__() methods.

import pathlib
import logging

file_path = pathlib.Path("hello.txt")

try:
    with file_path.open(mode="w") as file:
        file.write("Hello, World!")
except OSError as error:
    logging.error("Writing to file %s failed due to: %s", file_path, error)
    
'''

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.header_list = []
        self.data = []
        self.nb_col = 0
        self.nb_row = 0
        
    def __enter__(self):
        self.file = open(self.filename, mode="r")
        lines = self.file.readlines()
        first_length = len(lines[0].strip('\n').split(self.sep))
        if not all(len(line.strip('\n').split(self.sep)) == first_length and \
                   all(field for field in line.strip('\n').split(self.sep)) for line in lines):
            return None
        self.file.seek(0)
        if self.header:
            self.header_list = self.file.readline().strip('\n').split(self.sep)
            self.nb_col = len(self.header_list)
        else:
            self.first_line = self.file.readline().strip('\n').split(self.sep)
            self.nb_col = len(self.first_line)
            self.file.seek(0)
        if self.skip_top:
            for i in range(self.skip_top):
                self.file.readline()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            if isinstance(exc_val, FileNotFoundError):
                print("File not found")
                return True
            elif isinstance(exc_val, ValueError):
                print("File is not a valid CSV file")
                return True
            else:
                print("Error has been handled", exc_type, exc_val, exc_tb)
                return True

    def getdata(self):
        records_count = self.nb_col
        for line in self.file:
            self.nb_row += 1
            data_list = line.strip('\n').split(self.sep)
            if (len(data_list) != self.nb_col or len(data_list) != records_count):
                return None
            records_count = len(data_list)
            self.data.append(data_list)
        if self.skip_bottom:
            self.data = self.data[:-self.skip_bottom]
        return self.data
    
    def getheader(self):
        if self.header:
            return self.header_list
        else:
            return None