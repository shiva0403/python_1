def flatten(lst):
    for e in lst:
        if hasattr(e,"__iter__"):
            yield from flatten(e)
        else:
            yield e

f = flatten([1, 2, 3, [4, 5], 6, [7, 8]]) # [1, 2, 3, 4, 5, 6, 7, 8]

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
