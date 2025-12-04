n= int(input())
s=input().lower()
l="abcdefghijklmnopqrstuvwxyz"
Flag=False
for i in range(len(l)):
    if l[i] in s:
        Flag=True
       
    else:
        Flag=False
        break
if Flag==True:
    print("YES")
else:
    print("NO")

    
        