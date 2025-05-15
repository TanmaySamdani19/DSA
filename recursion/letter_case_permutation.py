def print_letter(s):
    input = s
    output = ""
    arr = []
    solve(input, output, arr)
    return arr

def solve(input, output, arr):
    if len(input) == 0:
        arr.append(output)
        return
    
    if input[0].isalpha():
        output1 = output +input[0].lower()
        output2 = output +input[0].upper()
        input = input[1:]
        solve(input, output1, arr)
        solve(input, output2, arr)
    else:
        output1 = output + input[0]
        input = input[1:]
        solve(input, output1, arr)
    return arr

print(print_letter("a1B2"))