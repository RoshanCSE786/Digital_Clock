class Mobile:
    # id=1011      #class variable
    def __init__(self,p):
        self.model="realme x"   #  instance variable
        self.price=p
    def show(self):
        # self.po=l               #instance method
        print("model",self.model)   #accessing instance variable 
        print("model",self.price)   #accessing instance variable 
        print("hellp")
    # @classmethod                  #class method
    # def new(cls):
    #     print("finger point",cls.id)  #accessing class variable
redmi=Mobile('by')
redmi.show()
# print(redmi.price)
# poco=Mobile()
# print(poco.model)
# redmi.model='nweew'
# print(redmi.model)
# print(poco.model)




# Mobile.id=5000
# mi=Mobile()
# # print(Mobile.id)
# mi.new()
# Mobile.new()