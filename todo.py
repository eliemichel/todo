import sys
from os import path

from utils import log, parse_args
import views



def main():
	argv = sys.argv[1:]

	if argv == []:
		views.home()




if __name__ == '__main__':
	main()

