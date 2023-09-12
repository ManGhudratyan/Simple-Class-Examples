class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def jump_height(self, height_cm):
        print(f"The world record for the highest {self.name} jump is {height_cm} centimeters.")

    def move(self):
        print(f"{self.name} is jumping")

    def eat(self, food):
        print(f"{self.name} is eating {food}")

    def sleep(self, hours):
        print(f"{self.name} is sleeping for {hours} hours.")

rabbit = Animal("Rabbit", "Sylvilagus")

rabbit.jump_height(107)
rabbit.move()
rabbit.eat("carrot")
rabbit.sleep(4)


