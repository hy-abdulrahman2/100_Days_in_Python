fruits = ("Apple", "Banana", "Melon", "mango")
print(fruits)

# convert tuple to list 
temp = list(fruits)

# 1 item apend in list 
temp.append("Graps")

# apend item on the index[1]
temp[2] = "Pineapple"

# convert list to tuple
fruits = tuple(temp)

# print tuple 
print(fruits)


# |||||||||||||||||||||||||||||||||||


vegetables = ("Onion", "Photatos", "Tomatos", "Gobi")

vegAndFruirts = fruits + vegetables
print(vegAndFruirts)

# |||||||||||||||||||||||||||||||||

num = (1,2,3,4,5,6,72,3,52,2,3,7,8,2,2)
numCount = num.count(2)
print(numCount)

# |||||||||||||||||||||||||||||||

numInd = num.index(3, 4, 8)
print("Index of 3 in num tuple : ", numInd)