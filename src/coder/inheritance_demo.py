
class A:
    def fun(self):
        print("A")
        
class B:
    def fun(self):
        print("B")
        
class C:
    def fun(self):
        print("C")
        

class D(A,B,C):
    pass

d = D()
d.fun()