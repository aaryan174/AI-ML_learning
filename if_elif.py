name = input("enter your name: ")
marks = int(input("enter you  marks: "))
if (marks < 0 or marks >100):
    print("enter the valid number 0 to 100")
elif(marks >= 95):
    print("A+\n")
    print(f"{name} is Very Fast learner")
elif(marks >= 85):
    print("A")
    print(f"{name} is Fast learner")
elif(marks >= 75):
    print("B+")
    print(f"{name} is Good learner")
elif(marks >= 65):
    print("B")
    print( f"{name} is Avg learner")
elif(marks >= 50):
    print("C")
    print(f"{name} is Slow learner")
else:
    print("D")
    print(f"{name} is fail also very slow learner")