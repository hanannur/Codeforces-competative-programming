n=int(input())
cards=list(map(int , input().split()))
serjascount=0
dimascount=0
left=0
right=n-1
turn=0
while left<=right:

    if cards[left]>cards[right]:
        chosen=cards[left]
        left+=1
    else:
        chosen=cards[right]
        right-=1
    if turn==0:
        serjascount+=chosen
    else:
        dimascount+=chosen

    turn=1-turn
print(serjascount ,dimascount)

    

    