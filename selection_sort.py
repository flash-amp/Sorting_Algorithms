print("----------selection Sort----------")

def display(arr):
    print(*arr,sep=',')

def sel_sort(arr):
    if(arr == []):
        return []
    x = arr.index(min(arr))
    arr[0],arr[x] = arr[x],arr[0]
    return [arr[0]]+sel_sort(arr[1:])

a = [6,5,2,3,1]
'''
n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
'''
display(a)
a = sel_sort(a)
display(a)
