from log_reader import LogReader
from dateutil.parser import parse
import unittest

class TestLogReader(unittest.TestCase):
    @classmethod    
    def setUp(self):
        self.reader = LogReader('test_log.log')

    def test_log_reader(self):
        expect = {
            'date_time' : parse('2014-01-09T06:16:53.748849+00:00'),
            'at' : 'info' ,
            'method' : 'POST' ,
            'path' : '/api/online/platforms/facebook_canvas/users/100002266342173/add_ticket',
            'host' : 'services.pocketplaylab.com',
            'forward' : '94.66.255.106',
            'dyno' : 'web.12',
            'connection_time' : 12,
            'service_time' : 21,
            'response_status' : 200 ,
            'byte' : 78,
        }
        assert len(self.reader.dataset) == 5
        assert  expect == self.reader.dataset[0]