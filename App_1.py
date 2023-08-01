# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

def find_duplicates(elements):
    """The function finds duplicates"""
    unique_elements = set()
    duplicates = set()

    for elem in elements:
        if elem in unique_elements:
            duplicates.add(elem)
        else:
            unique_elements.add(elem)

    return list(duplicates)


elements = [1, 2, 3, 1, 2, 4, 5]
result = find_duplicates(elements)
print(result)
