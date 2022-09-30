# Совершите десятиминутную прогулку
def is_valid_walk(walk):
    walk = "".join(walk)
    if len(walk) == 10:
        if walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')   :
            return True
    return False
