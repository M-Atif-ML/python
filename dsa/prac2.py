n =1

def fun(n):
    if n == 2:
        return n
    print(n)
    n+=1
    return fun(n)

print(fun(n))

# print(n)
