letter = "Hey how are you. My name is {1} I am from {0}"
name = "Abdul"
country = "Pakistan"


# print(letter.format(name, country))
print(letter.format(country, name))

x = f"Hey how are you. My name is {name} I am from {country}"
print(x)

rupess = 458.3990

money = f"My vulat in {rupess:.2f}"
print(money)


print(f"hy, My age is {3 * 6}")

f_string = f"This is f-string {{name}}, real name user as a f-str brakets {name}"
print(f_string)