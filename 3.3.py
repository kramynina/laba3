# Класс Хэш-таблицы
class HashTable:
    # Функция инициализации необходимых параметров
    def __init__(self):
        # Задаём длину нашей хэш-таблицы
        self.size = 11
        # Создаем список для хранения ключей
        self.slots = [None] * self.size
        # Создаем список для хранения значений
        self.data = [None] * self.size

    # Функция добавления ключа и значения в список
    def put(self, key, data):
        # Получаем ячеку хэша для ключа и значения
        hashvalue = self.hash(key, len(self.slots))
        # Если ячейка хэш-таблицы пуста
        if self.slots[hashvalue] is None:
            # Кладём ключ в ячейку
            self.slots[hashvalue] = key
            # Кладём значение в ячейку
            self.data[hashvalue] = data
        else:
            # Иначе если ключ уже находится в ячейке
            if self.slots[hashvalue] == key:
                # Заменяем значение ячейки хэш-таблицы
                self.data[hashvalue] = data
            else:
                # Иначе если ячека хэша не пуста и не содержит ключ
                # Ищем новое значние хэша с помощью линейного пробирования
                nextslot = self.rehash(hashvalue, len(self.slots))
                # Пока значение по новому хэшу ячейки ключей не является пустым и не равно ключу
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    # Ищем новое значние хэша с помощью линейного пробирования
                    nextslot = self.rehash(nextslot, len(self.slots))
                # Если ячейка хэш-таблицы пуста
                if self.slots[nextslot] is None:
                    # Кладём ключ в ячейку
                    self.slots[nextslot] = key
                    # Кладём значение в ячейку
                    self.data[nextslot] = data
                else:
                    # Иначе заменяем значение ячейки хэш-таблицы
                    self.data[nextslot] = data

    # Функция создания хэш-значения
    def hash(self, key, size):
        return key % size

    # Функция создания хэш-значения с помощью линейного пробирования
    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    # Функция получения ключа и значения из списока
    def get(self, key):
        # Получаем хэш ячейки по ключу и сохраняем как первую позицию
        startslot = self.hash(key, len(self.slots))
        # Создаем переменные для цикла
        # Будет содрежать значение ячейки хэш-таблицы по ключу
        data = None
        # Означает, что необходимая информация не найдена
        stop = False
        # Означает, что цикл не остановлен
        found = False
        # Берем позицию стартовой ячейки
        position = startslot
        # Пока значение ячейки ключа не является пустым и не найдено значение и цикл не остановлен
        while self.slots[position] is not None and not found and not stop:
            # Если ключ в ячейке равен искомому ключу
            if self.slots[position] == key:
                # останавливаем цикл
                found = True
                # получаем значение в ячеке хэш-таблицы
                data = self.data[position]
            else:
                # Иначе если ключи не равны
                # Ищем следующуюю ячеку
                position = self.rehash(position, len(self.slots))
                # Если полученный хэш ячейки равен хэшу стартовой ячейки
                if position == startslot or self.slots[position] is None:
                    # Отправим сообщение о ненахождении значения по ключу
                    data = "Ключ не найден!"
                    # останавливаем цикл
                    stop = True
        # Возвращаем значение ячейки хэш-таблицы по ключу
        return data


#if __name__ == '__main__':
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
