# print(list(filter(lambda x:x != 0,[i for i in range(0,10)])))

# from itertools import groupby
# print(*[(int(i),len(list(j)))[::-1]  for i,j in groupby('1222311')])

# for i in range(10): print(i,end="");print("")

# for i in range(10): print(i) if i%2==0 else None

# def callme(i):
#     return i if i%2 ==0 else None
# print(list(filter(callme,[i for i in range(10)])))

# print(filter(lambda x:x!=5,[1,2,3,4,5,6,5,5]))

# ans=list(filter(lambda x:x!=5,[1,2,3,4,5,6,5,5]))
# print("".join(map(str,ans)))

#if you want to join check type of list either int or string otherwise map to str
# print(" ".join(map(str,list(filter(lambda x:str(x)!=5,[1,2,3,4,5,6,5,5])))))

# following ex  works on python 3 only no need to convert array to string
# print(*filter(lambda x:x!=5,[1,2,3,4,5,6,5,5]))

# a=[1,2,3,2,2,2,3,3,3,1,12,3,2]
# print(*list(set(a)))

# from collections import Counter
# z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
# z = [1,2,2,1,2,3,43,2,2,1]
# print(Counter(z))
# dict = Counter(z)
# list = [(k, v) for k, v in dict.items()] 
# print(*list)
# print(*sorted(list,key=lambda x:x[0])[::-1])

# def solve(h, wallPoints, lengths):
#     minus =  list(map(lambda x:x/4 ,lengths))
#     fromthis = wallPoints
#     all_devices = [x - y for x, y in zip(fromthis, minus)]
#     return all_devices
# math.ceil()
# math.floor()
# round()

#textwrap python in older version
# import textwrap
# def wrapthis(string, max_width):
#     return '\n'.join(list(textwrap.wrap(string,width = max_width)))
# print(wrapthis('ASDFDSASDFGFDSA',3))




# letters = ["a", "b", "c"]     
# letters[::-1]  
# for i in range(7):
#     letters = letters[::-1]
#     print(letters)
#regex
# import re
# str = "a bcd efgh ijklmn opqrst uvwxyz"
# x = re.findall("[b-e]", str)
# y = re.findall("[be]", str)
# e = re.findall("[^be]", str)
# z = re.split("\s", str)
# a = re.split("\s", str, 4)
# b = re.sub("\s", "_______", str)
# c = re.search("efgh", str)


# d = re.search(r"\bi\w+", str)
# print(d)
# print(c.span())
# print(d.group())