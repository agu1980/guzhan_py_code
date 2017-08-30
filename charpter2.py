import json
from collections import defaultdict, Counter


# obj1= {1:'a'}
# obj2= {2:'b'}
# obj3= {3:'c'}
# obj4= {4:'d'}

obj1= ['a',8]
obj2= ['b',42]
obj3= ['c',3]
obj4= ['d',6]

test = [obj2,obj1,obj4,obj3]
test2 = [(i,j) for i,j in enumerate(test)]
#resutl = test[2][0]

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
    sorted_list = [(i,j) for j,i in obj.items()]
    sorted_list.sort()
    return sorted_list[-10:]


path = '/Users/guzhan/guzhan_py_code/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
lines = open(path).readlines()
records = [json.loads(line) for line in lines]
time_zones = [element['tz'] for element in records if 'tz' in element]
for rec in records:
    if 'tz' in rec:
        pass
    else:
        records.remove(rec)

dict_count = get_counts(records,'tz')
#dict_count2 = get_counts2(records,'tz')
#top_count = order(dict_count,'ASC', 10)
ttt = Counter(time_zones)
ppp = ttt.most_common(10)

for i in ppp:
    print '{',i[0],'=>',i[1],'}'
