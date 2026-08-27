# https://atcoder.jp/contests/joi2015yo/submissions/16057780
# D - シルクロード (Silk Road)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    D = list(int(input()) for _ in range(n))
    C = list(int(input()) for _ in range(m))

    dp = [[f_inf] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0
    for i in range(1, m + 1):
        c = C[i - 1]
        for j in range(n):
            d = D[j]
            # 移動しない場合
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
            # 移動する場合
            dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][j] + c * d)

    res = f_inf
    for i in range(m + 1):
        res = min(res, dp[i][-1])
    print(res)


if __name__ == '__main__':
    resolve()
