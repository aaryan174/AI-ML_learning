def umbrella_agent(weather):
     if(weather == "Rainy" or weather == "Cloudy"):
         print("carry an umbrella")
     else:
        print("dont carry an umbrella")
        
weather_condition = ["Summer", "Winter", "Rainy", "Cloudy"]

print("Select  the weather Conditions:")
for i in range(len(weather_condition)):
    print(i+1, ".", weather_condition[i])
    
choice = int(input("Enter the choice (1-4):"))

if 1<= choice <= len(weather_condition):
    weather = weather_condition[choice-1]
    decision = umbrella_agent(weather)
    
    print("Weather:", weather)
    print("Agent Decision:", decision)
else:
    print("Invalid choice")
    
