n=int(input())
for i in range(n):
    t=int(input())
    if t>=1900:
        print("Division 1")
    elif t>=1600 and t<=1899:
        print("Division 2")
    elif t>=1400 and t<=1599:
        print("Division 3")
    else:
        print("Division 4") 