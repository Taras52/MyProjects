# время ответа - 23.01.18 в 21:56

mass = [1, 2, 12, 20, 24]
cube_list = [n ** 3 for n in mass if n % 3 == 0 and n % 4 == 0]
print(cube_list)