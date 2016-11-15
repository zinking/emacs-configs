#!/usr/bin/python

import sys
import re
import subprocess


if __name__ == '__main__':
    #args = sys.argv
    #bran = args[1] if ( len(args)>0 ) else "sh-i53-bugs"
    #proj = args[2] if ( len(args)>1 ) else "mscm"
    #proj = args[1] if ( len(args)>0 ) else "mscm"

    #svncommand = 'svn st %s/%s'%(bran,proj)
    #svncommand = 'svn st %s'%(proj)
    #process = subprocess.Popen(svncommand, shell=True,
    #                       stdout=subprocess.PIPE, 
    #                       stderr=subprocess.PIPE)
    #process.wait()


    result = ""
    for line in sys.stdin.readlines():
	line = line.strip()
	if line[0] == '?' : continue
	if line[-1] == '1' : continue

	if line[0] not in ['M','A','D']: 
	    result += line + " "
	else:
	    result += line[2:]

    command = ""
    if len(sys.argv)>1 and sys.argv[1] == '-r' :
	command = 'post-review -r %s'%(sys.argv[2])
    print command, result

	
