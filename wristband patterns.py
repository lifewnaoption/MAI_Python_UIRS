def is_wristband(arr):
    note = {1, 2, 3, 4}
    for i, j in zip(arr, arr[1:]):
        if 1 in note and (len(set(i)) != 1 or len(set(j)) != 1):
            note.remove(1)
        if 2 in note and i != j:
            note.remove(2)
        if 3 in note and i[:-1] != j[1:]:
            note.remove(3)
        if 4 in note and j[:-1] != i[1:]:
            note.remove(4)
        if not note:
            return False
    return True