""" This is first line use as muiltline comment"""
import json
from json import JSONEncoder


class Person:
     
    def __init__(self, name: str, age: float, address: str) -> None:
        self.name = name
        self.age = age
        self.address = address  
        
    def __repr__(self) -> str:
        return json.dumps(self, cls=PersonEncoder)


class PersonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

   
class Employee:
    pass


class Business:
    pass


p1 = Person("lucky", 32.1, "pune")
print(p1)
print(p1.__dict__["address"])


# Inner class
class Outer:
    
    def __init__(self, outer_var, inner_var_in) -> None:
        self.var = outer_var
        self.inner_obj = self.Inner(inner_var_in)
     
    def __str__(self) -> str:
        return str(self.__dict__)   
    
    def get_inner(self):
        return self.inner_obj._get_inner()
        
    # Inner class
    class Inner:
        
        def __init__(self, inner_var) -> None:
            self.inner_var = inner_var
            
        def _get_inner(self):
            return self.inner_var
            

outer = Outer('outer', 'inner')

print(outer.get_inner())