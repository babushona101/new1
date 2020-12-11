#!/usr/bin/python3

import os,sys

def List(dir):
	files = os.listdir(dir)
	for file in files:
		print("THE OBJ3CT IS ",file)
		path = os.path.join(dir,file)
		print("TH3 PATH IS " ,path)
		print( "#" * 20 )
def main():
	List(sys.argv[1])

if __name__ == '__main__':
	main()
