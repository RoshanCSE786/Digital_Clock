class Father:
    age=42
    def __init__(self,m):
        self.month=m
        self.money=20000
        print("Parent class constructor",self.month,self.money)

    @classmethod
    def show(cls):
        print(cls.age)
    
    @staticmethod
    def stat():
        a=10
        print("Static method is calling",a)

class Child(Father):
    def __init__(self,m):
        self.whmon=m
        print("child class constructor",self.whmon)

    def display():
        print("Child Class")
    
subh=Child('january')
subh.show()
subh.stat()

