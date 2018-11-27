def NumberOf1(n):
    # write code here
    count = 0
    for i in range(32):
        count += (n >> i) & 1
    return count


print(NumberOf1(-1))
