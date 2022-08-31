import sys
input = sys.stdin.readline

n, m = map(int, input().split())

numlist = []
sumlist = []

for i in range(n):
    numlist.append(list(map(int, input().split())))
    sumlist.append([numlist[i][0]])
    for j in range(1, n):
        sumlist[i].append(sumlist[i][j - 1] + numlist[i][j])
    sumlist[i].append(0)

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0
    for
    print(result)
