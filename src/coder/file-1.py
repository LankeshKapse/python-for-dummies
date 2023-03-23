def print_value(value : any) -> None :
    print(value)
    
if __name__ == '__main__':
    # print("\x1b[2K") # clear screen
    # print("\x1b[H")  # reset control to left
    print_value(1290)
    
    set_1 = {1,2,3,4,5,6,7,8,9}
    frozen_set = frozenset({i for i in range(10)})
    
    dict_1 = { frozen_set:set_1}
    
    print(dict_1)
    
    x= 1
    print(f'int x {x}')
    
    x= 'str value'
    
    print(f'change type {x}')
    
    x = [ 1,2,3]
    y = [ 1,2,3]
    
    z = x
    
    print(x==y)  # check the value of objects
    print(x is y) # check wheathe two object sahre the shame memory instace
    print(x is z)
    