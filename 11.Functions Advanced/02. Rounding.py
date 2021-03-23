def round_values(nums_list):
    result = [round(float(el)) for el in nums_list]
    return result


number = [el for el in input().split()]
print(round_values(number))
