a = int(input("Enter a: "))

num = 1
result = []

while num <= a:
    result.append(num)
    num += 2

print(*result, sep=", ")
