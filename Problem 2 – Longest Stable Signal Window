from collections import deque

n = int(input())
a = list(map(int, input().split()))
k = int(input())

mx = deque()
mn = deque()

left = 0
best = 0
start = 1

for right in range(n):
    while mx and a[mx[-1]] <= a[right]:
        mx.pop()
    mx.append(right)

    while mn and a[mn[-1]] >= a[right]:
        mn.pop()
    mn.append(right)

    while a[mx[0]] - a[mn[0]] > k:
        if mx[0] == left:
            mx.popleft()
        if mn[0] == left:
            mn.popleft()
        left += 1

    length = right - left + 1

    if length > best:
        best = length
        start = left + 1

print(best, start)
