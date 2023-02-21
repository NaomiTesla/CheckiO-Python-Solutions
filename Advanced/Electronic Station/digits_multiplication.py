# Naomi Tesla
# https://py.checkio.org/en/mission/digits-multiplication/

def checkio(number: int) -> int:
    return eval(str([int(i) for i in str(number) if int(i)]).replace(',', '*'))[0]


assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1
