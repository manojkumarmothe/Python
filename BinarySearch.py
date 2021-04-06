#Binary Search Iterative
'''
mylist = [25,18,27,11,10,19,36,45,12,100,-1,-2,12,110]
def binarySearch(mylist,k):
    l=sorting(mylist)
    low = 0
    high = len(l)-1
    mid = 0
    while low<=high:
        mid= (low+high)//2
        if k < l[mid]:
            high=mid-1
        elif k > l[mid]:
            low= mid+1
        else:
            return mid
    return -1
def sorting(mylist):
    if len(mylist)>1:
        for i in range(len(mylist)):
            for j in range(len(mylist)-1-i):
                if mylist[j]>mylist[j+1]:
                    temp = mylist[j]
                    mylist[j] = mylist[j+1]
                    mylist[j+1] = temp
    print(mylist)
    return mylist

n= int(input('enter the number to find index in list'))
bin=binarySearch(mylist,n)
if bin !=-1:
    print('{} is found at {} index postion'.format(n,bin))
else:
    print('{} is not found'.format(n))
'''
# Binary Search recursive

def binarySearch(l,low,k,high):
    if low<=high:
        mid = (low+high)//2
        if k  == l[mid]:
            return mid
        elif k < l[mid]:
            high = mid-1
            return binarySearch(l,low,k,high)
        elif k > l[mid]:
            low = mid+1
            return binarySearch(l,low,k,high)
        else:
            return mid
    else:
        return -1
    
def sorting(mylist):
    if len(mylist)>1:
        for i in range(len(mylist)):
            for j in range(len(mylist)-1-i):
                if mylist[j]>mylist[j+1]:
                    temp = mylist[j]
                    mylist[j] = mylist[j+1]
                    mylist[j+1] = temp
    print(mylist)
    return mylist
mylist = [25,18,27,11,10,19,36,45,12,100,-1,-2,12,110]
l= sorting(mylist)
low = 0
high = len(l)
n= int(input('enter the number to find index in list:'))
bin=binarySearch(l,low,n,high)
if bin !=-1:
    print('{} is found at {} index postion'.format(n,bin))
else:
    print('{} is not found'.format(n))

