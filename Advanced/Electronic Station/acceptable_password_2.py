# Naomi Tesla
# https://py.checkio.org/en/mission/acceptable-password-ii/

def is_acceptable_password(password: str) -> bool:
    return any(char.isdigit() for char in password) and len(password) > 6


assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
