s = input("Enter a string:\n")
vowels = set('aeiouAEIOU')
s = list(s)
left, right = 0, len(s) - 1

while left < right:
    while s[left] not in vowels and left < right:
        left += 1
    while s[right] not in vowels and left < right:
        right -= 1

    if left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

result = ''.join(s)
print(result)
