#Solution by nnk94087 in python 2
i = int(input())
lis = list(map(int,input().strip().split()))

m = max(lis)
while max(lis) == m:
    lis.remove(max(lis))

print(max(lis))
