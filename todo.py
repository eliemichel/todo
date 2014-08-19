#!/usr/bin/python3
import sys
from os import path

import params
from utils import log, parse_args
import views
import actuators


commands = {
	'home': views.home,
	'help': views.help,
	'list': views.list,
	'add' : actuators.add,
	...   : views.not_found,
}


def main():
	argv = sys.argv[1:]
	cmd = argv[0] if argv != [] else 'home'
	commands.get(cmd, commands[...])(argv)


if __name__ == '__main__':
	main()

