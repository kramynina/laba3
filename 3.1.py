# Класс Хэш-таблицы
class HashTable:
    # Функция инициализации списков
    def __init__(self):
        # Задаём длину нашей хэш-таблицы
        self.size = 11
        # Создаем список для хранения ключей
        self.slots = [()] * self.size
        # Создаем список для хранения значений
        self.data = [()] * self.size

    # Функция добавления ключа и значения в список
    def put(self, key, data):
        # Получаем ячейку хэша для ключа и значения
        hashvalue = self.hash(key, len(self.slots))
        # Если ячейка хэш-таблицы пуста
        if self.slots[hashvalue] is ():
            # Добавляем ключ в ячейку
            self.slots[hashvalue] = (key, )
            # Добавляем значение в ячейку
            self.data[hashvalue] = (data, )
        else:
            # Иначе если ключ уже находится в ячейке
            if key in self.slots[hashvalue]:
                # Получаем индекс ключа в ячейке хэша
                index = self.slots[hashvalue].index(key)
                # Формируем список элементов ячейки
                lst = list(self.data[hashvalue])
                # Изменяем значение ключа
                lst[index] = data
                # Сохраняем изменение
                self.data[hashvalue] = tuple(lst)
            else:
                # Иначе если ячейка хэша не пуста и не содержит ключ
                # Формируем список элементов ячейки ключей
                list_slots = [elem for elem in self.slots[hashvalue]]
                # Добавляем ключ в ячейку
                list_slots.append(key)
                # Сохраняем изменение
                self.slots[hashvalue] = tuple(list_slots)
                # Формируем список элементов ячейки значений
                list_data = [elem for elem in self.data[hashvalue]]
                # Добавляем значение в ячейку
                list_data.append(data)
                # Сохраняем изменение
                self.data[hashvalue] = tuple(list_data)

    # Функция создания хэш-значения
    def hash(self, key, size):
        return key % size

    # Функция получения значения по ключу из хэш-таблицы
    def get(self, key):
        # Получаем хэш ячейки по ключу и сохраняем как первую позицию
        startslot = self.hash(key, len(self.slots))
        # Создаем переменные для цикла
        # Будет содержать значение ячейки хэш-таблицы по ключу
        data = None
        # Означает, что необходимая информация не найдена
        found = False
        # Означает, что цикл не остановлен
        stop = False
        # Берем позицию стартовой ячейки
        position = startslot
        # Пока значение ячейки ключа не является пустым кортежем и не найдено значение и цикл не остановлен
        while self.slots[position] is not () and not found and not stop:
            # Если ключ в ячейке
            if key in self.slots[position]:
                # останавливаем цикл
                found = True
                # получаем индекс ключа в ячейке хэш-таблицы
                index = self.slots[position].index(key)
                # получаем значение в ячейке хэш-таблицы по полученному индексу
                data = self.data[position][index]
            else:
                # Иначе если ключ не в ячейке
                # Ищем следующую ячейку
                position = self.hash(position, len(self.slots))
                # Если полученная ячейка равна стартовой ячейке
                if position == startslot:
                    # Отправим сообщение о ненахождении значения по ключу
                    data = "Ключ не найден!"
                    # останавливаем цикл
                    stop = True
        # Возвращаем значение ячейки хэш-таблицы по ключу
        return data


if __name__ == "__main__":
    # Создаём объект класса HashTable
    HT = HashTable()
    # Вносим данные в хэш-таблицу
    HT.put(218, "BMW 2 SERIES GRAN COUPE 218i")
    HT.put(5, "BMW M5")
    HT.put(3, "BMW M3")
    HT.put(420, "BMW 4 SERIES GRAN COUPE 420i")
    HT.put(430, "BMW 4 SERIES GRAN COUPE 430i")
    HT.put(440, "BMW 4 SERIES GRAN COUPE 440i")
    HT.put(530, "BMW 5 SERIES GT 530i")
    HT.put(8, "BMW I8")
    HT.put(320, "BMW 3 SERIES GT 320i")
    # Выводим полученные списки
    print(HT.slots)
    print(HT.data)
    # Получим значения по следующим ключам
    print(HT.get(320))
    print(HT.get(430))
    # Заменим значение ключа 430
    HT.put(430, "LADA GRANTA")
    # Выводим полученные списки
    print(HT.slots)
    print(HT.data)
    # Получим значения по следующим ключам
    print(HT.get(430))
    print(HT.get(1))
