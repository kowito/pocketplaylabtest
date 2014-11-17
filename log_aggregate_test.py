from log_reader import LogAggregate, LogReader
from dateutil.parser import parse
import unittest

from collections import defaultdict, Counter


class TestLogAggregate(unittest.TestCase):
    @classmethod    
    def setUp(self):
        self.reader = LogReader('test_log.log')

    def test_log_is_list_instance(self):
        self.assertIsInstance(self.reader.data, list)
    
    def test_log_value_is_dict_instance(self):
        self.assertIsInstance(self.reader.data[0], dict)

    def test_log_aggregate(self):
        assert len(self.reader.data) == 5

    def test_service_time_summary(self):
        aggregator = LogAggregate()
        self.assertEqual(aggregator.summary(self.reader.data, 'dyno', ['connection_time']), {'info': Counter({'connection_time': 25})})
        assert len(self.reader.data) == 5

