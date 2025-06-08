# find longest palindrome substring in given string

def is_palindrome(s):
    return s == s[::-1]

def expand_around_center(s, left, right):
    while left >=0 and right <= len(s) - 1 and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def solution(str):
    if not str:
        return ""
    longest = ""
    for i in range(len(str)):
        #Odd length palindrome
        odd_palindrome = expand_around_center(str,i,i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome

        #Even length palindrome
        even_palindrome = expand_around_center(str,i, i +1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    return longest