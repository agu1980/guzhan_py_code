import json
from collections import defaultdict, Counter
from pandas import DataFrame, Series
import pandas as pd; import numpy as np

# s = Series(data=[1,3,5,7],index = ['a','b','x','y'])
# tt = s.value_counts()
#
# data = {'state':['Ohino','Ohino','Ohino','Nevada','Nevada'],
#         'year':[2000,2001,2002,2001,2002],
#         'pop':[1.5,1.7,3.6,2.4,2.9]}
#
# df = DataFrame(data)
# df.replace({'Ohino':'test'},inplace=True)

# def get_counts(obj,key):
#     counts = {}
#     for x in obj:
#         if x[str(key)] in counts:
#             counts[x[key]] += 1
#         else:
#             counts[x[key]] = 1
#     return counts
#
#
# def get_counts2(obj,key):
#     counts = defaultdict(int)
#     for x in obj:
#         counts[x[key]] = counts[x[key]] + 1
#     return counts
#
#
# def order(obj, direction, return_number):
#     sorted_list = [(i,j) for j,i in obj.items()]#DSU methond
#     sorted_list.sort()
#     return sorted_list[-10:]


path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
lines = open(path).readlines()
records = [json.loads(line) for line in lines]
#time_zones = [element['tz'] for element in records if 'tz' in element]#DSU methond

frame = DataFrame(records)
frame.replace({'':'Empty'},inplace=True)
frame.fillna('Missing',inplace=True)
#tz_count = frame['tz'][:10].value_counts()
# tz_count = frame['tz'].value_counts()
# tz_count[0:10].plot(kind='barh', rot=0)# draw a bar chart for time_zone
# ie_str = [x for x in frame.a]
# p = list()
# for y in ie_str:
#     p.append(y.split()[0])
# ie_info = Series(p)
ie_str = [x.split()[0] for x in frame.a]

ie_info = Series(ie_str)
sss = ie_info[ie_info!='Missing']
ie_info.drop('Missing',axis=0,inplace=True)
ie_info.replace({'Missing':np.nan},inplace=True)
ie_info.dropna(inplace=True)
test = ie_info.value_counts()
test.plot(kind='barh', rot=0)
pass
# dict_count = get_counts(records,'tz')
# dict_count2 = get_counts2(records,'tz')
# top_count = order(dict_count,'ASC', 10)
# counter_tz = Counter(time_zones)
# ordered_tz = counter_tz.most_common(10)

# for tz in ordered_tz:
#     print '{',tz[0],'=>',tz[1],'}'
