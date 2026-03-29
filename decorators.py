def decorator(func):
    def wrapper(*args,**kwargs):
        print("before main function")
        temp = func(*args,**kwargs)
        print("AFter main function")
        return temp
    return wrapper

@decorator
def mainfunction(a,b):
    print("main functino")
    return a+b
print(mainfunction(2,3))