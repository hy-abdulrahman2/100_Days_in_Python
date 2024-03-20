x = int(input("Enter your num: "))

match x:
    case 0:
      print("x is zero")

    case 4:
      print("x is 4")

    case 5:
      print("x is 5")

    case _ if x!=90: #default case
      print(x, "is not 90")

    case _: #default case
      print(x) 