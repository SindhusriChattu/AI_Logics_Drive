n = int(input())

ranges = []

for _ in range(n):
    start, end = map(int, input().split())
    ranges.append((start, end))

# Sort based on starting time
ranges.sort()

merged = []

for start, end in ranges:
    if not merged or start > merged[-1][1]:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

for start, end in merged:
    print(start, end)
