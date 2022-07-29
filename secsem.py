#one
def gcd(a,b):
    if b==0:
        return(a)
    else:
        return gcd(b,a%b)
a=int(input("enter the number:"))
b=int(input("enter the number:"))
Gcd=gcd(a,b)
print("Gcd is:")
print(Gcd)

#two
def newtonssqrt(n):
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while better!=approx:
        approx=better
        better=0.5*(approx+n/approx)
    return approx
num1=int(input("enter the number:"))
print("square root of 1st no", newtonssqrt(num1))


#three
def power(base,exp):
    if exp==1:
        return(base)
    else:
        return base*power(base,exp-1)
base=int(input("enter the number:"))
exp=int(input("enter the number:"))
print("result:",power(base,exp))

#four
a=[]
n=int(input("enter the number:"))
for i in range(1,n+1):
               b=int(input("enter:"))
               a.append(b)
a.sort()
print("The maximum number is:",a[n-1])



#afive
num=[12,44,5,62,2,27,85,9]
x=int(input("enter the number to search:"))
def linear(num,x):
    for i in range(len(num)):
        if x==num[i]:
            return i
    return -1
result=linear(num,x)
if result==-1:
    print(f"{x}is not found in the list")
else:
    print(f"{x}is found at position {result}")

#bfive
def binary_search(List, search):
    first_index = 0
    last_index = len(List) - 1
    found = False
    result = False
    while first_index <= last_index and not found:
        mid = (first_index + last_index) // 2
        if search == List[mid]:
            found = True
            result = mid
        elif search < List[mid]:
            last_index = mid - 1
        else:
            first_index = mid + 1
    return result


list1 = [3, 6, 2, 8, 34, 98, 24, 67, 1]
list1.sort()
print(list1)
num = int(input("Enter search element: "))
output = binary_search(list1, num)
if output == False:
    print(f"{num} is not in list")
else:
    print(f"{num} is found at position {output}")

#asix
def selection_sort(list1):
    for i in range(0, len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] > list1[j]:
                (list1[i], list1[j]) = (list1[j], list1[i])


List1 = [4, 7, 3, 12, 65, 1, 2, 98, 32]
print("Before Sorting:", List1)
selection_sort(List1)
print("After Sorting:", List1)

#bsix
def insertionSort(list1):
    for index in range(1, len(list1)):
        current_value = list1[index]
        position = index
        while position > 0 and list1[position - 1] > current_value:
            list1[position] = list1[position - 1]
            list1[position - 1] = current_value
            position = position - 1


List1 = [54, 26, 93, 11, 77, 35, 44, 55, 22]
print("Before Sorting:", List1)
insertionSort(List1)
print("After Sorting:", List1)

#seven
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def mergesort(list1):
    if len(list1) < 2:
        return list1
    else:
        mid = len(list1) // 2
        left = mergesort(list1[:mid])
        right = mergesort(list1[mid:])
        return merge(left, right)


List1 = [6, 4, 87, 23, 4, 5, 76, 13, 80]
print("Before Sorting: ", List1)
print("After Sorting", mergesort(List1))

#eight
num = int(input("Enter a number to find first N prime numbers: "))
for i in range(2, num + 1):
    if i == 2:
        print(i)
    elif i > 2:
        for j in range(2, (i // 2) + 2):
            if i % j == 0:
                break
        else:
            print(i)
    else:
        pass






#nine
x = eval(input("Enter matrix 1: "))
y = eval(input("Enter matrix 2: "))
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += x[i][k] * y[k][j]


for row in result:
    print(row)


x=input("enter the name:")
y=input("enter the name:")
z=input("enter the name:")
#ten
import sys
total = len(sys.argv)
cmdargs = str(sys.argv)
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)
print ("Script name: %s" % str(sys.argv[0]))
print ("First argument: %s" % str(sys.argv[0]))
print ("Second argument: %s" % str(sys.argv[1]))
print ("Third argument: %s" % str(sys.argv[2]))
