# Get the Middle Character

# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"

def get_middle(s):
    return s[(len(s)//2)-1:((len(s)//2) + 1)] if len(s) % 2 ==0 else s[(len(s)//2)]
