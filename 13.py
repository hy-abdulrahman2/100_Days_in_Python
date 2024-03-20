hel = "Hy! How are You"
#The strings are unmutable 
print(hel)
# convert into upper Case
print(hel.upper())

# convert into Lower case 
print(hel.lower())

# rstrip method  extra character use only(in the last) 
a = "Hel lllehfdjfjdllldfkj snfkjnfkdlllldsjf dkjllllllllllll"
print(a.rstrip("l"))

#replace method use
print(a.replace("l", "O"))

#split method use
print(a.split(" "))

print("\n")
#capitalize method use
heading = '''introduction 100 dAy code.'''

print(heading.capitalize())

 #center method use
w = "Welcome to console!!!"
print(len(w))
print(len(w.center(70)))
print(w.center(50))  
print(len(w))

#count() method user for letter counting
print("This is l count : ",a.count("l"))

#endswith() method use 
print(w.endswith("!!!"))

wel = "Welcome"
print(wel.endswith("om", 1, 6))

#find() method use
he = "He's name is Dan. He is an honest man."
print(he.find("is"))
print(he.find("iss"))

#index() method use
print(he.index("is"))
# print(he.index("isfd"))

#isalnum() method use
ab = "WelcomeToTheConsole00"
print(ab.isalnum())

#isalpha() method use
xy = "Welcome"
print(xy.isalpha())

#islower() method use
print(xy.islower())
print(xy.isupper())

#isprintable() method use
aa = "  We wish you a Merry Christmas"
print(aa.isprintable())

#isspace() method use
spp = "   "
print(spp.isspace())

#istitle() method use
print(he.istitle())

#startswith() method use
print(he.startswith("He"))
print(len(he))
print(xy.startswith("co", 3, 6))
# print(he.startswith("is", 7, 12))

#swapcase() method use
print(aa.swapcase())

#title() method use
print(he.title())