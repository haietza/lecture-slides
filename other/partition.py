import sys

pivot = int(sys.argv[1])
n = [int(x) for x in sys.argv[2:]]
p = n.index(pivot)

print(n)
print(pivot, p)

n[p], n[-1] = n[-1], n[p]
print(n)
a, b = 0, len(n) - 2
while a < b:
    while n[a] < p:
        a += 1
    while n[b] > p:
        b -= 1
    if a < b:
        n[a], n[b] = n[b], n[a]
        a += 1
        b -= 1
n[a], n[-1] = n[-1], n[a]
print(n)