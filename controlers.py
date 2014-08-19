import core
import views
from utils import log, parse_args


def not_found(argv):
	log("todo: '%s' is not a valid command. See 'todo help'." % (argv[0],), 0)


def home(argv):
	help(['home'])


def help(argv):
	views.show('help')


def list(argv):
	f = core.get_todo_path()
	log("Todo list from '%s': " % (f,))
	l = views.read(f) or ' (Empty)'
	log(l)


def add(argv):
	if len(argv) < 2:
		log('todo: You must describe the idea you want to add.', 0)
		exit(1)

	f = core.get_todo_path()

	idea = argv[1]
	taglist = ','.join(argv[2:])
	index = core.new_index(f)
	line = '%d:%s:%s' % (index, taglist, idea)

	log("Append '%s' to '%s': " % (line, f))
	with open(f, 'a') as todo:
		todo.write(line + '\n')


def remove(argv):
	if len(argv) < 2:
		log('todo: You must specify what idea you want to remove.', 0)
		exit(1)

	index = int(argv[1])

	f = core.get_todo_path()
	with open(f, 'r') as old_todo:
		todo = old_todo.readlines()

	with open(f, 'w') as new_todo:
		for line in todo:
			if int(line.split(':', 1)[0]) == index:
				log("Line '%s' removed from '%s'" % (line[:-1], f))
				break
			else:
				new_todo.write(line)
		else:
			log('todo: No idea found at index %d' % (index,), 1)
