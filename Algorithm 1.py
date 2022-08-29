def func (n):
    for x in range(n):
        if 2**x >= n:
            return 2**x

print(func(5))
