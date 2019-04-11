#coding:utf-8

import sys
import colorama
import subprocess

from core import rootme
from core import color
from core import helper

class Optionnal:
	def __init__(self):
		'''
			I call the options in the params
			file and testing variable
		'''
		self.USER  = rootme.USER
		self.LANG  = rootme.LANG
		self.CHAT  = rootme.CHAT
		self.STAT  = rootme.STAT
		self.CHAL  = rootme.CHAL
		self.MACH  = rootme.MACH
		self.POINT = rootme.POINT

        def call_informations(self):
            '''
                it's basic informations
                on the function and print the information.
            '''
            if(self.USER == None):
                helper.help()

            if(self.USER != None):
                print color.G + "\n[+] User : %s" %(self.USER)
                print color.G + "[+] URL : https://www.root-me.org/%s\n" %(self.USER)

	def __str__(self):
		'''
			Here we will test our variables
			and go the necessary functions.
		'''

		if(self.LANG != None):
			sys.exit(rootme.PollersLangs())

		elif(self.CHAT != None):
			sys.exit(rootme.PollersChat())

		# So concretely here we will test the variables and options.
		# The options are call in the params.py file.

		elif(self.STAT != None):
			sys.exit(rootme.PollersStatus())

		elif(self.CHAL != None):
			sys.exit(rootme.PollersChallenge())

		# In the conditions we call the functions and
		# then execute that on the servers 

		elif(self.POINT != None):
			sys.exit(rootme.PollersPoint())

		elif(self.MACH != None):
			sys.exit(rootme.PollersMachines())

if __name__ == "__main__":
	q = Optionnal()
	q.call_informations()
	q.__str__()
