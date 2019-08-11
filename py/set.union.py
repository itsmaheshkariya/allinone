if __name__ == '__main__':
    n1 = int(input())
    line1 = set(map(int,input().split()))
    # print(*line1)
    n2 = int(input())
    line2 = set(map(int,input().split()))
    # print(*line2)
    list_line1 = list(line1)
    list_line2 = list(line2)
    for i in list_line1:
        if i not in list_line2:
            list_line2.append(i)
    print(len(list_line2))
# print(len(set(map(int, input().split()))|set(map(int, input().split()))))
