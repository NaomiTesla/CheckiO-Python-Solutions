# Naomi Tesla
# https://py.checkio.org/en/mission/roman-numerals/


def checkio(data):
    # Dict containing base roman numerals and valid subtractive notation groups below 4,000 c:
    roman_nums = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    def int_to_numeral(num: int):
        roman_numeral = ""
        for roman, arabic in roman_nums.items():
            while arabic <= num:
                roman_numeral += roman
                num -= arabic
            if num == 0:
                return roman_numeral
    return int_to_numeral(data)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
