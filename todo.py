#!/usr/bin/python3
import sys
from os import path

import params
import controlers

commands = {
	'home': controlers.home,
	'help': controlers.help,
	'list': controlers.list,
	'ls'  : controlers.list,
	'add' : controlers.add,
	...   : controlers.not_found,
}


argv = sys.argv[1:]
cmd = argv[0] if argv != [] else 'home'
commands.get(cmd, commands[...])(argv)
