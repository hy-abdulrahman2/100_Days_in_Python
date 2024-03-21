# recursion 
# 1 function ky inder os funtion ko he call kr de na 
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(0) = 1

# factorial(n) = n * factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
# print(factorial(6)) 


# Quiz 
# fibonacci series number 
# f0 = 0
# f1 = 1
# f2 = f1 + f0
# f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    if(n<0):
        return "Invalid input"
    elif(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return fibonacci (n-1) + fibonacci(n-2) 
    
print(fibonacci(9))