# Lazy Repeater

def make_looper(string):
    def generator():
        while True:
            for char in string:
                yield char
    return generator().__next__
