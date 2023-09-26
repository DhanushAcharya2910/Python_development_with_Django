
n = int(input("Enter a number (n): "))

result_dict = {}

for x in range(1, n + 1):
    result_dict[x] = x * x

print(result_dict)