#!/usr/bin/python3
import sys
from os import path

import params
import controlers
from utils import parse_args

commands = {
	'home'  : controlers.home,
	'help'  : controlers.help,
	'list'  : controlers.list,
	'ls'    : controlers.list,
	'add'   : controlers.add,
	'remove': controlers.remove,
	'rm'    : controlers.remove,
	...     : controlers.not_found,
}

options = {
	'--verbose': ('verbose', bool),
}


args = parse_args(options)

if args['verbose']:
	params.loglevel = 3

argv = args[...]
cmd = argv[0] if argv != [] else 'home'
commands.get(cmd, commands[...])(argv)
