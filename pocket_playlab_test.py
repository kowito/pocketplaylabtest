#!/usr/bin/env python
import operator
from log_reader import LogReader
from log_aggregate import LogAggregate

class Report:
    def __init__(self, dataset):
        aggreator = LogAggregate(dataset)
        output_file = open("output.txt", "w")

        output_file.write('%s The number of times the URL was called. %s\n' % ('='*20, '='*20))
        output_file.write(aggreator.get_count(key='dyno', group_by=['endpoint', 'method']).__str__())

        output_file.write('\n\n%s The average of the response time %s\n' % ('='*20, '='*20))
        output_file.write(aggreator.get_average(key='response_time', group_by=['endpoint', 'method']).__str__())

        output_file.write('\n\n%s The median of the response time %s\n' % ('='*20, '='*20))
        output_file.write(aggreator.get_median(key='response_time', group_by=['endpoint', 'method']).__str__())

        output_file.write('\n\n%s The "dyno" that responded the most. %s\n' % ('='*20, '='*20))
        dyno = dict(aggreator.get_count(key='at', group_by=['dyno']))
        output_file.write( max(dyno.iteritems(), key=operator.itemgetter(1))[0])

        output_file.close()

if __name__ == "__main__":
    reader = LogReader('sample.log')
    Report(reader.dataset)