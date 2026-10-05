# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    mn = min(arr)
    print(sum(arr) - mn)