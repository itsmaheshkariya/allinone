if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    def check(x,y,z,n):
        d_arr = []
        for i in range(x+1):
            for j in range(y+1):
                for k in range(z+1):
                    if i + j + k == n:
                        continue
                    else:
                        temp_arr = []
                        temp_arr.append(i)
                        temp_arr.append(j)
                        temp_arr.append(k)
                        d_arr.append(temp_arr)
             
        print(d_arr)
    check(x,y,z,n)





