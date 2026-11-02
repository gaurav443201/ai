# Simple Reflex Agent - Vacuum Cleaner
A = "Dirty"
B = "Dirty"

current_room = "A"

while A == "Dirty" or B == "Dirty":

    print("Current Room:", current_room)

    if current_room == "A":
        if A == "Dirty":
            print("Room A is Dirty. Cleaning...")
            A = "Clean"
        else:
            print("Room A is Clean. Moving to Room B.")
            current_room = "B"

    else:
        if B == "Dirty":
            print("Room B is Dirty. Cleaning...")
            B = "Clean"
        else:
            print("Room B is Clean. Moving to Room A.")
            current_room = "A"

print("Both Rooms are Clean!")
print("Final Status:")
print("Room A:", A)
print("Room B:", B)

