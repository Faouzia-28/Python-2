def sum(a,b):
    s=a+b
    if s>=15 and s<=20:
        return 20
    else:
        return s
a=int(input("Enter a value\n"))
b=int(input("Enter a value\n"))
print("The sum is",sum(a,b))

