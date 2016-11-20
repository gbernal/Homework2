import mediacloud, datetime
import json, ast 
import unittest
import logging


from electorialDisaster import MediaFrenzy

mc = mediacloud.api.MediaCloud('0a65d2b3a0780cf15a40ca6914fe2dfeed17257e30b440c0ddffdfbc179635cd')
wordsC = mc.wordCount('( clinton )',  solr_filter=[mc.publish_date_query( datetime.date( 2016, 7, 1), datetime.date( 2016, 8, 1) ), 'tags_id_media:1' ] )

# This metthod will test basic function of a function or class that imports mediacloud API

#It will check connection, name of politician and number of mentions

class Election_Fuckup(unittest.TestCase):
    
    def setUp(self):
        
        self.results = MediaFrenzy('0a65d2b3a0780cf15a40ca6914fe2dfeed17257e30b440c0ddffdfbc179635cd')  
    def test_load(self):
        
        self.results.load()
        logging.basicConfig(filename ='MediaCloudAccess.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.warning('API accessed time.')
        assert self.results is not None

    def test_getCount(self):
        self.results.load()
        assert self.results.getCount(wordsC) == 1048
    def test_getName(self):
        self.results.load()
        assert self.results.getName(wordsC) == 'clinton'
        

if __name__ == "__main__":
    unittest.main()
