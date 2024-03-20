import time

t = time.strftime('%H:%M:%S')
hours = int(time.strftime('%H'))


if(hours >= 0 and hours < 12):
    print("Good Morning Sir!")
elif(hours >= 12 and hours < 17):
    print("Good Afternoon Sir!")
elif(hours >= 17 and hours < 0):
    print("Good Night Sir!")
else:
    print("Good Night Sir!")