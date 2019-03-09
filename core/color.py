# -*- coding: utf-8 -*-
# Part of root-me

import platform
from colorama import *
# Modules

if platform.system() == ("Linux" or "Darwin"):
	# --> UNIX colors
	R = "\033[91m"
	O = "\033[0m"
	G = "\033[32m"
	Y = "\033[93m"
	B = "\033[94m"
	BOLD = "\033[1m"
	ERROR = R + "[ERROR] " + O
	PASS = G + "[+] " + O
	INFO = B + BOLD + "[INFO] " + O
	MED = Y + "[~] " + O
	SEMI = Y + "[+] " + O
	OOPS = R + BOLD + "[OOPS!] " + O
	OH = G + BOLD + "[OH!] " + O
	PLUS = B + BOLD + "[+] " + O

elif platform.system() == "Windows":
	# --> Windows colors
	R = Fore.RED
	O = Fore.RESET
	G = Fore.GREEN
	Y = Fore.YELLOW
	B = Fore.BLUE
	BOLD = Style.BRIGHT
	ERROR = R + "[ERROR] " + O
	PASS = G + "[+] " + O
	INFO = B + BOLD + "[INFO] " + O
	MED = Y + "[~] " + O
	SEMI = Y + "[+] " + O
	OOPS = R + BOLD + "[OOPS!] " + O
	OH = G + BOLD + "[OH!] " + O
	PLUS + B + BOLD + "[+] " + O
