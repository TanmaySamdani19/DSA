def print_paranthesis(n):
    arr = []
    open = n
    close = n
    output = ""
    solve(open,close, output, arr)
    return arr

def solve(open, close, output, arr):
    if open == 0 and close == 0:
        arr.append(output)
        return
    if open > 0:
        solve(open - 1, close, output + "(", arr)
    if close > open:
        solve(open, close -1, output + ")", arr)
    return arr

print(print_paranthesis(3))