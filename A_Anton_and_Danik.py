n=int(input())
s=input()
count1=0
count2=0

for i in s:
    if i=='A':
        count1+=1
    elif i=='D':
        count2+=1

if count1>count2:
    print("Anton")
elif count2>count1:
    print("Danik")
else:
    print("Friendship")

