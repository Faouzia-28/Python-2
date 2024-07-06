def Unreap(s):
    li=[];
    for char in s:
        if char not in li:
            li.append(char)
    return ''.join(li)
i_p=input("Enter a string:\n")
print("After removing repeating characters:\n",Unreap(i_p))
            
