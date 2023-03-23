
class MyClass:
    def fun(self):
        print('fun()')
        
        

def monkey_fun(self):
    print('monkey_fun()')
    
#  You can repce exsting functinality of an method
# It can used in testing for creating stubs

MyClass.fun = monkey_fun

obj = MyClass()

obj.fun()