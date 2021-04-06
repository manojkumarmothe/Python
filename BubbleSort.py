# Bubble sort:
# added new line
# In array current element is compared with the next element.
# if current element is greater then next element it is swapped

l=[4,3,5,6,7,2,1,35,45,-1,0,12]
temp =0
for i in range(len(l)):
    for j in range(len(l)-1-i):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1]=temp
print(l)
