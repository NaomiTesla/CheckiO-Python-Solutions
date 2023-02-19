# Naomi Tesla
# https://py.checkio.org/en/mission/time-converter-12h-to-24h/
# Very manual conversion of 12hr to 24hr that's clear without imports

def time_converter(time):
    if len(time) == 9:
        time = "0" + time

    twelve_flag = time[:2] == "12"
    am_flag = "a" in time
    time = time[:5]

    if twelve_flag and am_flag:
        return "00" + time[2:]
    elif twelve_flag and not am_flag:
        return "12" + time[2:]

    if am_flag:
        return time
    else:
        return str(12+int(time[:2])) + time[2:]


if __name__ == "__main__":
    assert time_converter("12:30 p.m.") == "12:30"
    assert time_converter("9:00 a.m.") == "09:00"
    assert time_converter("11:15 p.m.") == "23:15"
