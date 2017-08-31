import json
from collections import defaultdict, Counter
from pandas import DataFrame, Series
import pandas as pd; import numpy as np



def get_counts(obj,key):
    counts = {}
    for x in obj:
        if x[str(key)] in counts:
            counts[x[key]] += 1
        else:
            counts[x[key]] = 1
    return counts


def get_counts2(obj,key):
    counts = defaultdict(int)
    for x in obj:
        counts[x[key]] = counts[x[key]] + 1
    return counts


def order(obj, direction, return_number):
    sorted_list = [(i,j) for j,i in obj.items()]#DSU methond
    sorted_list.sort()
    return sorted_list[-10:]


path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
lines = open(path).readlines()
records = [json.loads(line) for line in lines]
time_zones = [element['tz'] for element in records if 'tz' in element]#DSU methond
for rec in records:
    if 'tz' in rec:
        pass
    else:
        records.remove(rec)

frame = DataFrame(lines)
tz_count = frame['tz'][:10].value_counts()
#clean_tz = frame['tz'].fillna('missing')
#clean_tz[clean_tz == ''] = 'Unknow'
tz_counts = tz_count.value_countes()
tz_counts.plot(kind='barh', rot=0)

#dict_count = get_counts(records,'tz')
#dict_count2 = get_counts2(records,'tz')
#top_count = order(dict_count,'ASC', 10)
counter_tz = Counter(time_zones)
ordered_tz = counter_tz.most_common(10)

for tz in ordered_tz:
    print '{',tz[0],'=>',tz[1],'}'
