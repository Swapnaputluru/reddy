'''
'''
# print numbers in serial wise
i = 1
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()

# print numbers in reverse order
for i in range(5, 0, -1):
    for j in range(0, i):
        print(i, end="")
    print()

# print characters in reverse order
a = 65
for i in range(1,6):
    for j in range(1, i + 1):
        print(chr(a), end="")
        a = a + 1
    print()


a = 65
for i in range(6, 1, -1):
    for j in range(i - 1):
        print(chr(a), end="")
        a = a + 1
    print()


# print stars in reverse order
for i in range(5,1):
    for j in range(5-i):
        print("*",end="")
    print()


print("Write a program to print first 10 even numbers in reverse order")
i = 10
while i >= 1:
    print(i)
    i -= 2

print("Write a program to print table of a number accepted from user")
num = int(input("Enter the number:"))
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(num, "*", i, "=", num*i)


print("don't print multiples of 2 and 3")
for a in range(1,20):
    if a % 2 == 0 or a % 3 == 0:
        continue
    print(a)

print("dividable by 11 not with 2")
for i in range(100, 500):
     if i % 11 == 0 and i % 2 != 0:
        print(i)

print("find even and odd numbers between 12 and 37 including 12 and 37")
for i in range(12, 38):
    if i % 2 == 0:
        print("Even number:", i)
    else:
        print("odd number:", i)

print("sum of digits accepted by user")

num = int(input("Enter the number:"))
sum = 0
for i in str(num):
    sum = sum + int(i)
print(sum)

print("product of digits accepted by user")
num = int(input("Enter the number:"))
product = 1
for i in str(num):
    product = product * int(i)
print(product)


print("find out given number is prime or not")
num =int(input("enter the number:"))
for i in range(2,num):
    if num % i == 0:
        break
        print("not prime")
    else:
        print("prime")


print("find out factorial of given number ")
num = int(input("enter the number:"))
num2 = 1
for i in range(num, 1, -1):
    num2 = num2 * i


print(num2)
print()




