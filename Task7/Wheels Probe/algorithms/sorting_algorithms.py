def bubble_sort(data, attribute):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][attribute] > data[j + 1][attribute]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data
def quick_sort(data, attribute):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2][attribute]
    left = [x for x in data if x[attribute] < pivot]
    middle = [x for x in data if x[attribute] == pivot]
    right = [x for x in data if x[attribute] > pivot]
    return quick_sort(left, attribute) + middle + quick_sort(right, attribute)
