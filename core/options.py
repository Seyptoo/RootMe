#coding:utf-8

from optparse import *
from threading import *

parser = OptionParser(add_help_option=False)
parser.add_option("-u", "--user", dest="user", help="Enter the user.")
parser.add_option("-l", "--lang", dest="lang", action="store_true", help="See the user's language.")
parser.add_option("-c", "--chatbox", dest="chatbox", action="store_true", help="See the number of chatboxes posted.")
parser.add_option("-s", "--status", dest="status", action="store_true", help="See the status of the user")
parser.add_option("-p", "--point", dest="point", action="store_true")
parser.add_option("-m", "--machines", dest="machines", action="store_true")
parser.add_option("-C", "--Challenge", dest="Challenge")
(options, args) = parser.parse_args()

PollersUser   = options.user
PollersLang   = options.lang
PollersChat   = options.chatbox
PollersStatus = options.status
PollersPoint  = options.point
PollersMachines  = options.machines
PollersChall  = options.Challenge
