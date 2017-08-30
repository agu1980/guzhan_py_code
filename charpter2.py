import json
from collections import defaultdict

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
    return map(obj.get,obj.keys().sort())
    # if direction == 'ASC':
    #     for x in obj.iteritems():
    #         y = list(x)
    #         count_pairs.append(y)
    # count_pairs.sort()
    # return count_pairs[-return_number:]


path = 'C:\Users\guzhan\Documents\GitHub\pydata-book\ch02\usagov_bitly_data2012-03-16-1331923249.txt'
lines = open(path).readlines()
records = [json.loads(line) for line in lines]
for rec in records:
    if 'tz' in rec:
        pass
    else:
        records.remove(rec)

dict_count = get_counts(records,'tz')
#dict_count2 = get_counts2(records,'tz')
top_count = order(dict_count,'ASC', 10)
for i in top_count:
    print '{',i,'=>',top_count[i],'}'
