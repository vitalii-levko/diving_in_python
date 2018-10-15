#!/usr/bin/python3

from solution import FileReader

def _main():
    reader = FileReader('example.txt')
    print(reader.read())

if __name__ == '__main__':
    _main()
