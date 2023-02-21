# Naomi Tesla
# https://py.checkio.org/en/mission/acceptable-password-iv/

def is_acceptable_password(password: str) -> bool:
    return ((any(char.isdigit() for char in password) and not password.isdigit()) or len(password) > 9) and len(password) > 6


assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("notshort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
