# Program to print a patter of stars(*)


print("how many rows you wanna print\n:")
n = int(input())
print("choose 1 or 0:\n")
a = int(input())
b = bool(a)

if b == True:
    for i in range(n):
        print("* " * (i+1))
else:
    for i in range(n):
        print(("* " * (n-i)))
