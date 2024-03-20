tup = (2, 4, 5, True, "yellow, 9.3")
print(type(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-1])
print(tup[len(tup)-2])

if 4 in tup:
    print("yoh")
else:
    print("No")

print(tup[:3])