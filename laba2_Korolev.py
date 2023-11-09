class Ship:
    def __init__(self, name, length, max_speed):
        self.__name = name
        self.__length = length
        self.__max_speed = max_speed

    @property
    def name(self):
        return self.__name

    @property
    def length(self):
        return self.__length

    @property
    def max_speed(self):
        return self.__max_speed

    def display_info(self):
        pass

class Steamship(Ship):
    def __init__(self, name, length, max_speed, engine_type):
        super().__init__(name, length, max_speed)
        # super() для того, чтобы вызвать конструктор родительского класса
        # (Ship) и выполнить необходимую инициализацию родительских атрибутов.
        self.__engine_type = engine_type

    @property
    def engine_type(self):
        return self.__engine_type

    def display_info(self):
        print(f"\nТип: Пароход")
        print(f"Имя: {self.name}")
        print(f"Длина: {self.length} метров")
        print(f"Максимальная скорость: {self.max_speed} км/ч")
        print(f"Тип двигателя: {self.engine_type}")

class SailingShip(Ship):
    def __init__(self, name, length, max_speed, mast_count):
        super().__init__(name, length, max_speed)
        self.__mast_count = mast_count

    @property
    def mast_count(self):
        return self.__mast_count

    def display_info(self):
        print(f"\nТип: Парусник")
        print(f"Имя: {self.name}")
        print(f"Длина: {self.length} метров")
        print(f"Максимальная скорость: {self.max_speed} км/ч")
        print(f"Количество мачт: {self.mast_count}")

class Corvette(Ship):
    def __init__(self, name, length, max_speed, weapon):
        super().__init__(name, length, max_speed)
        self.__weapon = weapon

    @property
    def weapon(self):
        return self.__weapon

    def display_info(self):
        print(f"\nТип: Корвет")
        print(f"Имя: {self.name}")
        print(f"Длина: {self.length} метров")
        print(f"Максимальная скорость: {self.max_speed} км/ч")
        print(f"Вооружение: {self.weapon}")

def add_ship_to_registry(ship_list, ship):
    return

def display_registry_contents(ship_list):
    return

def demonstrate_skills(ship):
    return

