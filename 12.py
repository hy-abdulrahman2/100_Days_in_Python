names = ("harryshunb")
print(names[0:5]) # including 0 but not 4
print(names[1:5]) # including 1 but not 4
print("\n")
# postive slicing 
print(names[5:10])
print(names[:7]) 
print(names[:]) # this is the same as print(names[0:len(names)])
print("\n\n")

# negative slicing
nam1 = "abdulr"
print(nam1[0:-2]) #including 0 and - len(nam1) - 2
print(nam1[0:len(nam1)-2])

print("\n")

print(nam1[-2:-1])
#start len(nam1) - 2 {3} and end len(nam1) - 1 {4}
print(nam1[len(nam1)-2:len(nam1)-1])


print("Lenth of nam1 ",len(nam1))
print("\n\n")

# find str length 
print("Length of names ",len(names))
print("\n")

# Quick Quiz:
nm = "Harry"
print(''' Quiz Ans: ar, 
___ Quiz real Answer: ''', nm[-4:-2],)