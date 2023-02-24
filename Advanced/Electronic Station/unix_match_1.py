# Naomi Tesla
# https://py.checkio.org/en/mission/unix-match-part-1/

import re


def unix_match(filename: str, pattern: str) -> bool:
    return re.match(r''+pattern.replace(".", "\.").replace("*", ".*").replace("?", ".")+'', filename) is not None


assert unix_match("somefile.txt", "*") == True
assert unix_match("other.exe", "*") == True
assert unix_match("my.exe", "*.txt") == False
assert unix_match("log1.txt", "log?.txt") == True
assert unix_match("log12.txt", "log?.txt") == False
assert unix_match("log12.txt", "log??.txt") == True
