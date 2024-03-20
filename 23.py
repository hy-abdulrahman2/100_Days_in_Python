l = [39,41,63,26,13, 41]
print("Simple list : " , l)

# .append()
l.append(7)
print("append element: ",l)

# .sort()

             # ascending Order 
l.sort() 
print("Ascending order: ",l)

            # decending Order 
l.sort(reverse=True) 
print("Decennding order: ",l)

# .reverse()
l.reverse()
print("reversed list: ", l)

# .index()
print("index() method: ", l.index(26))
# k = l.index(41)
# print(k) 

# .count()
# coun = l.count(41)
# print("count one item in the list: ", coun)
print("count one item in the list: ", l.count(41))


# .copy()
cop = l.copy()
cop[0] = 0
print("cop in  use l.copy(): ", cop)
print("Simple list: ",l)
# cop = l
# cop[0] = 0
# print("cop", cop)
# print(l)

# .insert()
l.insert(0, 9090)
print("list in use  insert(  'index_no' , 'value')  method : ",l)

# .extend()
m = [900, 1000, 1100]
l.extend(m)
print("'l' list in extend 'm' list in the last : ",l)
lm = l + m
print("'l' list in extend 'm' list in the last : ",lm)