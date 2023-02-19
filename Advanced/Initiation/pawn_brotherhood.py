# Naomi Tesla
# https://py.checkio.org/en/mission/pawn-brotherhood/

def safe_pawns(pawns: set) -> int:
    safe = 0
    for pawn in pawns:
        right_diag = '{}{}'.format(
            chr(ord(str(pawn[0]))+1), str(int(pawn[1])-1))
        left_diag = '{}{}'.format(
            chr(ord(str(pawn[0]))-1), str(int(pawn[1])-1))
        if left_diag in pawns or right_diag in pawns:
            safe += 1
    return safe


assert safe_pawns({"d2", "f4", "d4", "b4", "e3", "g5", "c3"}) == 6
assert safe_pawns({"f4", "g4", "d4", "b4", "e4", "e5", "c4"}) == 1
