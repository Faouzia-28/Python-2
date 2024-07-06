x="PIZZA TOPPINGS"
x=x.center(50,'*')
print(x)
print("Enter the toppings that you desire. Enter 'Quit' when you're done")
n=3
for i in range(1,n):
    a=input(i)
    if a!="Quit"or a!="quit":
        print("your topping will be added")
        i+=1
        n+=1
        continue
    else:
        break
    
