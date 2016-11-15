#!/usr/bin/python

import sys
import re
import rbtools
import time
from rbtools.api.client import RBClient


#https://github.com/jantman/reviewboard-scripts/blob/master/list_mine.py

def postDraftReview(root):
    review_request = root.get_review_requests().create(repository=1)
    print 'Created Review to catch Fish'
    print '#'*10,review_request.id,'#'*10
    return review_request.id

if __name__ == '__main__1':
    URL = 'http://rb.hotel.com/'
    root = RBClient(URL,username='ewngzen',password='********').get_root()
    postDraftReview(root)


if __name__ == '__main__':
    URL = 'http://rb.hotel.com/r/?sort=-time_added,-last_updated'
    URL = 'http://rb.hotel.com/api/json/reviewrequests/all/'
    URL = 'http://rb.hotel.com/'
    MAX_RESULTS = 10
    root = RBClient(URL,username='ewngzen',password='abcdefghi').get_root()
    args = {}
    args['max_results'] = MAX_RESULTS
    args['sort'] = "-time_added"
    maxReqId = 0

    while True:
        reqs = root.get_review_requests(**args)
        MINUTE = 60*1
        MINUTE = 1 #for testing
        maxreview = []
        for review in reqs:
            if review.id > maxReqId:
                maxReqId = review.id
                maxreview = [review]

        for review in maxreview:
            print "CurrentTopReview: %d - %s - %s" % (review.id, review.get_submitter().username, review.summary)
            next10Reviews = range(review.id,review.id+20,2)
            next10ReviewIds = map(lambda x:str(x), next10Reviews)
            palIds = filter(lambda s:s==s[::-1],next10ReviewIds)
            if len(palIds) > 0:
                print "About to catch fish, current review:%d, target review %s"%(review.id,palIds)
                nextId = str(review.id + 2)
                if nextId == nextId[::-1]:
                    print 'Boom Post Review and I catch fish %s'%(nextId)
                    print '#'*20
                    #fishid = postDraftReview(root)
                    maxReqId = max(maxReqId, fishid)
                time.sleep(MINUTE)
            else:
                print "check point: review: %d, far from fish"%(review.id)
                time.sleep(5*MINUTE)





