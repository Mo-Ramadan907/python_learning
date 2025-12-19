class Student:
    _class_year = 2024

    def __init__(self,name,age):
        self.__name = name
        self.age = age


std1 = Student("ahmed",10)
std1.__name = "mohamed"
print(std1.__name)