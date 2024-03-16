integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
 
def roman_to_arabic(roman):
    result = 0
    for i, c in enumerate(roman):
        if i+1<len(roman) and integers[roman[i]] < integers[roman[i+1]]:
            result-=integers[roman[i]]
        else:
            result+=integers[roman[i]]
    return str(result)
 
def arabic_to_roman(arabic):
    romans = list(integers)
    str_arabic = arabic[::-1]
    str_arabic_len = len(str_arabic)
    result = str()
    romans_pointer = 0
    for i in range(str_arabic_len):
        if str_arabic[i] in ['0', '1', '2', '3']:
            result = romans[romans_pointer] * int(str_arabic[i]) + result
        elif str_arabic[i] in ['4']:
            result = romans[romans_pointer] + romans[romans_pointer + 1] + result
        elif str_arabic[i] in ['5', '6', '7', '8']:
            result = romans[romans_pointer + 1] + romans[romans_pointer] * (int(str_arabic[i]) - 5) + result
        elif str_arabic[i] in ['9']:
            result = romans[romans_pointer] + romans[romans_pointer + 2] + result
        romans_pointer += 2
    return result
 
def parse_inegers():
    with open('input.txt', 'r') as file_input:
        file_input=file_input.read().splitlines()
 
    with open('output.txt', 'w') as file_output:
        for i in file_input:
            if i.isdigit():
                file_output.write(arabic_to_roman(i) + '\n')
            else:
                file_output.write(roman_to_arabic(i) + '\n')
 
 
parse_inegers(1)