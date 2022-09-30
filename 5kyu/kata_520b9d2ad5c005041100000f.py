# Simple Pig Latin

# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

import string


def pig_it(text):
    ret = ""
    for el in text.split():
        punctuation_not_in_el = True
        for j in el:
            if j in (string.punctuation + '!'):
                punctuation_not_in_el = False
        ret += el[1:] + el[0] + 'ay ' if punctuation_not_in_el else el + ' '
    return ret.strip()
