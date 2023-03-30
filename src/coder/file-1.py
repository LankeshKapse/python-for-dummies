def print_value(value: any) -> None:
    print(value)


def supper_decorator(function):
    print(f'supper_decorator')

    def wrapper(arg):

        return function(arg)

    return wrapper


@supper_decorator
def decorator_lower(function):
    print(f'decorator_lower')

    def wrapper(arg1):
        str_1 = ""
        for idx, ch_1 in enumerate(arg1):
            if idx == 0:
                str_1 += str(ord(ch_1))
            else:
                str_1 += "-"+str(ord(ch_1))

        fun = function(str_1)
        return fun.upper()

    return wrapper


def add_fun(**kwarg):
    input1 = kwarg.get('input1')
    input2 = kwarg.get('input2')
    return input1 + input2

def add_fun2(input1, input2):
    return input1 + input2

@decorator_lower
def hello(statement):
    print(f'hello')
    return statement


if __name__ == '__main__':
    # print("\x1b[2K") # clear screen
    # print("\x1b[H")  # reset control to left
    print_value(1290)

    set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    frozen_set = frozenset({i for i in range(10)})

    dict_1 = {frozen_set: set_1}

    print(dict_1)

    x = 1
    print(f'int x {x}')

    x = 'str value'

    print(f'change type {x}')

    x = [1, 2, 3]
    y = [1, 2, 3]

    z = x

    print(x == y)  # check the value of objects
    print(x is y)  # check wheathe two object sahre the shame memory instace
    print(x is z)


    class Person:
        count = 0

        def __init__(self, name: str, age: float) -> None:
            self.name = name
            self.age = age
            Person.count += 1


    p1 = Person('lucky', 32)
    p2 = Person('lucky', 33)
    print(Person.count)

    value = hello('Hello World...!')
    print(f'input ascii -> {value}')
    ascii_chr = ""
    for v in value.split("-"):
        ascii_chr += chr(int(v))
    print(f'output chr -> {ascii_chr}')

    a = [1, 2, 3]
    b = [7, 8, 9]

    list_tup = [(x, y) for x in a for y in b]
    # addition of numbers
    add = [ x+y for x, y in zip(a, sorted(b, reverse=True))]
    print((f'add {add}'))
    print((f'list tup {list_tup}'))

    multi_dim_list = [[i for i in range(1, tmp) ] for tmp in range(2, 10)]
    print((f'multi_dim_list {multi_dim_list}'))

    # flatten the list
    flatten_list = [elem for item in multi_dim_list for elem in item]
    print((f'flatten_list {flatten_list}'))

    #unique values
    print(f'unique set {set(flatten_list)}')

    from collections import Counter

    print(f'Duplicate count {(Counter(flatten_list))}')
    
    
    # dictonary unpacking 
    print(add_fun(**{'input1':10, 'input2':20}))
    print(add_fun2(**{'input1':20, 'input2':20}))
    

