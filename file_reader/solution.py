#!/usr/bin/python3

class FileReader:
    
    def __init__(self, file_path):
        self._file_path = file_path

    def read(self):
        try:
            with open(self._file_path) as f:
                content = f.read()
            return content
        except IOError:
            return ''
