fp = open('input.txt','r')
a = []
b = []
total = []
newtotal =[]
sum = 0
for i in range(3):
    a.append(list(map(int,fp.readline().split(' '))))

fp.readline()
for j in range(3):
    b.append(list(map(int,fp.readline().split(' '))))


for i in range(3):
    print(* a[i])
print()
for i in range(3):
    print(* b[i])

# for i in range(3):
for j in range(3):
    for k in range(3):
        sum = sum + a[j][k] * b[k][j]
    total.append(sum)
    sum = 0
    newtotal.append(total)
print()
for i in range(3):
    print(* newtotal[i])
    
    

        
