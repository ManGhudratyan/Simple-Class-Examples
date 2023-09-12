class Car:
    def __init__(self, model, color, year):
        self.model = model;
        self.color = color;
        self.year = year;
        
    def start(self):
        print(f"The eleventh-generation {self.model} was released in {self.year}.");
        
    def get_info(self):
        return f"Car Model: {self.model}\nColor: {self.color}\nYear: {self.year}";
    
    def change_color(self, new_color):
        self.color = new_color;
        print(f"The car's color is now {new_color}.");

    def brake(self):
        print(f"The {self.model} is braking.");
    

myCar = Car('Civic', 'grey', 2021);
myCar.start();
print("\nCar Information:");
print(myCar.get_info());
myCar.change_color('blue');
myCar.brake();
