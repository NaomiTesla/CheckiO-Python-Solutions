# Naomi Tesla
# https://py.checkio.org/en/mission/goes-after/

def goes_after(word: str, first: str, second: str) -> bool:
    return bool(len(word)) and -1 not in [word.find(first), word.find(second)] and not bool(word.index(first)+1 == len(word)) and not first == second and word.index(second) > word.index(first) and word[word.index(first)+1] == second


assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False
