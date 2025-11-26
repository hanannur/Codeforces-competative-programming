t=int(input())
for i in range(t):
    med_num=list(map(int,input().split()))
    sorted_med=sorted(med_num)
    print(sorted_med[1])