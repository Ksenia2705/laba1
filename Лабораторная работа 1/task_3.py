players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]


count = len(players)
mid = count//2 # индекс середины

comand_1 = players[:mid]
comand_2 = players[mid:]


print(comand_1)
print(comand_2)
