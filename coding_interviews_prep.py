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