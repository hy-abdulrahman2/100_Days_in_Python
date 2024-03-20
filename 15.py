# https://docs.python.org/3/library/time.html
# time.strftime(format[, t])
# t = time.strftime("%a %b %Y %H:%M:%S %I", time.localtime())
# print(t)

import time
from playsound import playsound
 
# playsound('./audio/gm.mp3')
# print('playing sound using  playsound')

l_time = time.strftime("%I:%M")

ampmHours = time.strftime("%H")
hours = int(ampmHours)

mintStr = time.strftime("%H")
mint = int(mintStr)


# morning 
if(hours >= 4 and hours <11):
    if(mint == 30):
        print("Oh ho Good Morning :) \t |> ", l_time, " <|")
    else:
        print("Good Morning :(\t |> ", l_time, " <|")
        playsound("./audio/gm.mp3")

# afternoon 
        
elif(hours >= 12 and hours < 16):
    if(mint == 30):
        print("Oh ho Good Afternoon :)\t |> ", l_time, " <|")
    else:
        print("Good Afternoon :(\t |> ", l_time, " <|")
        playsound("./audio/gm.mp3")

# evening 
        
elif(hours >= 17 and hours <= 19):
    if(mint <= 30):
        print("Oh ho Good Evening :)\t |> ", l_time, " <|")
    else:
        print("Good Evening :(\t |> ", l_time, " <|")
        playsound("./audio/gm.mp3")

# wrong time zone 
else:
    print("Sorry! \n You are Live in Space... :)")

    
print(l_time)

