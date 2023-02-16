# Naomi Tesla
# https://py.checkio.org/en/mission/non-unique-elements/
# Not the most efficient but I kinda just wanted to do it from scratch without importing 3rd party stufffff :3


from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    occurence_count = {}

    for item in data:
        occurence_count[item] = occurence_count.get(item, 0) + 1

    for item, count in occurence_count.items():
        if count == 1:
            data.pop(data.index(item))

    return data