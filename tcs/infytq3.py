class Example:
    def __init__(self):
        self.__num=5

    def set_num(self,num):
        self.__num=num

    def get_num(self):
        return self.__num
obj=Example()
obj.set_num(6)
print(obj.get_num())