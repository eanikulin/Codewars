def narcissistic(value):
    len_dig = len(str(value))
    res_lst = []
    res_num = value

    while (value > 0):
        lst_dig = value % 10
        res_lst.append(lst_dig)
        value = value // 10
    res = sum([x ** len_dig for x in res_lst])
    if res == res_num:
        return True
    else:
        return False


narcissistic(153)

# test.assert_equals(narcissistic(7), True, '7 is narcissistic');
# test.assert_equals(narcissistic(371), True, '371 is narcissistic');
# test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
# test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')
