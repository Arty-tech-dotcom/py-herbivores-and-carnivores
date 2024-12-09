class Animal:
    alive = []

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __str__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def die(self):
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target):
        if not isinstance(target, Herbivore) or target.hidden:
            return

        target.health -= 50
        if target.health <= 0:
            target.die()