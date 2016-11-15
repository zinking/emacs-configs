#!/usr/bin/python
# mgrt.py kunlun-i53-clone-sitelinks sh-i53-bugs mscm

import sys
import re
import subprocess


if __name__ == '__main__':
    args = sys.argv
    target_branch = args[1] if len(args) > 1 else 'kunlun-i53-clone-sitelinks'
    source_branch = args[2] if len(args) > 2 else 'sh-i53-bugs'
    source_proj   = args[3] if len(args) > 3 else 'mscm'

    svncommand = 'svn st %s/%s'%(source_branch,source_proj)
    process = subprocess.Popen(svncommand, shell=True,
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE)
    process.wait()

    # wait for the process to terminate
    for line in process.stdout: 
	print 'migrate change: %s'%(line)
	filename = line[2:].strip()
	if( filename[len(filename)-1] == "1"):
	    print "skip tempoarary file:"
	    continue;

	tgtfilename = filename.replace( source_branch, target_branch )
	cpcmd = "cp %s %s"%( filename, tgtfilename )
	process = subprocess.Popen( cpcmd, shell=True, stdout=subprocess.PIPE )
	process.wait()
	
	
    
    #errcode = process.returncode
