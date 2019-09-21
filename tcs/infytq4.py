class Example:
    def __init__(self):
        self.__num=None

    def set_num(self,num):
        self.__num=num

    def change_num(self):
        self.__num=5
        return self.__num
obj=Example()
obj.set_num(10)
print(obj.change_num())