

if __name__ == '__main__':
    # create dictonary empty
    dct = {}
    print(f'empty dict {dct}')
    
    # create dictonary form collectionsexit()
    lst = [(i,i) for i in range(1,10)]
    
    print(f'dict from lst {dict(lst)}')
    
    # create dict from two collection
    values = [i for i in range(1,10)]
    keys = list("char will be keys".replace(" ",""))
    
    dct_from_two = dict([(i,j) for i,j in zip(keys,values)])
    print(f'dct_from_two {dct_from_two}')
    
    # create a dict from collection of keys
    dct_from_keys = dict.fromkeys(keys,6)
    print(f'dct_from_keys {dct_from_keys}')
    
    # values return view
    view_list = dct_from_keys.values()
    print(f'view_list {view_list}')
    view_list = [7 for i in range(0,len(view_list))]
    print(f'view_list {view_list}')
    print(f'dct_from_keys {dct_from_keys}')
    
    dct_item = dct_from_keys.items()
    print(f'return list of tuple {dct_item}')
    
    c_value = dct_from_keys.get('c',None)
    print(f'c_value {c_value}')
    c_value=7
    print(f'original dict {dct_item}')
    
    dct_from_keys['c'] = 8
    print(f'c_value {c_value}')
    print(f'original dict {dct_item}')
    
    # crete dictonary
    dct_2 = {
        'key1' : 'value1',
        'key2' : 'value2',
        'key3' : 'value3',
        'key4' : 'value4',
        'key5' : 'value5',
    }
    
    # remove item from dict
    print(dct_2)
    
    # pop item pop last item in dict and return (key,value) tuple
    value_5 = dct_2.popitem()
    print(f'value_5 -> {value_5}')
    print(f'dict_2 -> {dct_2}')
    
    # filter keys based on value
    filter_keys = [k for k,v in dct_2.items() if v == 'value3']
    print(f'filter_keys {filter_keys}')
    
    # filter value based on keys
    keys = ['key1','key2']
    filter_values = [v for k,v in dct_2.items() if k in keys]
    print(f'filter_values {filter_values}')