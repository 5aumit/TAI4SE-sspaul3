N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]

aoki = 0
taka = 0
for a, b in ab:
    aoki += a

ab.sort(key=lambda x: sum(x)+x[0], reverse=True)

ans = 0
for a, b in ab:
    aoki -= a
    taka += a + b
    ans += 1
    if taka > aoki:
        break

print(ans)