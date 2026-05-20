a = int(input("Enter your first number"))
b = int(input("Enter your second number"))
c = a % b
if c > 0:
    print(a,"is not divisible by", b)
else:
    print(a,"is divisible by", b)