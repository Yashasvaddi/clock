import time

timestamp=time.strftime("%H:%M:%S")
if int(time.strftime("%H"))>=0 and int(time.strftime("%H"))<=12 and time.strftime("%p")=="AM":
    print("Goodmorning Sir!!")
elif int(time.strftime("%H"))>12 and int(time.strftime("%H"))<=4 and time.strftime("%p")=="PM":
    print("Goodafternoon Sir!!")
elif int(time.strftime("%H"))>4 and int(time.strftime("%H"))<9 and time.strftime("%p")=="PM":
    print("Good Evening Sir")
elif int(time.strftime("%H"))>=9 and int(time.strftime("%H"))<12 and time.strftime("%p")=="PM":
    print("Goodnight Sir")
