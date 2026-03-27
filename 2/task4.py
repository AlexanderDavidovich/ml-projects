from itertools import combinations
n = int(input('введите число n: '))
mink = int(input('введите число mink: '))
maxk = int(input('введите число maxk: '))
s = str(n)
ans = set()

for r in range(mink, maxk + 1):
    for idxs in combinations(range(len(s)), r):
        m = int(''.join(s[i] for i in idxs))
        if m > 0:
            ans.add(m * 2)
            if m % 2 == 0:
                ans.add(m // 2)

print(sorted(ans))