def second_large(li):
    m1=-999999
    m2=m1
    for i in li:
        if i>m1:
            m2=m1
            m1=i
        if i!=m1 and m2<i:
            m2=i
    return m2

l=[]
print("Enter values in the list. If enough enter 'exit'")
while True:
    n=input("Enter a value: ")
    if n.lower() =='exit':
        break
    l.append(float(n))
print(l)
s=second_large(l)
if s==-1:
    print("List should have atleast 2 elements")
else:
    print("The second largest element is",s)
