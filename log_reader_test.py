from log_reader import LogReader

# 2014-01-09T06:16:53.748849+00:00 
# heroku[router]: 
# at=info 
# method=POST 
# path=/api/online/platforms/facebook_canvas/users/100002266342173/add_ticket 
# host=services.pocketplaylab.com 
# fwd="94.66.255.106" 
# dyno=web.12 
# connect=12ms 
# service=21ms 
# status=200 
# bytes=78

class TestReader:
    reader = None
        
    def setup(self):
        pass
 
    def teardown(self):
        pass
 
    @classmethod
    def setup_class(cls):
        cls.reader = LogReader('test_log.log')

    def test_read_log(self):
        result = self.reader.data
        
        exspect = {
            'None' : 0,
        }

        assert len(result) == 1
        assert  exspect == result
