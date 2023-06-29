def max_count(m, n, ops):
    length = len(ops)
    if length == 0:
        return m*n
    result = [ops[0][0] , ops[0][1]]
    for i in range(1,length):
        result[0] = min(result[0] , ops[i][0])
        result[1] = min(result[1] , ops[i][1])
        return result[0]*result[1]  

m = 3
n = 3
ops = [[2, 2], [3, 3]]

result = max_count(m, n, ops)
print(result)
