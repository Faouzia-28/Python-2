#assignment10
s=input("Enter your password")
c1=0;c2=0
l=len(s)
for i in s:
    if i.isalnum():
        if i.islower():
            c1=1
