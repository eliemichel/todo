from os import path

import params
from utils import log

def show_text(txt):
	with open(path.join(params.views_dir, txt), 'r') as text:
		log(text.read())

def home():
	help(['home'])

def help(argv):
	show_text('help')

def not_found(argv):
	log("todo: '%s' is not a valid command. See 'todo help'." % (argv[0],), 0)

