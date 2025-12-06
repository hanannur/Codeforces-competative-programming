# n=int(input())
# i=list(map(int,input().split()))
# for j in range(n):
#     if i[j]==1:
#         print("HARD")
#         break
# else:
#     print("EASY")
n=int(input())
s=list(map(int , input().split()))
set_s=set(s)
if 1 in s:
    print("HARD")
else:
    print("EASY")