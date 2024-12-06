class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)


    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f"Название: {self.name}, количество этажей {self.number_of_floor}"

    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor

    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        self.number_of_floor = self.number_of_floor + value
        return House(self.name, self.number_of_floor)

    def __iadd__(self, value):
        self.number_of_floor = self.number_of_floor + value
        return House(self.name, self.number_of_floor)


    def __radd__(self, value):
        self.number_of_floor = self.number_of_floor + value
        return House(self.name, self.number_of_floor)


    def go_to(self, new_floor):
        for i in range(1, (new_floor + 1)):
            if new_floor <= self.number_of_floor:
                print(i)
            else:
                print("Такого этажа не существует!")
                break
        if new_floor <= 0:
            print("Такого этажа не существует!")



    def __del__(self):
        print(f'{self.name}, снесён, но он останется в истории')


#1 = House('ЖК Горский', 18)
#h2 = House('домик в деревне', 2)
#h3 = House('ЖК Новые ватутинки', 17)
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


# Удаление объектов
del h1
del h3


print(House.houses_history)
input()