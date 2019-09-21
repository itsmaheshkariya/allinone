test_list = [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]] 
print (str(test_list)) 
res = list(set.intersection(*map(set, test_list))) 
print (str(res)) 