# print(r'c:\Desktop\newdir')
# print('mahesh\'s \"macbook\"')
if __name__=='__main__':
    fptr=open('inputs/6_8_19_1.txt','r')
    arr=[]
    while True:
        l=fptr.readline()
        if not l:
            break
        else:
            if list(l.split())==[]:
                continue
            else:
                arr.append(list(l.split()))
    for i in arr:
        print(i) 
    #print(arr)
    fptr.close()
    



                
