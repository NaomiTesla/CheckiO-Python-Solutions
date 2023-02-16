# Naomi Tesla
# https://py.checkio.org/en/mission/all-upper/

def is_all_upper(text: str) -> bool:
    if text == text.upper():
        return True
    return False

assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True