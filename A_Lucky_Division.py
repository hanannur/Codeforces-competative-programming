n=int(input())
s=sorted(set(str(n)))
joined=int(''.join(s))

if n%4==0 or n%7==0 or joined==47 or joined==74:
    print("YES")
else:
    print("NO")