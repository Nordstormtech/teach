# Wizard
# Warrior
# Paladin
import sys


class Base:
    def __init__(self, health):
        self.health = health

    def go_to(self):
        print("go_to")

    def get_damaged(self):
        self.health -= 10
        print("get_damaged")

    def restore_health(self):
        self.health += 10
        print("restore_health")


class Wizard(Base):
    def __init__(self, health=100):
        super().__init__(health)

    def get_damaged(self):
        self.health -= 20
        print("health:", self.health)


class Warrior(Base):
    pass


class Paladin(Base):
    def __init__(self, health=200):
        super().__init__(health)

    def restore_health(self):
        self.health += 20
        print("health:", self.health)


print(issubclass(Paladin, Base))
a = Paladin()
# print(issubclass(a, Base)) - Error
print(sys.getsizeof(a))
print(sys.getsizeof(Paladin))
