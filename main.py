class House:
    def __init__(self, name, number_of_flors):
        self.name = name
        self.number_of_flors = number_of_flors

    def go_to(self, new_floor):
        if new_floor > self.number_of_flors or new_floor < 1:
            print ('такого этажа не существует')
        else:
            #print(f'надо приехать на {new_floor} этаж') #как вариант прописать куда ехать вместо перечисления каждого этажа
            for floor in range (1, new_floor + 1):
                print (floor)



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

