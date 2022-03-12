import string


def is_pangram(s):
    count = 0
    s = " ".join(s.split())
    s = set(s.lower())
    for i in s:
        if i in string.ascii_letters:
            count += 1
    return True if count == 26 else False


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
