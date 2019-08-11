if __name__ == '__main__':
    n = int(input())
    redudent_list = []
    for _ in range(n):
        store = input()
        if store not in redudent_list:
            redudent_list.append(str(store))
    print(len(list(redudent_list)))


