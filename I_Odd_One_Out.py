t=int(input())
for i in range(t):
    reapeted_nums=list(map(int,input().split()))
    if reapeted_nums[0]!=reapeted_nums[1] and reapeted_nums[0]!=reapeted_nums[2]:
        print(reapeted_nums[0])
    elif reapeted_nums[1]!=reapeted_nums[0] and reapeted_nums[1]!=reapeted_nums[2]:
        print(reapeted_nums[1])
    else:
        print(reapeted_nums[2])