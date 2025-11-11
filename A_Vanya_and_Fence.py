n,h=map(int,input().split())
heights=list(map(int,input().split()))
length_of_width=0
for i in range(n):
    if heights[i]<=h:
        length_of_width+=1
    elif heights[i]>h:
        length_of_width=length_of_width+2
print(length_of_width)
