#!/usr/bin/python3

#importing os and sys module from python library

import os, sys

# for taking the file and folder name as one into directory/location

def List_file(dir):
	filename = os.listdir(dir)
	for file in filename:
		print( file )

# defining main function

def main():
	List_file(sys.argv[1])

if __name__ == '__main__':
	main()
