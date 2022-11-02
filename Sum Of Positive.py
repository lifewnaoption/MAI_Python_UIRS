def positive_sum(arr):
    pee = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            pee += arr[i]
    return pee