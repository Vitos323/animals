class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Издает звук"

    def eat(self):
        return f"{self.name} ест пищу."



class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return f"{self.name} чирикает."

    def fly(self):
        return f"{self.name} летает."


#
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return f"{self.name} рычит или мурлычет."

    def run(self):
        return f"{self.name} бегает."



class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        return f"{self.name} шипит."

    def crawl(self):
        return f"{self.name} ползет."



def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())



class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        return f"{self.name} выполняет работу."



class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "Смотритель зоопарка")

    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}."



class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}."



class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в зоопарк.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} нанят в зоопарк.")

    def show_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"- {animal.name}, {animal.age} лет")

    def show_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            print(f"- {employee.name}, {employee.position}")



parrot = Bird("Попугай", 2, "30 см")
tiger = Mammal("Тигр", 5, "Оранжевый с полосками")
snake = Reptile("Питон", 4, "Гладкая чешуя")


keeper = ZooKeeper("Иван")
vet = Veterinarian("Мария")


zoo = Zoo("Городской зоопарк")
zoo.add_animal(parrot)
zoo.add_animal(tiger)
zoo.add_animal(snake)
zoo.add_employee(keeper)
zoo.add_employee(vet)


zoo.show_animals()
zoo.show_employees()


print("\nЗвуки животных:")
animal_sound([parrot, tiger, snake])


print(keeper.feed_animal(tiger))
print(vet.heal_animal(snake))
