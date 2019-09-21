class University:
 def __init__(self,university_name,dept_name):
 self.__university_name= university_name
 self.__department=Department(dept_name)

 def display_details(self):
 print("University Name: ", self.__university_name)
 self.__department.display()
class Department:
 def __init__(self,dept_name):
 self.__dept_name=dept_name

 def display(self):
 print("Department Name: ", self.__dept_name)

university=University("VTU", "Computer Science")
university.display_details()