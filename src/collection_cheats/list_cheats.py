from itertools import (chain)
import functools

def main():
    print(f"main function called....! from {__name__}")
    
    # append into list
    lst1 = [i for i in range(1,5)]
    print(f"list1 {lst1}")
    lst1.append(5)
    print(f"list1 after append {lst1}")
    
    lst1.extend([i for i in range(10,5,-1)])
    print(f"list1 after extend {lst1}")
    
    # sort an list inplace
    lst1.sort()
    print(f"sort an list {lst1}")
    
    # Reverse an list inplace
    lst1.reverse()
    print(f"reverse an list {lst1}")
    
    # sort a list and return new 
    sorted_list = sorted(lst1)
    print(f"sorted_list  {sorted_list}")
    
    # reverse a list and return itr 
    reversed_list = reversed(sorted_list)
    print("reversed list [" , end ="")
    for el in reversed_list:
        print(f"{el}", end = ',')
        
    print("]" , end ="\n")
    
    # sum of elem
    print(f"sum of element {sum(lst1)}")
    
    # sum of two list elemet wise using unpack
    element_sum_list = [ i+j for i,j in zip(sorted_list,lst1)]
    print(f"element wise addtion of two list {element_sum_list}")
    
    # another way to do so using tuple
    element_sum_list2 = [ sum(pair) for pair in zip(sorted_list,lst1)]
    print(f"element wise addtion of two list2 {element_sum_list2}")
    
    list_tup = [(i,j) for i,j in enumerate(range(1,10))]
    print(f"tuple list {list_tup}")
    
    # sorted using lambda 
    sorted_tup = sorted(list_tup, key= lambda el : el[1], reverse=True)
    print(f"sorted decending tuple list by second value  {sorted_tup}")
    
    # flattern the list
    # non python way
    # nested_list =[]
    # for i in range(1,5):
    #     inner_list= []
    #     for j in range(i):
    #         inner_list.append(j)
    #     nested_list.append(inner_list)
    
    # paython way
    nested_list = [ [i,j] for i in range(1,5) for j in range(i) ]
    
    print(f"nested list {nested_list}")
    
    # flatten the list
    flatten_lst = list(chain.from_iterable(nested_list))
    print(f"flatten list {flatten_lst}")
    
    # reduce the list using function tolls
    reduced = functools.reduce(lambda input, out : input + out, flatten_lst)
    print(f"reduced value {reduced}")
    
    # list of char
    list_char = list("Hello world..!")
    print(f"list of char {list_char}")
    
    print(f"count of word l in hello world..! {list_char.count('l')}")
    
    # pop exeletory form hello wolrd
    char = list_char.pop()
    print(f"pop char {char}")
    print(f"rest of list  {list_char}")

if __name__ == '__main__':
    main()