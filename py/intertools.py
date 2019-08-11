import os
from itertools import permutations

if __name__=='__main__':
    def remove_last_line_from_string(s):
        return s[:s.rfind('\n')]
    result=""
    fptr=open(os.environ['OUTPUT_PATH'],'w')
    s=input().split()
    a=s[0]
    b=int(s[1])
    ok = list(permutations(a,b))
    ok.sort()
    count = 0 
    for i in ok:
        count += 1
        if count != 1:
            print("\n"+str(i[0]+i[1]), end="")
        else:
            print(str(i[0]+i[1]), end="")
