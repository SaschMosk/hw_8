class Animals:
    habitat = "land"
    lungs = True
    age = 0  # лет
    babys = 0  # количество потомков
    size = 0  # условный размер животного, в дециметрах
    weight = 0  # вес животного в кг

    def init_size(self):
        s = input('Введите размер животного, в дм:')
        self.size += int(s)
        return self.size

    def init_weight(self):
        w = input('Введите вес животного, в кг:')
        self.weight += int(w)

    def eat(self):
        float(self.age)
        self.age += 0.05
        self.weight += 0.2
        print('Теперь возраст: ', self.age)

    def sleep(self):
        float(self.age)
        self.age += 0.07
        self.size += 0.1
        print('Теперь возраст:', self.age)


class Birds (Animals):
    legs = 2
    wings = True
    beak = True
    eggs = 0

    def lay_an_egg(self):
        import random
        self.eggs += random.randint(1, 7)

    def hatch_an_egg(self, eggs):
        if self.eggs != 0:
            self.babys += (eggs - 2)
        else:
            print('Ещё не готова!')


class Mammals (Animals):
    legs = 4
    wings = False
    beak = False

    def reproduction(self):
        self.babys += 1


class Cow(Mammals):
    color = 'black&white'

    @staticmethod
    def hear():
        return "Muuuu"

    @staticmethod
    def give_milk():
        print("Получено random.int(20, 40) литров молока")


class Goat(Mammals):
    color = 'gray'

    @staticmethod
    def hear_goat():
        return 'Meeee'


class Sheep(Mammals):
    color = 'white'

    @staticmethod
    def hear():
        return 'Beeee'


class Pig(Mammals):
    color = 'pink'

    @staticmethod
    def hear():
        return 'Chryu'


class Duck(Birds):
    color = 'green'

    @staticmethod
    def hear():
        return 'Krya'

    @staticmethod
    def swim_in_pond():
        print("Утка плавает в пруду...")


class Chicken(Birds):
    color = 'brown'

    @staticmethod
    def hear():
        return'Kud-Kudach'


class Goose(Birds):
    color = 'gray&blu'

    @staticmethod
    def hear():
        return 'Ga-ga-ga'

