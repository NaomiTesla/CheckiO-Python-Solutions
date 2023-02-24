# Naomi Tesla
# https://py.checkio.org/en/mission/unix-match-part-2/
# Honestly not that great of a solution, will def come back later for a better solution c:

def unix_match(filename: str, pattern: str) -> bool:
    if '[' in pattern:
        pattern = pattern.replace(']', '[').split('[')
        pattern[1] = [c for c in pattern[1]]
        match = filename[filename.index(pattern[2])-1]
        if not len(pattern[0]) and (len(pattern[2]) == len(filename)):
            return False
        elif '!' in pattern[1]:
            return match not in pattern[1][1:len(pattern[1])]
        return match in pattern[1]
    return filename == pattern


print(unix_match('name.txt', 'name.exe'))
print(unix_match('name.txt', '[!abc]name.txt'))  # False
print(unix_match('1name.txt', '[!abc]name.txt'))  # True


assert unix_match("log1.txt", "log[1234567890].txt") == True
assert unix_match("log1.txt", "log[!1].txt") == False
