n = int(input())
m = int(input())
d = int(input())
xi,yi = [], []
for g in range(d):
    xiz = int(input())
    xi.append(xiz)
    yiz = int(input())
    yi.append(yiz)
print(min(xi)*min(yi), d) 