def arrange_coins(n):
    row = 0
    count = 0

    while n >= row + 1:
        count += 1
        row += 1
        n -= row

    return count

n = 5

result = arrange_coins(n)
print(result)
