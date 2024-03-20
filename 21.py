# def average(a, b):
#     print("The average: ", (a+b)/2)
# average(3, 4)

# default & keyword arguments 
def average(a=3, b=4):
    print("The average: ", (a+b)/2)
average()#default arguments
average(5) #value of b is default
average(b=2) #value of a is default
average(3, 8) #assign a, b

# keyword arguments
average(b=4, a=9) #change argument order no problem 


#Required argument
def sum(a, b=4):
    print(a + b)
sum(3)
sum(b=5, a= 9)

# variable length argument 
def sumAv(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("SumAv : ", sum / len(numbers))

sumAv(3,5)
sumAv(4,2,8,4,1,2)
sumAv(2)


def names(**name):
    print("hello", name["fname"], name["lname"], )

names(fname= "Abdul", lname="rehman")