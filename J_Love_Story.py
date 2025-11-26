t=int(input())
for i in range(t):
    diffrent=input()
    check="codeforces"
    count=0
    for j in range(10):
        if diffrent[j]!=check[j]:
            count+=1
    print(count)
      