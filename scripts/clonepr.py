#!/usr/bin/python

import sys
import re
import rbtools
from rbtools.api.client import RBClient



if __name__ == '__main__':
    review_id = sys.argv[1]
    root = RBClient('http://rb.hotel.com').get_root()
    r1 = root.get_review_request(review_request_id=review_id)
    summary = r1['summary'] 
    bugs_closed_str = ",".join(list(r1['bugs_closed']))
    bugs_closed_str = "[%s]"%(bugs_closed_str)

    #summary=re.sub( bugs_closed_str, '', summary)
    summary=summary.replace( bugs_closed_str, '')

    diffs = r1.get_diffs()
    changed_files = diffs[-1].get_files()
    changed_files_str = ""
    for file in changed_files:
	file_name = file['source_file']
	#'/branches/sh-i53-bugs/front_end/modules/bulk/bulk_en.properties'
	#assumption is the file pattern is like this
	nth = [ m.start() for m in re.finditer(r"/",file_name)]
	file_name_pat = file_name[nth[2]+1:]
	changed_files_str += file_name_pat + " "

    command = r'svn commit -m "review %s , fixes %s: %s" %s' %(review_id, bugs_closed_str, summary, changed_files_str ) 

    print command

    if ( len(sys.argv) > 2 and sys.argv[2] == '-e'):
	import subprocess
	process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
	process.wait()


	
	
    
	
	
