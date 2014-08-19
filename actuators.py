import os
from os.path import join, exists, abspath, expanduser

import params
from utils import log

def create_todo_file(f):
	if not exists(f):
		open(f, 'x').close()
		log("File '%s' has been created." % (f,))
	

def get_todo_path(root=None):
	root = abspath(root or os.curdir)
	f = join(root, params.todo_filename)
	if exists(f):
		return f
	else:
		next_root = abspath(join(root, os.pardir))
		if next_root != root:
			return get_todo_path(next_root)
		else:
			home = expanduser('~')
			if home == '~':
				raise Exception('$HOME not found')
			f = join(home, params.todo_filename)
			create_todo_file(f)
			return f

def add(argv):

