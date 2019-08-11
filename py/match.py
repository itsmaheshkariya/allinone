def reverse(a):
    temp = a
    a = int(a)
    rev = 0
    while a!=0:
        r = a % 10
        rev = rev * 10 + r
        a = a//10
    return rev

def check(a):
    total = 0
    total = int(a) + int(reverse(a))
    if total == reverse(total):
        print(total)
    else:
        check(total)




        
    


a = input()
check(a)