class egehan:
    x=5
ege = egehan()
print(ege.x)

class car:

    def __init__(self,name,brand, year):
        self.name = name
        self.brand = brand
        self.year = year

    def trial(self):
        print("The name of my  car is", self.name,"brand is",self.brand, "and the age is", self.year)


class anan(car):
    def __init__(self, balata):
       super().__init__(balata)
       self.balata = balata
    def __str__(self):
        return f"{self.balata, self.name, self.brand, self.year}"
p3= anan("burak", "audi", "31", "teyzen" )
print(p3)