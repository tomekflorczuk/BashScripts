#!/usr/bin/python

import sys;
import os;

if len(sys.argv)!=3:
	print("Niepoprawna ilosc argumentow")
	exit()

if not os.path.isdir(sys.argv[1]):
	print("argument nie jest katalogiem")
	exit()

cat = os.path.join(os.getcwd(), sys.argv[1])
ext = sys.argv[2]

with open('result', 'w') as outfile:
	for file in os.listdir(cat):
		if file.endswith(ext):
			with open(os.path.join(cat, file)) as infile:
				print (os.path.join(cat, file))				
				print file
				outfile.write(file)
				outfile.write('\n')			
				outfile.write(infile.read())


