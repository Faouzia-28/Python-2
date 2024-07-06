#concatenate
s1="Hi "
s2="python class"
print(s1+s2)
#repeting string
print(s1*3)
#string is immutable
#changes the first letter into capital
str="welcome"
print(str.capitalize())
#changes the first letter of every word capital
str1="welcome to pYthon"
print(str1.title())
#changing to lower case
print(str1.lower())
#checks if its lower
print(str1.islower())
#checks if its upper
print(str1.isupper())
#checks if only alphabets is present
print(str1.isalpha())#space is a special character so returns false
#returns true if characters in the string are alphabets or numbers.
print(str1.isalnum())
#checks if digits are present. Returns tru if all the characters is the string are digits.
print(str1.isdigit())
#converts lower to upper and upper to lower
print(str1.swapcase())
#casefold and lower same function
print(str1.casefold())
print(str1.center(100,'*'))
#checks if the last letter ends with the given letter
print(str1.endswith("n"))
#checks the starting letter
print(str1.startswith("w"))
print(str1.find('e1',0,len(str1)))
a="    hgyi     "
#removes the unwanted spaces from the string
print(a.strip())
#removes left side space
print(a.lstrip())
#removes right side space
print(a.rstrip())


