# Naomi Tesla
# https://py.checkio.org/en/mission/bird-language/

def translate(text: str) -> str:
    vowels = [
        'a',
        'e',
        'i',
        'o',
        'u',
        'y'
    ]

    translated = ""
    translation_not_complete = True
    untranslated = text
    
    while translation_not_complete:
        c_char = untranslated[0]
        translated += untranslated[0]
        if c_char in vowels:
            untranslated = untranslated[3::]
        elif c_char == ' ':
            untranslated = untranslated[1::]
        else:
            untranslated = untranslated[2::]
        if not len(untranslated):
            translation_not_complete = False
    return translated

assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"
