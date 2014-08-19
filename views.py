from os import path

import params
from utils import log

def read(f):
	with open(f, 'r') as text:
		return text.read()


def show(v, bindings={}):
	txt = read(path.join(params.views_dir, v))
	for k, v in bindings:
		txt = txt.replace('{{' + k + '}}', v)
	log(txt)