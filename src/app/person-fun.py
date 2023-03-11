from app.main import Person


s1 = Person()
# s1.name = "abc"
# s1.age = "10"

print(f"student name {s1.name}")
print(f"student age {s1.age}")
print(f"student grade {s1.grade}")
print(f"student init method {s1.__dict__}")

lst = [[i*i for i in range(1,10)]]
tup = (1,2,3,4,5,6,7,8,9,0,[i*5 for i in range(1,10)])
print(lst[0:5:2])
print(f"tup slic {tup[1:-1:2]}")