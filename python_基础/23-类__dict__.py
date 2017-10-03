import json

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student('tf', 22)
print(s.__dict__)

j = json.dumps(s.__dict__)
print(j)