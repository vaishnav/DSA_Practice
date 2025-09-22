# Strings are immutable in Python → once created, they cannot be changed.
# This makes repeated concatenation (+ in a loop) O(n²) in worst case.

result = ""
for i in range(5):
    result += str(i)

print(result)


# Above solution is inefficient, as for every += operation a new string is created a better solution would be to use .join


parts = []
for i in range(5):
    parts.append(str(i))

result = ''.join(parts)
print(result)

