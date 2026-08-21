#wap to create a simple intelligent agent that decide weather to study or relax based on the available study time
#implement a rule based itelligent agent in python that recommend an action based on temp condition

#program no `1`
hours = int(input("enter the hours (0-24):"))

if (hours < 0 or hours > 24):
    print("enter the valid hours")
elif(hours <=3):
    print("take a short break")
elif(hours <= 5):
    print("take a nap and rest for a while")
elif(hours <=10):
    print("take a long break and get some good sleep ")
else:
    print("this is dengerous for the health")
    
#program no `2`
temprature = int(input("enter the tempreture (1-50):"))

if (temprature < 0 or temprature > 50):
    print("enter the valid temprature")
elif(temprature <=15):
    print("cold")
elif(temprature >=16 and temprature <=25 ):
    print("good weather")
else:
    print("hot weather")