from os import path

import params
from utils import log
import actuators

def read(f):
	with open(f, 'r') as text:
		return text.read()


def show_view(v):
	log(read(path.join(params.views_dir, v)))




def not_found(argv):
	log("todo: '%s' is not a valid command. See 'todo help'." % (argv[0],), 0)


def home(argv):
	help(['home'])


def help(argv):
	show_view('help')


def list(argv):
	f = actuators.get_todo_path()
	log("Todo list from '%s': " % (f,))
	l = read(f) or ' (Empty)'
	log(l)
