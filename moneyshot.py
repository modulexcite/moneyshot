#!/usr/bin/python

import sys
import colors
import outputter
import codelibrary
import codeparameters
import lolsled
import builder
import pattern
import ezrop
import pprint
import fmt
import shell

def banner():
	ms_fancy  = colors.bold() + colors.fg('yellow') + "$$$ " + colors.end()
	ms_fancy += colors.bold() + "moneyshot" + colors.end()
	ms_fancy += " by "
	ms_fancy += colors.bold() + "blasty"  + colors.end()
	ms_fancy += colors.bold() + colors.fg('yellow') + " $$$" + colors.end()

	sys.stderr.write("\n " + ms_fancy + "\n\n")

def usage():
	print ""
	print "  usage: moneyshot <action> [options]\n"
	print "  actions:"
	print "    * list     - list shellcodes"
	print "    * build    - build shellcodes"
	print "    * pattern  - build patterns"
	print "    * lolsled  - build a lolsled"
	print "    * format   - format input"
	print "    * fmt      - formatstring helper"
	print "    * rop      - ROP helper\n"

def warning(instr):
	print "  " + colors.fg('red') + colors.bold() + "!!" + colors.end() + " " + instr

def action_list(path = ""):
	codes = codelibrary.find_codes(path)
	print ""
	codelibrary.print_codes(codes)

if len(sys.argv) == 1:
	banner()
	usage()
	exit()

action = sys.argv[1]

codelibrary.load_codes(sys.path[0] + "/codes")

if action == "list":
	if len(sys.argv) == 3:
		action_list(sys.argv[2])
	else:
		action_list()

elif action == "fmt":
	fmt.main(sys.argv[2:])

elif action == "rop":
	ezrop.main(sys.argv[2:])

elif action == "lolsled":
	lolsled.main(sys.argv[2:])

elif action == "pattern":
	pattern.main(sys.argv[2:])

elif action == "shell":
	shell.main(sys.argv[2:])

elif action == "format":
	outputter.main(sys.argv[2:])

elif action == "build":
	builder.main(sys.argv[2:])

else:
	banner()
	usage()
	exit()
