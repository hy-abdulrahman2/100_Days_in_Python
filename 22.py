marks = [3,4,2,"hello", True,8, 5, 6.2]
print(marks)
print(type(marks))

# postive indexing 
print(marks[0])
print(marks[4])


# negative indexing 
print(marks[-2]) 
print(marks[len(marks)- 2]) 
print(marks[6-2]) 

# list searching 
if "hello" in marks:
    print("Yes") 
else:
    print("No")

print(marks[1:])
# print(marks[1:4])

# jumping 
m = [3,2,1,4]
print(m[0:4])
print(m[0:4:2])


# list comprehension 
p = [1,2,3]
lis = [x+x for x in range(10)]
print(lis)




# searching in string 
# str = "hello"
# if "o" in str:
#     print("Yes") 
# else:
#     print("No")