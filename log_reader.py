#!/usr/bin/env python
import re
from dateutil.parser import parse
from pandas import DataFrame

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
                        'connection_time' : to_integer(parse_parameter(log[8])),
                        'service_time' : to_integer(parse_parameter(log[9])),
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


class LogAggregate:
    def __init__(self, dataset):
        self.dataset = DataFrame(dataset)

    def get_median(self, *arg, **kwarg):
        if kwarg.has_key('group_by'):
            return self.dataset.groupby(kwarg['group_by']).median()[kwarg['key']]
        else:
            return self.dataset.median()[kwarg['key']]

    def get_average(self, *arg, **kwarg):
        if kwarg.has_key('group_by'):
            return self.dataset.groupby(kwarg['group_by']).mean()[kwarg['key']]
        else:
            return self.dataset.mean()[kwarg['key']]

    def get_min(self, *arg, **kwarg):
        if kwarg.has_key('group_by'):
            return self.dataset.groupby(kwarg['group_by']).min()[kwarg['key']]
        else:
            return self.dataset.min()[kwarg['key']]
    
    def get_max(self, *arg, **kwarg):
        if kwarg.has_key('group_by'):
            return self.dataset.groupby(kwarg['group_by']).max()[kwarg['key']]
        else:
            return self.dataset.max()[kwarg['key']]

    def get_count(self, *arg, **kwarg):
        if kwarg.has_key('group_by'):
            return self.dataset.groupby(kwarg['group_by']).count()[kwarg['key']]
        else:
            return self.dataset.count()[kwarg['key']]

class Report:
    def __init__(self, dataset):
        aggreator = LogAggregate(dataset)
        print aggreator.get_median(key='byte', group_by=['endpoint', 'method'])
        print aggreator.get_count(key='byte', group_by=['endpoint', 'method'])



if __name__ == "__main__":
    reader = LogReader('sample.log')
    i = Report(reader.dataset)