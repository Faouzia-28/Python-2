print("***SHOPPING CART***")
print("Enter no. of items")
a=int(input())
i=1
total=0
while i<=a:
    print("Enter item no.",i)
    na=input()
    print("Enter cost of the item no.",i)
    cost=int(input())
    print("Enter quantity of the item ")
    q=int(input())
    total=total+(cost*q)
    i+=1

print("The total is",total)    
    
