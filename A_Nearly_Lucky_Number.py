# n = input()
# s=set(n)
# if s=={'7','4'} or s=={'4','7'}:
#     print("YES")
# else:
#     print("NO")
#print(s)
# for i  in range(len(n)):
#     if n[i]==7 or n[i]==4:
#         continue
        
#     else:
#         print("NO")
#         break
# else:
#     print("YES")


n = input()
count=0
for i in range(len(n)):
    if n[i]=='4' or n[i]=='7':
        count+=1

if count==4 or count==7:
    print("YES")
else:
    print("NO")

    