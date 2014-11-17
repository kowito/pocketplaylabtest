from log_reader import LogReader
from dateutil.parser import parse

class TestLogReader:
    reader = None
        
    def setup(self):
        pass
 
    def teardown(self):
        pass
 
    @classmethod
    def setup_class(cls):
        cls.reader = LogReader('test_log.log')

    def test_log_reader(self):
        result = self.reader.data
        
        
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

        assert len(result) == 1
        assert  expect == result[0]
