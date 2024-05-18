class Student:
    def __init__(self,a,r):
        self.name=a
        self.roll=r

    def stu_show(self):
        print("Name: ",self.name)
        print("Roll: ",self.roll)

class User:
    @staticmethod
    def show(s):
        print(s.name,s.roll)
        # print(s.roll)
st=Student("Roshan",101)
User.show(st)
 