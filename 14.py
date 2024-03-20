# oprators
# Assignment Operators 
# =, +=, -+, *=
x = 5
print(x)

x += 4
print(x)

x -= 3
print(x)

x *= 2
print(x)


# relational operators 
# <, > , <=, >=, ==, != 

print(4<3)
print(4>3)

print(4<=3)
print(4>=3)

print(4!=3)
print(4==3)


# if, else  contion
y = 45
z = 24
if(y > z):
  print("y is greater than z")
else:
  print("y is less than z")

#   if, elif, else 
age = int(input("Enter your age: "))
if(age <= 0):
  print("Warn! \tYou are No Human")
elif(age >= 18):
  print("Cong...! \tYou are valid for Driving")
else:
  print("Sorry! \tYour age is Less than to 18")



# condition nesting 
age = int(input("Enter your age: "))
if(age <= 0):
  print("Warn! \tYou are No Human")
elif(age >= 18):
  licn = input("Your linc, \t YES/NO? \t")
  if(licn == "YES"):
    print("Congr...! \n You are valid for Drive Car")
  else:
    print("Sorry! \n Please create a license")
else:
  print("Sorry! \tYour age is Less than to 18")