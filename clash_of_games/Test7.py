n = int(input())
b = bin(n)[2:-1]
o = oct(int(b, 2))[2:-1]
h = hex(int(o, 8))[2:-1]

i = int(h, 16)

print(i)