def bylength(a):
    return len(a)

my_arr = ["AW","QWE","EW","PPP"]
my_arr.sort(key=bylength)
print(my_arr)