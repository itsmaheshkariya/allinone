# # str=input()
# from itertools import combinations
# a= list(combinations(range(3),3))
# print(a)


from itertools import permutations
arr = []
for item in permutations(range(3),3):
    arr.append(list(item))

print(arr)

# def even(a):
#     a=list(a)
#     new_arr = []
#     for i in a:
#         if ord(i)>47 and ord(i)<58:
#             new_arr.append(i)
#         new_arr=list(dict.fromkeys(new_arr))
#     new_arr.sort(reverse=True)
    # new_arr[]
    #print(new_arr)
    # insert()

       


# even("shu@124s1")
