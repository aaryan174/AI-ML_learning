    print("select the weather condition:")
    print("1. sunny")
    print("2. Rainy")
    print("3. Winter")
    print("4. Cloudy")

    choice = int(input("enter your choice (1-4)"))

    if( choice == 1):
        weather = "sunny"
    elif choice == 2:
        weather = "Rainy"
    elif choice == 3:
        weather = "Winter"
    elif choice == 4:
        weather = "Cloudy"
    else:
        print("invalid choice")
        

    if weather == "Rainy":
        print("Carry the Umbrella")
    else:
        print("Dont carry the Umbrella")
