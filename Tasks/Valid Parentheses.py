def valid_parentheses(string):
    res = ''.join([sym for sym in string if sym =='(' or sym == ')'])
    while '()' in res:
        res = res.replace('()', '')
    if len(res) == 0:
        return True
    else:
        return False

# def valid_parentheses(string):
#     string = "".join(ch for ch in string if ch in "()")
#     while "()" in string: string = string.replace("()", "")
#     return not string

print(valid_parentheses('((())()())'))
