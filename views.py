from utils import log

def home():
	with open('README.md', 'r') as readme:
		log(readme.readall())
