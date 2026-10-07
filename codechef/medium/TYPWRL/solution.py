# cook your dish here
t = int(input())
for _ in range(t):
    n ,m = map(int,input().split())
    s = input()
    l = input()
    
    cur = 0
    ans = 0
    prev= ""
    
    for ch in s:
        hand ="L" if ch in l else "R"
        
        if hand == prev:
            cur += 1
        else:
            cur = 1
            prev = hand
            
        ans = max(ans,cur)
    print(ans)