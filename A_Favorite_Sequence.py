n=int(input())
for i in range(n):
    s=int(input())
    left =0
    right=s-1
    Polycarp=[]
    a=list(map(int,input().split()))
    while right>left:
        Polycarp.append(a[left])
        Polycarp.append(a[right])
        left+=1
        right-=1
    if right==left:
        Polycarp.append(a[left])
    print(*Polycarp)

