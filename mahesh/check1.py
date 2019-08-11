# letters = ["a", "b", "c"]     
# letters[::-1]  
# for i in range(7):
#     letters = letters[::-1]
#     print(letters)
import re
str = "a bcd efgh ijklmn opqrst uvwxyz"
x = re.findall("[b-e]", str)
y = re.findall("[be]", str)
e = re.findall("[^be]", str)
z = re.split("\s", str)
a = re.split("\s", str, 4)
b = re.sub("\s", "_______", str)
c = re.search("efgh", str)


d = re.search(r"\bi\w+", str)
# print(d)
# print(c.span())
print(d.group())




