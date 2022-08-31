import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
sumlist = [nums[0]]

for i in range(1, n):
    sumlist.append(sumlist[i-1] + nums[i])

sumlist.append(0)
for i in range(m):
    i, j = map(int, input().split())
    print(sumlist[j - 1] - sumlist[i - 2])