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
	args = {o[0]: None for o in options.values()}
	args[...] = [] # Remaining arguments

	argv = iter(argv or sys.argv[1:])
	for arg in argv:
		if arg in options:
			k, t = options[arg]
			args[k] = True if t == bool else t(next(argv))
		else:
			args[...].append(arg)

	return args

