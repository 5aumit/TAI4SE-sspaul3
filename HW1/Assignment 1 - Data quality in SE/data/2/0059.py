from bisect import bisect_left as bisect
while True:
    xp, yp = set(), set()
    veneer = []
    W, H = map(int, input().split())
    if not W:
        break
    N = int(input())
    for i in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        veneer.append((x1, y1, x2, y2))
        xp.add(x1)
        xp.add(x2)
        yp.add(y1)
        yp.add(y2)
    xp = list(xp)
    yp = list(yp)
    wa = [[0 for x in range(len(xp) + 1)] for y in range(len(yp) + 1)]
    print()
    for v in veneer:
        xi1 = bisect(xp, v[0])
        xi2 = bisect(xp, v[1])
        yi1 = bisect(yp, v[2])
        yi2 = bisect(yp, v[3])
        print(xi1, yi1, xi2, yi2)
        wa[yi1][xi1] += 1
        wa[yi2 + 1][xi1] -=1
        wa[yi1][xi2 + 1] -=1
    mem = [[0 for x in xp] for y in yp]
    for y, _ in enumerate(yp):
        for x, _ in enumerate(xp):
            mem[y][x] += wa[y][x]
            if y > 0:
                mem[y][x] += mem[y - 1][x]
            if x > 0:
                mem[y][x] += mem[y][x - 1]
        print(wa[y])
