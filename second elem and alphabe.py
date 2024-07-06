#to get name and corresponding scores and fins second element and printing the names alphabetically
n = int(input())
names = []
scores = []
# Read names and scores
for i in range(n):
    names.append(input())
    scores.append(float(input()))

# Find the smallest and second smallest scores
min1 = float('inf')
min2 = float('inf')

for i in scores:
    if i < min1:
        min2 = min1
        min1 = i
    elif min1 < i < min2:
        min2 = i

nind = [names[i] for i in range(n) if scores[i] == min2]

# Print the names with the second lowest score
for i in sorted(nind):  # Sorting the names alphabetically
    print(i)

            
