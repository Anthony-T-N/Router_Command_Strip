""" Router_Command_Strip

"""

__author__ = 'Anthony T Nguyen'
__version__ = '---'
__date__ = '06.09.2019'

import os

def line_strip(input_file, output_file):
	"""

	"""
	line = 0

def main():
	"""
	Begin
	"""
	if os.path.exists("router.txt"):
		input_file = open("router.txt", "r")
		output_file = open("new_router.txt", 'w')
		line_strip(input_file, output_file)
	else:
		print("File not there")
		input_file = open("router.txt", "w")
	input_file.close()
	
  
if __name__ == '__main__':
    main()
