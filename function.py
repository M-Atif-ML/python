def func(*arg, **kwargs) -> None:
        arg = list(arg)
        print(type(arg))
        for k,w in kwargs.items():
            print(w)

func("odd",1,3.3 , name ="Atif",age = 18,gpa= 2.2)