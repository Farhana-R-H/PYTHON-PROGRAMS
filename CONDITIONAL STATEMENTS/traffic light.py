#traffic light
a=str(input("colour:"))
#red,green and yellow
if a=="red" or a=="RED":
    print("STOP")
elif a=="yellow" or a=="YELLOW":
    print("GET READY")
elif a=="green" or a=="GREEN":
    print("GO") 
else:
    print("invalid signal")           