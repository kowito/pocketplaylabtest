from log_reader import LogAggregate, LogReader
from dateutil.parser import parse
import unittest

from collections import defaultdict, Counter


class TestLogAggregate(unittest.TestCase):
    @classmethod    
    def setUp(self):
        self.reader = LogReader('test_log.log')

    def test_log_is_list_instance(self):
        self.assertIsInstance(self.reader.dataset, list)
    
    def test_log_value_is_dict_instance(self):
        self.assertIsInstance(self.reader.dataset[0], dict)

    def test_log_aggregate(self):
        assert len(self.reader.dataset) == 5

    def test_median(self):
        assert len(self.reader.dataset) == 5
        aggregator = LogAggregate(self.reader.dataset)

        assert aggregator.get_median_from_key('byte') == 52
        assert aggregator.get_median_from_key('connection_time') == 2
        assert aggregator.get_median_from_key('service_time') == 42
        




