class Mahesh:
    def __init__(self,name,age,gender,dob,test):
        self.test = test
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__dob = dob
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_gender(self):
        return self.__gender
    def get_dob(self):
        return self.__dob

    def set_name(self,name):
        self.__name = name

mahesh=Mahesh("Mahesh Kariya",24,"Male","29-10-1994","test")
print(mahesh.get_name())
mahesh.set_name("Mahesh Dipak Kariya")
print(mahesh.get_name())
print(mahesh.get_age())
print(mahesh.get_gender())
print(mahesh.get_dob())
print(mahesh.test)


