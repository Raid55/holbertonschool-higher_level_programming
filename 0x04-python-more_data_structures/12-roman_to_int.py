#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    final = 0

    if not isinstance(roman_string, str) or roman_string is None:
        return final

    str_len = len(roman_string)
    i = 0
    while i < str_len:
        num1 = roman[roman_string[i]]

        if i + 1 < str_len:
            num2 = roman[roman_string[i + 1]]

            if num1 >= num2:
                final += num1
                i += 1
            else:
                final += num2 - num1
                i += 2
        else:
            final += num1
            i += 1

    return final
