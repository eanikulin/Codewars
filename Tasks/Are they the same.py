
def comp(array1, array2):
    count = 0
    for i in array2:
        if int(i**(0.5)) in array1:
            count += 1
    if count == len(array1):
        return True
    return False

# try:
#     return True if sorted([i * i for i in array1]) == sorted(array2) else False
# except:
#     return False


a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp(a, b))

