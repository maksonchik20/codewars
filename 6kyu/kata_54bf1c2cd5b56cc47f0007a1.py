# Count the number of Duplicates

def duplicate_count(text):
    text = text.lower()
    mnoj = set()
    for el in text:
        if text.count(el) > 1 and el not in mnoj:
            mnoj.add(el)
    return len(mnoj)

print(duplicate_count('Indivisibilities'))