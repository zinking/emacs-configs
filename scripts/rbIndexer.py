#!/Users/ewngzen/anaconda/bin/python

import sys
import re
import rbtools
from rbtools.api.client import RBClient
import elasticsearch


class RBIndexer(object):
    def __init__(self,config):
        self.root = RBClient(config['url'],username=config['username'],password=config['password']).get_root()
        self.es = elasticsearch.Elasticsearch()

    def indexPage(self, page):
        def extractReviewObject(rr):
            ro = {}
            ro['id'] = rr.id
            ro['status '] = rr.status
            ro['description'] = rr.description
            ro['summary'] = rr.summary
            ro['time_added'] = rr.time_added
            last_update = rr.get_last_update()
            ro['last_update'] = last_update.timestamp if last_update is not None else ''
            lastDiffFiles = rr.get_diffs()[-1].get_files()
            diffFiles = map(lambda d:d.dest_file, lastDiffFiles)
            diffDevFiles = []
            diffTestFiles = []
            for diffFile in diffFiles:
                if diffFile.lower().find("test") == -1:
                    diffDevFiles.append(diffFile)
                else:
                    diffTestFiles.append(diffFile)
            ro['files'] = diffDevFiles
            ro['test_files'] = diffTestFiles
            ro['bugs_closed'] = list(rr.bugs_closed)
            ro['testing_done'] = rr.testing_done
            ro['target_groups'] = map(lambda g:g.title, rr.target_groups)
            ro['target_people'] = map(lambda g:g.title, rr.target_people)
            ro['repository'] = rr.get_repository().name
            ro['submitter'] = rr.get_submitter().username
            ro['change_count'] = len(rr.get_changes())
            ro['review_count'] = len(rr.get_reviews())
            ro['attach_count'] = len(rr.get_file_attachments())
            ro['screen_count'] = len(rr.get_screenshots())
            return ro

        indexed = []
        skipped = []
        for review in page:
            if review.status != "submitted":
                skipped.append(review.id)
                continue

            try:
                rbody = extractReviewObject(review)
                #self.es.index(index='rbs', doc_type='rb', id=review.id, body = rbody)
                #print rbody 
                print "."
                indexed.append(review.id)
            except Exception,e:
                print 'error indexing review:',review.id,e
        print 'Indexed one page','#'*30
        print 'indexed:',indexed
        print 'skipped:',skipped


    def index(self):
        page = self.root.get_review_requests(status = 'submitted')
        pagecount = 0
        while page is not None:
            print 'Indexing Page',pagecount
            self.indexPage(page)
            page = page.get_next(status = 'submitted')
            pagecount += 1

if __name__ == '__main__':
    config = {}
    config['url'] = 'http://rb.hotel.com'
    config['username'] = 'ewngzen'
    config['password'] = 'abcdefghi'
    indexer = RBIndexer(config)
    indexer.index()


