# return masked string

def maskify(cc):
    str = ''
    for char in cc[:-4]:
        str += '#'
    str += cc[-4:]
    return str

# print(maskify('22616'))


sdf = '123456789'
print(sdf[1:3])

