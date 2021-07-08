print("----------Merge Sort----------")

def display(arr):
    print(*arr,sep=',')

def merge(a,b):
    if(a == []):
        return b
    if(b == []):
        return a
    if(a[0] <= b[0]):
        return [a[0]]+merge(a[1:],b)
    if(a[0] > b[0]):
        return [b[0]]+merge(a,b[1:])
    
def merge_sort(arr):
    if(len(arr) <= 1):
        return arr
    m = len(arr)//2
    return merge(merge_sort(arr[:m]),merge_sort(arr[m:]))

a = [6,5,2,3,1]
'''
n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
'''
display(a)
a = merge_sort(a)
display(a)