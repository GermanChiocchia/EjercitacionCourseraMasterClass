def even_numbers(x):
    for i in range(x):
        if i%3 == 0:
            yield i

print(list(even_numbers(9)))