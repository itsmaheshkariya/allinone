if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = 0
    count = 0
    for i in student_marks:
        if i == query_name:
            for j in student_marks[i]:
                avg += j 
                count +=1
    avg /= count
    print("%0.2f" % avg)
    # print(name)

