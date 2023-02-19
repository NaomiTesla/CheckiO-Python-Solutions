# Naomi Tesla
# https://py.checkio.org/en/mission/between-markers/
# def could be made more efficient

def between_markers(text: str, begin: str, end: str) -> str:
    if [text.find(begin), text.find(end)] == [-1, -1]:
        return text
    elif text.find(begin) == -1:
        return "No"
    elif text.find(end) == -1:
        return text[text.index(begin)+len(begin):]
    else:
        return text[text.index(begin)+len(begin):text.index(end)]


assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>",
                    "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""
