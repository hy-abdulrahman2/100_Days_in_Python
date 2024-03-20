# loops
#for in 

name = "Abdul"
for i in name:
    print(i)

colors = ["Red", "Green", "Yellow", "Orange", "Brown", "Black", "White", "Blue"]
# for in  & nested loop
for c in colors:
    print(c)
    for b in c:
        print(b)

# stop 
for x in range(9):
    # print(x + 1)
    print(x)
# start, stop 
for x in range(3,9):
    print(x)

# start, stop, step 
for g in range(2, 19, 3):
    print(g)