#!/usr/bin/python3
import sys
from os import path

import params
from utils import log, parse_args
import views


commands = {
	'help': views.help,
	...   : views.not_found,
}


def main():
	argv = sys.argv[1:]
	cmd = argv.get(0) or 'home'
	commands.get(cmd, commands[...])(argv)


if __name__ == '__main__':
	main()

