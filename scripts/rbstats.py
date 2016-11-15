#!/usr/bin/python

import sys
import re
import numpy as np
import rbtools
from rbtools.api.client import RBClient

def resource_iterator( resources ):
     while True:
	for resource in resources:
	    yield resource
	try:
	    resources = resources.get_next()
	except StopIteration:
	    break

def print_statistics_header():
    print 'name', 'review count', 'max revisions', 'min revisions', 'avg revisions', 'var revisions', 'max reviews', 'min reviews', 'avg reviews', 'var reviews', '\n'

def calculate_statistics( arr ):
    if len(arr) == 0: arr=[0]
    return np.max(arr), np.min(arr), np.mean(arr), np.var(arr)

def print_statistics(name, n, ucrs, urns):
    print name, n, calculate_statistics(ucrs), calculate_statistics(urns)

if __name__ == '__main__':
    root = RBClient('http://rb.hotel.com').get_root()
    rusers = root.get_users()
    print_statistics_header()
    for u in resource_iterator(rusers):
	uname = u['username']
	ureviews = root.get_review_requests(from_user=uname,status='submitted')
	ucrs = []
	urns = []
	n = 0
	for r in resource_iterator(ureviews):
	    code_revisions = len(r.get_diffs())
	    review_numbers = len(r.get_reviews())
	    ucrs.append(code_revisions)
	    urns.append(review_numbers)
	    n+=1
	print 'LOG ', uname, ucrs, urns, '\n'
	print_statistics(uname, n, ucrs, urns)
	
	
	
 

   
	
	
