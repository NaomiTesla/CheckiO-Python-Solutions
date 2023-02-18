# Naomi Tesla
# https://py.checkio.org/en/mission/cut-sentence/
# Will be cleaned up and made more efficient later c:

def cut_sentence(line: str, length: int) -> str:
    if length < len(line):
        truncated = line[:length].strip()
        if truncated + ' ' not in line:
            if truncated.rfind(' ') > -1:
                truncated = truncated[:truncated.rfind(' ')]
            else:
                truncated = ''
        return truncated + "..."
    return line


print("Example:")
print(cut_sentence("Hi my name is Alex", 1))

# These "asserts" are used for self-checking
assert cut_sentence('Hi my name is Alex', 1) == '...'
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

print("The mission is done! Click 'Check Solution' to earn rewards!")
