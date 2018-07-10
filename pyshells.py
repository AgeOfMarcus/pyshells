#!/usr/bin/python3

import argparse, os
from subprocess import Popen, PIPE
from termcolor import colored as c

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-g",
		help=("Generate a password-protected payload. Example: gen lamepassword"))
	parser.add_argument(
		"-c",
		help=("Connect to a server running the payload. Example: conn 192.168.0.24 lamepassword"))
	return parser.parse_args()

