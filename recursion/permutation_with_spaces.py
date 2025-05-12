def solve(input, output):
    if len(input) == 0:
        return [output]
    
    # recursive calls
    result = []
    result += solve(input[1:], output + input[0])           # without space
    result += solve(input[1:], output + ' ' + input[0])     # with space
    return result

def generate(input_string):
    if not input_string:
        return []
    return solve(input_string[1:], input_string[0])  # Start from 1st char, no space before

print(generate("abc"))
