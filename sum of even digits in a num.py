print("enter the digit")
n=int(input())
t=n
sum=0
while t!=0:
    d=t%10
    if d%2==0:
        sum+=d
    t=t//10
print(sum)
