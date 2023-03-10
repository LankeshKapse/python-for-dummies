
class Student:
    
    def __int__(self):
        self.name = "abc"
        self.age = 22.3
        self.grade = "A"
        
    
    def get_grade(self):
        return self.grade
    



s1 = Student()

s1.grade='A'
print(s1.grade)