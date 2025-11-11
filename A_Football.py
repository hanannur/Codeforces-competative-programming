n=input()
count=1
Flag=False
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        count+=1
        if count>=7:
            Flag=True
            break
    else:
        count=1
if Flag:
    print("YES")
else:
    print("NO")
