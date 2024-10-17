def all_variants(text):
    for x in range(len(text)):
        for y in range(len(text) - x):
            yield text[y:y+x+1]







# Пример использования
a = all_variants("abc")
for i in a:
    print(i)

