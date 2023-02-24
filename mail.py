#!/bin/python
import os

def Main():
	print("-----------------------------------------------------------------------------------")
	print("Mail (Temporary email creator) by Awkward_Lancer (https://github.com/AwkwardLancer)")
	print("-----------------------------------------------------------------------------------")
	print("")
	print("Thank you for using mail :) ")
	print("")
	print("Instructions: use the temporary email in any mailbox, then, if you receive an email, you will receive a link containing the message's content, which can be seen in the terminal by running this command in another shell:curl -s '<url>' | jq")
	print("")
	print("Here is your temporary email, if you want another email, please close the program and run it again!")
	print("")
	try:
		os.system("python3 -m ote")
	except:
		os.system("python -m ote")
if __name__ == "__main__":
	Main()
