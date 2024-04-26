T = int(input())
for _ in range(T):
    n, k, b, s = map(int, input().strip().split())
    
    if s-k*b < 0:
        print(-1)
    elif s-k*b > (k-1)*n or s-k*b > k*n or (k != 1 and s-k*b-(k-1)*((s-k*b)//(k-1)) < 0):
        print(-1)
    elif k == 1 :
        ans = list(0 for i in range(n))
        ans[0] += (s-b)
        ans[n-1] = ans[n-1]+b
        print(' '.join(map(str, ans)))
    else:
        p = (s-k*b)//(k-1)

        ans = list(0 for i in range(n))

        for i in range(p):
            ans[i] = k-1
        ans[n-1] = ans[n-1]+s-(k-1)*p
        print(' '.join(map(str, ans)))
    
