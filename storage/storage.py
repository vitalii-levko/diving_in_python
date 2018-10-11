#!/usr/bin/python3

import os
import tempfile
import argparse
import json
import sys

def store_val(key, val):
	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

	if os.path.isfile(storage_path) and os.path.getsize(storage_path) != 0:

		with open(storage_path, 'r+') as f:
			storage = json.load(f)
			
			if not key in storage:
				storage[key] = val
			elif isinstance(storage[key], list) :
				storage[key].append(val)
			else:
				storage[key] = [storage[key], val]

			f.seek(0)
			json.dump(storage, f)

	else:
		
		with open(storage_path, 'w') as f:
			storage = {key: val}
			json.dump(storage, f)

def read_val(key):
	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

	if os.path.isfile(storage_path) and os.path.getsize(storage_path) != 0:

		with open(storage_path, 'r') as f:
			storage = json.load(f)

			if key in storage:

				if isinstance(storage[key], list):
					print(', '.join(storage[key]))
				else:
					print(storage[key])
				
				sys.exit()

	print('None')

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="key name")
parser.add_argument("--val", help="value")
args = parser.parse_args()

if args.key is None:
	sys.exit()

if not args.val is None:
	store_val(args.key, args.val)
else:
	read_val(args.key)
