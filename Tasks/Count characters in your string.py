def count(string):
    res = {}
    my_set = set(string)
    for sym in my_set:
        res[sym] = string.count(sym)
    return res

print(count('aba'))
