n=int(input())
i=list(map(int,input().split()))
for j in range(n):
    if i[j]==1:
        print("HARD")
        break
else:
    print("EASY")