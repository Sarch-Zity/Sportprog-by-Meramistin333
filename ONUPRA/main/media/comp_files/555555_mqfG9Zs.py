n = int(input())
m = int(input())
d = int(input())
a = []
b = []
for i in range(d):
    a.append(int(input()))
    b.append(int(input()))
# print(a, b)
# aMin = min(a)
# bMin = min(b)
print(min(a) * min(b), d)