num = int(input("Enter number: "))

s = 0
for i in str(num):
    s += int(i) ** 3

if num == s:
    print("Armstrong number")
else:
    print("Not Armstrong")