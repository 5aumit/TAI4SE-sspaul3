def find(x):
    if root[x] == x:
        return x
    return find(root[x])

V, E = map(int, input().split())
data = []
root = [i for i in range(V+1)]
S = [1]*(V+1)

for i in range(E):
    A, B, C = map(int, input().split())
    data.append((C, A, B))

data.sort()
cnt = 0
for d in data:
    w, n1, n2 = d
    A = find(n1)
    B = find(n2)

    if A != B:
        cnt += w
        if S[A] > S[B]:
            root[B] = A
            S[A] += S[B]
        else:
            root[A] = B
            S[B] += S[A]

print(cnt)
