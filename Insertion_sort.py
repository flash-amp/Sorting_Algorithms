print("----------Insertion Sort----------")

def display(arr): #Display Function
    print(*arr,sep=',')

def ins_sort(arr):
    n = len(arr) 
    for i in range(1,n): #This loop runs from 1 to n
        for j in range(i,0,-1): #This loop runs from i to 0 (in reverse)
            if(arr[j] < arr[j-1]):
                arr[j],a[j-1] = arr[j-1],arr[j]
            else:
                break
    return

a = [6,5,2,3,1] # Input
'''
n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
'''
display(a)
ins_sort(a)
display(a)
