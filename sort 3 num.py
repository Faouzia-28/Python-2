def sort_three_numbers(a, b, c):
    mini=min(a, b, c)
    maxi= max(a, b, c)
    mid = (a + b + c) - mini-maxi
    return mini,mid,maxi

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
s= sort_three_numbers(n1,n2,n3)
print("Sorted numbers:",s)
