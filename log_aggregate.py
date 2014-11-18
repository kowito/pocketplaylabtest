#!/usr/bin/env python
from pandas import DataFrame
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
