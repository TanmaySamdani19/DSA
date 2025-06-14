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