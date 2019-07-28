if __name__ == '__main__':
    listy = []
    store = []
    N = int(input())
    # def Reverse(lst): 
    #     new_lst = lst[::-1] 
    #     return new_lst
    for i in range(N):
        store.append(input().split(" "))
    for j in store:
        if j[0] == "insert":
            listy.insert(int(j[1]),int(j[2]))
        elif j[0] == "remove":
            listy.remove(int(j[1]))
        elif j[0] == "print":
            print(listy)
        elif j[0] == "append":
            listy.append(int(j[1]))
        elif j[0] == "sort":
            listy.sort()
        elif j[0] == "pop":
            listy.pop()
        elif j[0] == "reverse":
            # listy.sort(reverse=True)
            # listy = reversed(listy)
            listy = listy[::-1]



