# Play store вернул данные с "мусором". Мусором являются единицы.
# Исправьте приведенный ниже код таким образом чтобы все условия выполнялись без ошибок.

parsed_data = [100, 1, 5, 20, 1, 25, 1, 55, 75, 1, 1, 1]

while 1 in parsed_data:
    parsed_data.remove(1)
    if 100 in parsed_data:
        parsed_data.remove(100)
        parsed_data[-1] = 100
    # здесь решение необходимо дописать
print(parsed_data)
# здесь также решение необходимо дописать

# Ниже набор тестов, менять нельзя
assert parsed_data.count(1) == 0
assert len(parsed_data) == 6
assert parsed_data == [5, 20, 25, 55, 75, 100]