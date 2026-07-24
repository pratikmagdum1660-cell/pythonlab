'''n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i)''' 

'''n = int(input("Enter n: "))

for i in range(2, n + 1, 2):
    print(i)'''

'''n = int(input("Enter n: "))

for i in range(1, n + 1, 2):
    print(i)'''

'''n = int(input("Enter number of terms: "))

a = 1
for i in range(n):
    print(a, end=" ")
    a = a * 2'''

n = int(input("Enter n: "))

fact = 1
sum = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum =", sum)