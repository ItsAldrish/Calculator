def addition(nums):
    sum = 0
    sum_string = ""

    for index, num in enumerate(nums):
        sum += num
        if index == len(nums) - 1:
            sum_string += f"{num} = {sum}"
        else:
            sum_string += f"{num} + "

    return sum_string


def subtraction(nums):
    dif = 0
    dif_string = ""

    for index, num in enumerate(nums):
        dif -= num
        if index == len(nums) - 1:
            dif_string += f"{num} = {dif}"
        else:
            dif_string += f"{num} - "

    return dif_string
