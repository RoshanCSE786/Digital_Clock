class Add:
    def res(self,a,b):
        print(a+b)
class Mul(Add):
    def res(self,x,y):
        super().res(x,y)
        print(x*y)

k=Mul()
k.res(10,20)