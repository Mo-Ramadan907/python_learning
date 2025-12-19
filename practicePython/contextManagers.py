from contextlib import contextmanager
from abc import ABC,abstractmethod

@contextmanager
def open_file(file):
    f = open(file,"r+")
    yield f
    f.close()

class animal(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def make_sound(self):
        pass
class dog(animal):
    def __init__(self):
        super().__init__()
class Open_File:
    def __init__(self,fileName,mode):
        self.fileName = fileName
        self.mode = mode
    def __enter__(self):
        self.file = open(self.fileName,self.mode)
        return self.file
    def __exit__(self,exc_type, exc_value, traceback):
        self.file.close()

# with Open_File("/home/mo/Projects/study_program/practicePython/temp.txt","r+") as f:
#     for i in f.readlines():
#         print(i)

# with open_file("/home/mo/Projects/study_program/practicePython/temp.txt") as f:
#     print(f.readlines())