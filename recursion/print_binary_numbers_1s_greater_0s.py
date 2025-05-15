one = 0
zero = 0
output = ""
def solve(one, zero, n, output):
    if n == 0:
        print(output)
        return
    solve(one+1, zero, n -1, output + "1")
    if one > zero:
        solve(one, zero +1, n -1, output + "0")

    return
print(solve(0, 0, 3, output))