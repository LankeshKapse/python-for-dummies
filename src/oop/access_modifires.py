
class Student:
    
    name = ''
    _age = 0.0
    __grade = ''
    
    def get__grade(self):
        return self.__grade
    



s1 = Student()

s1.__grade='A'
print(s1.__grade)