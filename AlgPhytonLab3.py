cars_mas = [["0", "Нет данных", "Нет данных"]] 
while True:
    print("ДЕЙСТВИЯ:")
    print("Выход")
    print("Добавить")
    print("Удалить")
    print("Поиск")
    print("Вывод")
    command = input("Введите действие: ")
    print()
    if command == "Выход" or command == "выход":
        break
    elif command == "Добавить" or command == "добавить":
        data = input("Введите характеристики через пробел: Номер, Бренд, Цвет: ")
        print()
        try:
            number, brand, color = data.split()
            cars_mas.append([number, brand, color])
        except:
            print("Ошибка")
            print()
    elif command == "удалить" or command == "Удалить":
        car_id = int(input("Введите порядковый номер машины: ")) #id
        if car_id < len(cars_mas):
            cars_mas.pop(car_id)
            print("УДАЛЕНО")
            print()
        else:
            print("Ошибка, введите верно номер.")
            print()
    elif command == "поиск" or command == "Поиск":
        search_by = input("По какой характеристике искать(Номер, Бренд, Модель, Цвет): ")
        if search_by == "Номер" or search_by == "номер":
            search_by = 0
        elif search_by == "Бренд" or search_by == "бренд":
            search_by = 1
        elif search_by == "Модель" or search_by == "Цвет":
            search_by = 2
        else:
            print("Такой характеристики нет")
            print()
            continue
        q = input("Введите характеристику: ")
        found = False
        for i in cars_mas:
            if i[search_by] == q:
                print(cars_mas.index(i), i)
                print()
                found = True
        if not found:
            print("Не найдено.")
            print()
    elif command == "Вывод" or command == "вывод":
        for i in cars_mas:
            print(cars_mas.index(i), i)
            print()
    elif command == "Изменить" or command == "изменить":
        car_id = int(input("Введите порядковый номер машины: "))
        if car_id < len(cars_mas):
            feature = input("Что хотите изменить: ")
            new_feature = input("Введите новое значение: ")
            if feature == "Номер" or feature == "номер":
                feature = 0
            elif feature == "Бренд" or feature == "бренд":
                feature = 1
            elif feature == "Цвет" or feature == "Цвет":
                feature = 2
            else:
                print("Нет такой характеристики")
                print()
                continue
            cars_mas[car_id][feature] = new_feature
        else:
            print("Такой машины нет")
            print()
    else:
        print("Нет такого действия")
        print()

