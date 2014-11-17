#!/usr/bin/env python

import re
from dateutil.parser import parse
from collections import defaultdict, Counter


def to_integer(params):
    try:
        return int(re.sub('[a-zA-z]', '', params))
    except ValueError:
        return 0

def parse_parameter(params):
    try:
        return re.sub('"', '', params.split('=')[1])
    except IndexError:
        return params

class LogReader:
    def __init__(self, filename):
        self.data = list()
        file = open(filename, 'r')
        for row in file.readlines():
            log = row.split()
            self.data += [
                {
                        'date_time' : parse(log[0]),
                        'at' : parse_parameter(log[2]),
                        'method' : parse_parameter(log[3]),
                        'path' : parse_parameter(log[4]),
                        'host' : parse_parameter(log[5]),
                        'forward' : parse_parameter(log[6]),
                        'dyno' : parse_parameter(log[7]),
                        'connection_time' : to_integer(parse_parameter(log[8])),
                        'service_time' : to_integer(parse_parameter(log[9])),
                        'response_status' : to_integer(parse_parameter(log[10])),
                        'byte' : to_integer(parse_parameter(log[11])),
                }
            ]


class LogAggregate:
    def summary(self, dataset, group_by_key, sum_value_keys):
        dic = defaultdict(Counter)
        for item in dataset:
            key = item[group_by_key]
            vals = {k:item[k] for k in sum_value_keys}
            dic[key].update(vals)
        return dic