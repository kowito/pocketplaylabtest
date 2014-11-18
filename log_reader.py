#!/usr/bin/env python
import re
from dateutil.parser import parse

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
        self.dataset = list()
        file = open(filename, 'r')
        for row in file.readlines():
            log = row.split()
            self.dataset += [
                {
                        'date_time' : parse(log[0]),
                        'at' : parse_parameter(log[2]),
                        'method' : parse_parameter(log[3]),
                        'path' : parse_parameter(log[4]),
                        'host' : parse_parameter(log[5]),
                        'forward' : parse_parameter(log[6]),
                        'dyno' : parse_parameter(log[7]),
                        'connect_time' : to_integer(parse_parameter(log[8])),
                        'service_time' : to_integer(parse_parameter(log[9])),
                        'response_time' : to_integer(parse_parameter(log[8]))+to_integer(parse_parameter(log[9])),
                        'response_status' : to_integer(parse_parameter(log[10])),
                        'byte' : to_integer(parse_parameter(log[11])),
                        'endpoint' : self.get_endpoint(parse_parameter(log[4]))
                }
            ]
    def get_endpoint(self, path):
        endpoint_strings = [
            '/api/users/(\d+)/count_pending_messages',
            '/api/users/(\d+)/get_messages',
            '/api/users/(\d+)/get_friends_progress',
            '/api/users/(\d+)/get_friends_score',
            '/api/users/(\d+)$',
        ]
        endpoint = re.search('|'.join(endpoint_strings), path)
        if endpoint is not None:
            return re.sub('(\d+)', '{users}', path)
