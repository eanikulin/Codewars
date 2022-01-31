def square_digits(num):
    res_str = ''
    list_num = []
    len_num = len(str(num))
    for i in range(len_num):
        digit = num % 10
        num = num // 10
        list_num.append(str(digit**2))
    list_num.reverse()
    res_str = int(res_str.join(list_num))
    return res_str


print(square_digits(3212))