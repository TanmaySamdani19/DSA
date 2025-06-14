# Variables are dynamicly typed
n = 0
print('n = ', n)

# Multiple assignments
n, m = 0, "abc"

# Increment
n = n + 1
n += 1
# n++ - not work

# None is null (absence of value)

# I f statements dont need parentheses
# or curly braces.
n= 1
if n> 2:
    n-=1
elif n == 2:
    n *= 2
else:
    n += 2


# Parentheses needed for multi-line  conditions.
# and  = &&
# or  = ||
n, m = 1,2
if ((n > 2 and n!=m) or n==m):
    n += 1

# while loops are similar
n = 0
while n < 5:
    print(n)
    n += 1

# looping from i = 0  to i = 4
for i in range(5):
    print(i)

# looping from i = 2 to i =5
for i in range(2, 6):
    print(i)

# looping from i = 5 to i = 2
for i in range (5, 1, -1):
    print(i)

# Division is decimal by default
print( 5/2)

# Double slash rounds down
print(5//2)

# CAREFUL : most languaes round towards 0 by default so negatie numbers will round down
print(-3 // 2)


# A workaround for rounding towards zero is to use decimal divison and then convert to int.
print(int(-3/2)) 

# Modding is similar to most languages
print( 10 % 3 )

# Except for negative values
print(-10 % 3)


# to be consistent with other languages modulo
import math
print(math.fmod(-10, 3))

# More math helpers
print( math.floor(3 / 2))
print( math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2,4))


# Math / Min Int
float("inf")
float("-inf")

# Python numbers are infinite so they never overflow
import math
print(math.pow(2, 300))

# But still les than infinity

# Arrays (called lists in python)
arr = [1,2,3]
print(arr)

# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1,7)
print(arr)
#inserting  in middle is o(n) time operation 

#but indexing is constant time operation
arr[0] = 0

# Initialize arr of size n with default value of 1
n = 5
arr = [i] * n
print(arr)
print(len(arr))

# Careful : -1  is not out of bounds,
# its the last value
arr = [1, 2, 3]
print(arr[-1])

# Sublists  (aka slicing)
arr = [1,2,3,4]
print(arr[1:3])

# Similar to for loop ranges, last index is
# non-inclusive
print(arr[0:4])


# Unpacking
a, b, c = [1,2,3]
print(a,b,c )

# Careful though
# a,b  = [1, 2, 4]

# Loop through arras
nums = [1, 2, 3]

# Using index
for i in range(len(nums)):
    print(nums[i])

# Without index
for n in nums:
    print(n)

# With index and value
for i, n in enumerate(nums):
    print(i, n)

# Loop through multiple arrays simultaneously with unpacking
nums1 = [1,3,5]
nums2 = [2,4,6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)


# reverse
nums = [1,2,3]
nums.reverse()

# sorting
arr = [4,2, 4,6]
arr.sort()
arr = ['apple', 'kiwi', 'banana']
# it will aslso sort in alphabetical order
# Custom sort (by lenght of string)
arr.sort(key = lambda x : len(x))

# List comprehension
arr = [i for i in range(5)]
print(arr)

# 2-D lists
arr = [[0]*4 for i in range(4)]

# This won't work
arr = [[0]* 4] *4
print(arr)
# you can make this but if you make changes to any one it will applied to everything

# Strings are similar to arrays
s = 'abc'
print(s[0:2])

# But they are immutable

# So this create a new string
s += 'def'
print(s)

# valid numeric strings cna be converted
print(int("123") +int("123"))

# Add numvers can be converted to strings
print(str(123) + str(123))

# in rare cases you may need the ASCII value of char
print(ord("a"))
print(ord("b"))


# COmbine a list of strings (with an empty stirng delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))

# Queues double ended queue
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

# similar to stack in python but benefit is we can pop from left and we can do it in cosntant time unlike stack
queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)


# HashSet
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))
print(1 in mySet)
mySet.remove(2)
print(2 in mySet)

# list to set
print(set([1, 2, 3]))

# Set comprehension
mySet =  { i for i in range(5)}
print(mySet)


# HashMap (aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap))

myMap['alice'] = 80
print(myMap['alice'])

print('alice' in myMap)
myMap.pop('alice')
print('alice' in myMap)

myMap = {'alice' :90, 'bob':70}
print(myMap)

# Dict comprehension
myMap = {i : 2*i for i in range(3)}
print (myMap)

# Looping through maps
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)


# Tuples are like arrays but immutable
tup = {1,2,3}
print(tup)
# print(tup[0])

# Can't modify

# Can be used as key for hash map/set
myMap = { (1,2): 3}
print(myMap[(1,2)])


# mySet = set()
# mySet.add((1,2))
# print((1,2) in mySet)

# Lists cant be keys
# myMap[[3,4]] = 5  -this will not work so we use tuple 

# Heaps
import heapq
# under the hood are arrays
minHeap = []
heapq.heappush(minHeap,3)
heapq.heappush(minHeap,2)
heapq.heappush(minHeap,4)

#  min is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

# No max heaps by default, work around is to use min heap and multiply by -1 when push and pop.
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1* maxHeap[0])

while len(maxHeap):
    print(-1*heapq.heappop(maxHeap))

# Build heap from iniial values
arr = [2,1,8,4,5]

heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

# Funcitons
def myFunc(n, m):
    return n* m


# Nested funciton 
def outer(a,b):
    c = "c"

    def inner():
        return a+b+c
    return inner()

print(outer("a","b"))

# Can modify objects but not reassign
# unless using nonlocal keyboard
def double(arr, val):
    def helper():
        for i, n  in enumerate(arr):
            arr[i] *= 2

        # will only modify val in the helper scope
        # val *= 2

        # this will modify val outside helper scope
        nonlocal val
        val *=2

    helper()
    print(arr, val)

nums = [1,2]
val = 3
double(nums,val)  

# Class
class MyClass:
    # Constructor
    def __init__(self, nums):
        # Create member variables
        self.nums = nums
        self.size = len(nums)

    # sef keyword required as param
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2*self.getLength()