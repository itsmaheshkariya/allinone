import os
if __name__ == '__main__':
    ftpr = open(os.environ['OUTPUT_PATH'],'w')
    a = input().split()
    b = input().split()
    # print(list(a))
    # print(list(b))
    multi = [[]]
    result = ""
    for i in range(len(a)):
        for j in range(len(b)):
            temp = []
            temp.append(int(a[i]))
            temp.append(int(b[j]))
            multi.append(tuple(temp))
            
            # result += str("("+a[i].strip()+","+b[j].strip()+")")
    multi.pop(0)
    ftpr.write(' '.join(map(str, multi)))
    ftpr.write('\n')
    ftpr.close()
    
    # multi.pop(0)
    # print(tuple(multi))
    

