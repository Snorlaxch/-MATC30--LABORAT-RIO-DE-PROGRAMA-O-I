def gcbr_insertion_sort(gcbr_array):
    gcbr_shifts = 0
    for gcbr_i in range(1, len(gcbr_array)):
        gcbr_key = gcbr_array[gcbr_i]
        gcbr_j = gcbr_i - 1
        while gcbr_j >= 0 and gcbr_array[gcbr_j] > gcbr_key:
            gcbr_array[gcbr_j + 1] = gcbr_array[gcbr_j]
            gcbr_shifts += 1
            gcbr_j -= 1
        gcbr_array[gcbr_j + 1] = gcbr_key
    return gcbr_shifts

# Exemplo de uso:
t = 2
casos = [
    [1, 1, 1, 2, 2],
    [2, 1, 3, 1, 2]
]
for vetor in casos:
    print(gcbr_insertion_sort(vetor[:]))  # usar [:] para não modificar o original


    