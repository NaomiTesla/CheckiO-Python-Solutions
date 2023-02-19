# Naomi Tesla
# https://py.checkio.org/en/mission/x-o-referee/

from typing import List


def checkio(game_result: List[str]) -> str:
    game = [
        list(game_result[0]),
        list(game_result[1]),
        list(game_result[2]),
        [game_result[0][0], game_result[1][1], game_result[2][2]],
        [game_result[0][2], game_result[1][1], game_result[2][0]],
        [game_result[0][0], game_result[1][0], game_result[2][0]],
        [game_result[0][1], game_result[1][1], game_result[2][1]],
        [game_result[0][2], game_result[1][2], game_result[2][2]]
    ]

    for row in game:
        result = set(row)
        victor = next(iter(result))
        if len(result) == 1 and victor != '.':
            return victor
    return 'D'


assert checkio(["X.O", "XX.", "XOO"]) == "X", "X wins"
assert checkio(["OO.", "XOX", "XOX"]) == "O", "O wins"
assert checkio(["OOX", "XXO", "OXX"]) == "D", "Draw"
assert checkio(["O.X", "XX.", "XOO"]) == "X", "X wins again"
