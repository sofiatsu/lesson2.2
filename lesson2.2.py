a = int(input("enter a number"))

c = str(a%10)
b = str((a//10)%10)
d = str((a//100)%10)
e = str((a//1000)%10)
f = str(a//10000)

print(str(c+b+d+e+f))


