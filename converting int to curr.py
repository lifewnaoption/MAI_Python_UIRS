def to_currency(price):
    nums = list(str(price))
    nums = nums[::-1]
    i = 0
    three = 0
    while i < len(nums):
        if (nums[i] != ','):
            three += 1
        if three == 4:
            nums.insert (i, ',')
            three = 0
        i += 1
    res = ''.join(nums[::-1])
    return res

print(to_currency(123456789))


