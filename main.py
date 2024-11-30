import functions as fc

nums = []

while True:
    try:
        num = int(input("Введите число для добавления или ноль для завершения: "))

        if num == 0:
            break
        else:
            nums.append(num)
    except ValueError:
        print("Это не число")

print(fc.addition(nums))
