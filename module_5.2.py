class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
    def __len__(self):
        return self.number_of_floor
    def __str__(self):
        return f"Название: {self.name}, количество этажей {self.number_of_floor}"

    def go_to(self, new_floor):
        for i in range(1, (new_floor + 1)):
            if new_floor <= self.number_of_floor:
                print(i)
            else:
                print("Такого этажа не существует!")
                break
            pass

h1 = House('ЖК Горский', 18)
h2 = House('домик в деревне', 2)
h3 = House('ЖК Новые ватутинки', 17)
#str
print(h1)
print(h2)
print(str(h3))

#len
print(len(h1))
print(len(h2))
print(len(h3))