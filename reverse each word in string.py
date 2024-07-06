a = input("Enter the message to encode: ")
words = a.split()
b= ' '.join(word[::-1] for word in words)
print("Encoded message:", b)












