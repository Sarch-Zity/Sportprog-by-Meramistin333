v = int(input())
ans = []
for _ in range(v):
    n, m = map(int, input().split())
    if (n + m) % 2 == 0:
        ans.append("Tonya")
    else:
        ans.append("Burenka")
for i in range(len(ans)):
    print(ans[i])