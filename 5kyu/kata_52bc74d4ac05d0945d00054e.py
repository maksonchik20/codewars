# Первый неповторяющийся символ

def first_non_repeating_letter(string):
    for el in string:
        if string.lower().count(el.lower()) == 1:
            return el
    return ""
    