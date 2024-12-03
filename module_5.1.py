class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        for i in range(1, (new_floor + 1)):
            if new_floor <= self.number_of_floor:
                print(i)
            else:
                print("Такого этажа не существует!")
                break
        if new_floor <= 0:
            print("Такого этажа не существует!")
            pass

h1 = House('ЖК Горский', 18)
h2 = House('домик в деревне', 2)
h3 = House('ЖК Новые ватутинки', 17)
h1.go_to(5)
h2.go_to(11)
h3.go_to(-12)

