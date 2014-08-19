import sys

import params


def log(msg, level=2):
	"""Print log messages whom level is bellow loglevel
	level: -1: mute (not implemented), 0: Error only, 1: Warnings, 2: Info, 3: Verbose"""
	if level <= params.loglevel:
		print(msg)


def parse_args(options, argv=None):
	"""Parse args from [argv] (default to sys.argv) and return a dict
	associating values to option names. Remaining args are listed in
	Ellipsis entry of the returned dict."""
	argv = argv or sys.argv[1:]
	args = {o: None for o in options.values()}
	args[...] = [] # Remaining arguments
	cur = None
	for arg in argv:
		if cur != None:
			args[cur] = arg
			cur = None
		else:
			if arg in options:
				cur = options[arg]
			else:
				args[...].append(arg)

	return args

