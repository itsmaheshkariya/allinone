# lst = [12, 15, 17] 
# for i in lst: 
#     print(i, end="") 




def convert(list): 
      
    s = [str(i) for i in list] 
      
    res = int("".join(s)) 
      
    return(res) 
  
list = [1, 2, 3] 
print(convert(list)) 