#!/usr/bin/python3

import os,sys

#TO lIst the contents of a directory we use os.listdir(directory name
#TO pRint the path we use os.path.join() which joins the elements in an intelligent way seperating them with /
#TO fInd absolute path we use os.path.abspath() which provides us with the absolute path

def List(dir):
	files = os.listdir(dir)
	for file in files:
		print("THE OBJ3CT IS ",file)
		path = os.path.join(dir,file)
		print("TH3 PATH IS " ,path)
		print("TH3 ABSOLUTE PATH IS ", os.path.abspath(path))
		print( "#" * 20 )
def main():
	List(sys.argv[1])

if __name__ == '__main__':
	main()
