""" Router_Command_Strip

A python script that takes a text file containing a list of commands for routers. The script then strips away unnecessary
parts that prevent the router from accepting the command.

"""

__author__ = 'Anthony T Nguyen'
__version__ = '---'
__date__ = '06.09.2019'

import os

def line_strip(input_file, output_file):
	"""
	Takes the existing text files as inputs.
	"""
	line = 0
	for current_line in input_file:
		if ('#' in current_line):
			current_line = current_line.split('#', 1)[-1]
			current_line = current_line.lstrip(' ')
		print(current_line)
		output_file.write(current_line)
		line += 1
	print(line)

def main():
	"""
	Begin
	"""
	if os.path.exists("router.txt"):
		input_file = open("router.txt", "r")
		output_file = open("new_router.txt", 'w')
		line_strip(input_file, output_file)
	else:
		print("[-] File not found")
		input_file = open("router.txt", "w")
	input_file.close()
	
  
if __name__ == '__main__':
    main()
