def square_root(num):
    return (num)**0.5
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def exponential(ba,ex):
    return ba**ex

while True:
    print("\nChoose an operation")
    print("1. Square root")
    print("2. Greatest common divisor")
    print("3. Exponential")
    print("4. Exit")
    ch=int(input("Enter your choice (1,2,3 or 4 to exit): "))
    if ch==1:
        num=float(input("Enter the number to find its square root: "))
        print("The square root of the number is: ",square_root(num))
    elif ch==2:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("The greatest common divisor is",gcd(a,b))
    elif ch==3:
        ba=float(input("Enter the base value: "))
        ex=float(input("Enter the exponent value: "))
        print(ba,"raised to the power of",ex,"is",exponential(ba,ex))
    elif ch==4:
        print("You are exiting the program.")
        break
    else:
        print("Invalid choice.")
        
    
