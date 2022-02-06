def get_count(sentence):
    count = 0
    vowels = ['a', 'e','i', 'o','u']
    for sym in sentence:
        if sym in vowels:
            count += 1
    return count

print(get_count('aeiouddd'))
