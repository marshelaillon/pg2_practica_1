n = int(input("Enter a number: "))

factorial = 1

for i in range(n):
  factorial *= (i + 1)

print(factorial)