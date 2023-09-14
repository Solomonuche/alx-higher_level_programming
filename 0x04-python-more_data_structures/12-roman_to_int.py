#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
    }
    last_value = 0
    result = 0
    if not isinstance(roman_string, str) or None:
        return 0

    for i in reversed(roman_string):
        if i not in roman_dict:
            return 0

        value = roman_dict[i]
        if value < last_value:
            result -= value
        else:
            result += value
        last_value = value

    return result
