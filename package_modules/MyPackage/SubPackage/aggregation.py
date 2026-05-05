import os
def sum(lst):
	s = 0
	for i in lst:
		s = s+i
	return s
def print_cwd():
	return os.getcwd()