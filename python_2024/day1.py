class Day1:
    def __init__(self,r,p=10):
        self.name=r
        self.srn="Sahu"
        self.a1=p
    def Show(self,a,b,c):
        dat=a
        self.mont=b
        self.yr=c
        k=2000
        print('model',self.name)
        # print('Look',dat,self.mont,self.yr,k)

d1=Day1('Roshan')
d1.Show(10,5,2024)
# print(d1.a1)  
# print(d1.srn)  
# # print(d1.dat)   