def count(phrase):
    lower = 0
    upper = 0

    for letter in phrase:
        if letter.islower():
            lower += 1
        elif letter.isupper():
            upper += 1
    return (lower, upper)

print(count('The quick Brown Fox')) # (12, 3)
