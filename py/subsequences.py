# lst = [12, 15, 17] 
# for i in lst: 
#     print(i, end="") 




# def convert(list): 
      
#     s = [str(i) for i in list] 
      
#     res = int("".join(s)) 
      
#     return(res) 
  
# list = [1, 2, 3] 
# print(convert(list)) 



# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)


# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = person("mahesh",22)

# print(p1.name)
# print(p1.age)




import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if (x):
  print("match")
else:
  print("not match")