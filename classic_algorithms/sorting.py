

def insert_sorted(elem, array):
    if elem < array[0]:
        return array
    else:
        array.append(elem)
r        return sorted(array, reverse=True)

