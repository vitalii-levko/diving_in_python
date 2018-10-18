#!/usr/bin/python3

import tempfile
import os
import string
from random import randint, choice

class File:
    def __init__(self, path):
        self.path = path
        self.content = None
        self.content_size = 0

    def __str__(self):
        return self.path

    def __add__(self, obj):
        chars_arr = string.ascii_letters + string.digits
        filename = ''.join(choice(chars_arr) for _ in range(randint(20, 30)))
        storage_path = os.path.join(tempfile.gettempdir(), '%s' % (filename))

        with open(self.path) as f:
            first_file = f.read()

        with open(obj.path) as f:
            second_file = f.read()

        file_content = '%s%s' % (first_file, second_file)

        with open(storage_path, 'w') as f:
            f.write(file_content)

        return File(storage_path)

    def __getitem__(self, index):
        if index+1 == self.content_size:
            self.content = None

        if self.content is None:
            with open(self.path, 'r') as f:
                self.content = f.readlines()
            self.content_size = len(self.content)

        return self.content[index].strip()

    def write(self, value):
        with open(self.path, 'a') as f:
            f.write(value)

def _main():
    obj = File('/tmp/file.txt')
    obj.write('line\n')

    for line in obj:
        print(line)

    print()    
    obj.write('line2\n')

    for line in obj:
        print(line)
    
    print(obj)
    print()

    first = File('/tmp/first')
    second = File('/tmp/second')

    first.write('line1\n')
    second.write('line2\n')

    new_obj = first + second

    for line in new_obj:
        print(line)

    print(new_obj)

if __name__ == '__main__':
    _main()
