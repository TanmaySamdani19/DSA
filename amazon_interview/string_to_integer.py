def solution(string):
    string = string.strip() # remove leading and trailing spaces
    if not string:
        return 0
    sign  = 1
    result = 0

    if string[0] == '-' or string[0] == '+':
        if string[0] == '-':
            sign = -1
        string = string[1:]

    for char in string:
        if not char.isdigit():
            break
        result = result * 10 + int(char) # convert character to integer
        # and update the result
    result = result * sign

    if result  < -2**31:
        return -2**31
    elif result > 2**31 - 1:
        return 2**31 -1
    return result
