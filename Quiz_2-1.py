# Kyle Bautista (AMDG) 11/24/2020

day = input("Insert the letter of your cycle from A-G: ")
day = day.upper()

if day == 'A':
    print("There is class today because it's {0} day." .format(day))
elif day == 'B':
    print("There is no class today because it's {0} day." .format(day))
elif day == 'C':
    print("There is class today because it's {0} day." .format(day))
elif day == 'D':
    print("There is no class today because it's {0} day." .format(day))
elif day == 'E':
    print("There is class today because it's {0} day." .format(day))
elif day == 'F':
    print("There is no class today because it's {0} day." .format(day))
elif day == 'G':
    print("There is no class today because it's {0} day." .format(day))
else:
    print("Error")
