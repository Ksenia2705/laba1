numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index = numbers.index(None)
dlina = len(numbers)
summa = sum(numbers[:index]) + sum(numbers[(index+1):])
new = summa / dlina
numbers[index] = new

print("Измененный список:", numbers)
