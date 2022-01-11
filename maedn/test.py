class Car():
    price = "cheap"
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def bla(self):
        return self.brand + " " + self.model
    
class FCar(Car):
    price = "expensive"
    def __init__(self, brand, model, owner):
        super().__init__(brand, model)
        self.owner = owner
    
    def bla(self):
        return super().bla() + " owned by " + self.owner
    
parkingLot = [
    Car("Opel", "Corsa"),
    FCar("Ford", "Angila", "Arthur Weasley"),
    FCar("Fiat", "Panda", "Ich"),
    Car("Tesla", "Model S")
]

def xrlwyzz():
    print("qufzdibufz")