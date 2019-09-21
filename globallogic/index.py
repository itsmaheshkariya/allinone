# def callme(a,n):
#     temp = []
#     for i in range(n):
#         for j in range(len(list(a[i:n]))):
#             temp.append(a[j:n-i])
#     print(*sorted(temp),sep = "\n")


# a="abcd"
# callme(a,len(a))

# def callme(a,n):
#     temp = []
#     for i in range(n):
#         for j in range(i+1,n+1):
#             temp.append(a[i:j])
#     temp.sort(key=len)
#     print(*temp,sep="\n")
# a="abcd"
# callme(a,len(a))

# a = "mahesh" 
# print(a.find("ahe"))
# def passhere(str,substr):
#     if str.find(substr) == -1:
#         print("NO")
#     else:
#         print("YES")

# str = "Mahesh Dipak Kariya"
# substr = "Kariya"
# passhere(str,substr)



# def callme(str,sub_str):
#     count = str.find(sub_str)
#     if count > 0:
#         print(count) 
#     else:
#         print(count)

    # if sub_str in str:
    #     print("OK")
    # else:
    #     print("NOT OK")

# str = "Mahesh"
# sub_str = "Mah"
# callme(str,sub_str)

# s = "abababab"
# print({'ab':s.count("ab") for i in s}) 


# def isSubSequence(str1,str2,ls1,ls2): 
#     j = 0    
#     i = 0    
#     while j<ls1 and i<ls2: 
#         if str1[j] == str2[i]:     
#             j = j+1    
#         i = i + 1
#     return j==ls1
# str1 = "gksrek"
# str2 = "geeksforgeeks"

# ls1 = len(str1) 
# ls2 = len(str2) 

# print("Yes" if isSubSequence(str1,str2,ls1,ls2) else "No")


# def longest_common_subsequence(str1,str2,len1,len2):
#     m =0
#     n=0
#     count=0
#     while m<len1 and n<len2:
#         if str1[m] == str2[n]:
#             count+=1
#         else:
#             if m == len1:
#                 n+=1
#             else:
#                 m+=1
            
#     print(count)

# str1 = "efghijk"
# str2 = "abcdefg"
# longest_common_subsequence(str1,str2,len(str1),len(str2))


def frequency(fre, s, n):  
    for i in range(0, n):  
        string = s[i]  
        for j in range(0, len(string)):  
            fre[i][ord(string[j]) - ord('a')] += 1    

def LongestSequence(fre, n):    
    for i in range(MAX_CHAR-1, -1, -1):  
        mi = fre[0][i]  
        for j in range(1, n):  
            mi = min(fre[j][i], mi)           
        while mi:  
            print(chr(ord('a') + i), end = "") 
            mi -= 1

if __name__ == "__main__": 
    s = ["loo", "lol", "olive"]  
    n = len(s) 
    MAX_CHAR = 26
    fre = [[0 for i in range(26)] for j in range(n)]    
    frequency(fre, s, n)  
    LongestSequence(fre, n)

