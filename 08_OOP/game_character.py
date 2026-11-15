class Character:
    def _init_(self, name, health):
        self.name = name
        self.health = health

    def display(self):
        print("Name:", self.name)
        print("Health:", self.health)


class Warrior(Character):
    def attack(self):
        print(self.name, "uses Sword Attack")


class Wizard(Character):
    def attack(self):
        print(self.name, "uses Magic Attack")


class Archer(Character):
    def attack(self):
        print(self.name, "uses Bow Attack")


w = Warrior("Warrior", 100)
m = Wizard("Wizard", 80)
a = Archer("Archer", 90)

w.display()
w.attack()

m.display()
m.attack()

a.display()
a.attack()
