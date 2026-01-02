C_brack = {"{":"}","(":")","[":"]"}
   
def sol(s):
    stack =  
    for i in s:
    	print(i)
    	if i in C_brack:
        	print(i) 
        	stack.append(i)
        if i in O_brack:
        	if stack[:-1] == O_brack[i]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
print(sol("(){}[]"))

# print(")" == O_brack[")"])