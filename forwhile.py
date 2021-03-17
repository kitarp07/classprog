#wap to find Am or Pm from the time given by user

time = int(input("Enter the time:" ))

if time<12:
    print ("AM")
elif time>=12 and time<=21:
    print("PM")
else:
    print("error")