from collections import Counter

colors = ['blue', 'white', 'red' , 'blck', 'blue', 'white', 'red', 'red']

cn = Counter(colors)
print(f'counter {cn}')
# finding most common element in list 
print(f'most common {cn.most_common()[0]}')

# Finding most comon element in list 
# Non python way
common_map = {}
for elem in colors:
    value = common_map.get(elem,None)
    if value is None:
        common_map.setdefault(elem,1)
    else:
        common_map[elem] = value+1

# sort dict via value
sorted_dic=sorted(common_map.items(), key= lambda x : x[1], reverse=True)
print(f'common_map {sorted_dic[0]}')