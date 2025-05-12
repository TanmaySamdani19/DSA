def solve(input, output):
    if len(input) == 0:
        print(output)
        return
    output1 = output
    output2 = output + input[0]
    input = input[1:]
    solve(input, output1)
    solve(input, output2)
    return

input = "abc"
output = ""
print(solve(input, output))