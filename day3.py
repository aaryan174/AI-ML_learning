# name = "hello"
# #in is membership operator
# for var in name:
#     print(var)

#use of (in) in conditional statement

# string = "hello"

# if 'a' in string:
#     print("o exists!!!")

# word = "Artificial Intelligent"

# ans = 0

# for ch in word:
#     if(ch == 'i'):
#         ans += 1
# print("count of i is:", ans)
n = int(input("enter the number"))
def factorial():
    fac = 1
    for i in range(1, n+1):
        fac = fac * i
    print(fac)

factorial()