# Задача №1
from time import sleep


class TrafficLight:
    color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


t = TrafficLight()
t.running()

 #  Задача №2
class Road:
    def __init__(self,lenght,widht,mas,tol):
        self.lenght=20
        self.widht=5000
        self.mas=25
        self.tol=5
    def asfalt (self):
        asfalt=self.lenght*self.widht*self.mas*self.tol/1000
        print(f"Для покрытия дороги необходимо {round(asfalt)} тонн асфальта")
i=Road(20,5000,25,5)
i.asfalt()

# Задача №3
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]


p = Position("Марина", "Петрова", "КТР", 2000, 5000)
print(p.get_full_name())
print(p.get_total_income())

 #Задача 5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())


