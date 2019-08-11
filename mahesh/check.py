# one dimentional array
# if __name__ == '__main__':
#     fptr_write = open('ans.txt','w')
#     fptr_read = open('que_single_array.txt','r')
#     a = fptr_read.readline()
#     list_of_list = []
#     for i in range(int(a)):
#         one = fptr_read.readline()
#         one = str(one.strip()).split(' ')
#         one = list(one)
#         # one = list(str(fptr_read.readline().strip()).split(' '))
#         list_of_list.append(one)
#     a = str(list_of_list)
#     fptr_write.write(a)
#     fptr_write.close()
# two dimentional array

if __name__ == '__main__':
    def doit(n): 
        n = n.replace('\n','')
        return n
    fptr = open('que_multi_array.txt','r')
    allfile = list(fptr.readlines())
    result = list(map(doit, allfile))
    while '' in result:
        result.remove('')
    # for i in range(int(result[0])):
    #     print(i)
    print(result)