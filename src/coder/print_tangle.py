import time
r = 10
for i in range(r):
    if r //2 >= i:
        print(' '*(r-i-1)+'*'*(2*i+1))
    else:
        print(' '*(r-i-1)+'*'*(2*i+1))
        pass
    

lst = [i for i in range(10000000)]
start_time = time.time()
lst_rev = lst[::-1]
lst_time = (time.time() - start_time)
print("--- %s seconds ---" % (lst_time))
# print(lst_rev)
tup = tuple(lst)
start_time = time.time()
tup_rev = tup[::-1]
tup_time = (time.time() - start_time)
print("--- %s seconds ---" % tup_time)
print(type(tup_time))
print(tup_time < lst_time)
print('not indent')

import array as arr

arra1= arr.array('i',[1,2,3,4,5,6,7,8,9])
print(f'arrays {arra1}')
arra1.reverse()
print(f'arrays  reverse {arra1}')
print(f'arrays  buffer info  {arra1.buffer_info()}')
print(f'arrays  byte swap  {arra1.byteswap()}')
print(f'arrays  conunt number of 7  {arra1.count(7)}')

# Append to array

#iterator

class Iter:
    
    def __init__(self,limit) -> None:
        self.limit=limit
    
    def __iter__(self):
        self.x = 0
        return self
    
    def __next__(self):
        x = self.x
        
        if x >= self.limit:
            raise StopIteration
        
        self.x = x + 1
        return x
    
    
# Calling custom iter
print('Calling custom iter')
for i in Iter(5):
    print(i)
    

# picking and unpicling
import pickle
with open('pickel.txt','wb') as file:
    str_data = pickle.dumps(Iter(5))
    
with open('pickel.txt','rb') as file:
    iter = pickle.loads(str_data)
print('After unpickle the object')
for i in iter:
    print(i)