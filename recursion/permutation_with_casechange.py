def solve(input, output):
    if len(input) == 0:
        print(''.join(output))
        return
    output1 = output + [input[0].lower()]
    output2 = output + [input[0].upper()]
    solve(input[1:], output1)
    solve(input[1:], output2)

solve("abc", [])
