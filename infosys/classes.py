class Mahesh:
    __static_variable_name=2
    @staticmethod
    def callme():
        return Mahesh.__static_variable_name

m1 = Mahesh("Mahesh")
print(m1.callme())
