'''class selahattin:

    def __init__(self, height, weight):
        self.height=height
        self.weight=weight

    def selos(self):
        print("BMI of Selahattin is: ", self.weight/(self.height**2))
        if self.weight/(self.height**2) < 20:
            print("KILO AL AMK OLCEN")
        elif self.weight/(self.height**2) > 25:
            print("YOGAMINA")
        else:
            print("HELAL LAN")
    
    def __str__(self):
        return f"{self.height}  {self.weight}"


selo = selahattin(1.84,74.5)
selocan = selahattin(1,213)

print(selocan)
print(selo)'''

class ATM:

    def __init__(self, balance, money):
        self.balance=balance
        self.money=money

    def __str__(self):
        return f"Your current FUCKING balance is: {self.balance}, FUCKING selahattin"

    def withdraw (self):
        self.balance=self.balance-self.money
        return f"You withdrew this {self.money} FUCKING amout of money, and your new FUCKING balance is: {self.balance}"
    
    def deposit (self):
        self.balance=self.balance+self.money
        return f"You have deposited this {self.money} FUCKING amout of money, and your new FUCKING balance is: {self.balance}"
    
amounts = ATM(40, 4)
print(amounts.withdraw())
print(amounts.deposit())
print(amounts)


class circle:
    def __init__(self, radius):
        self.radius=radius

    def perimeter(self):
        per = (2*3*self.radius)
        return f"Your perimeter is: {per}"

    def area(self):
        area_circle = 3*(self.radius**2)     
        return f"Your area is: {area_circle}"   

c1= circle(31)
print(c1.perimeter())
print(c1.area())
       
class book:
    def __init__(self, title, author, publication_year):
        self.title=title
        self.author=author
        self.publication_year=publication_year
    
    def get_book_info(self):
        return f"The information regarding your book is as follows: {self.title}, {self.author}, {self.publication_year}"

b1= book("anan","teoman", 2031)
result = b1.get_book_info()
print(result)

class employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    
    def get_annual_salary(self):
        annual_salary=self.salary*12
        return f"Your annual salary is: {annual_salary}"
    
    def raise_salary(self, percentage):
        self.salary+=percentage*self.salary
        return f"Your updated salary will be: {self.salary} "

e1=employee("anan", 31)
print(e1.get_annual_salary())
print(e1.raise_salary(0.1))
print(e1.get_annual_salary())

class inventory:
    def __init__(self):
        self.items=[]
    
    def add_item(self, name, barcode, price, quantity):
        item={"name": name, "barcode": barcode, "price": price, "quantity": quantity}
        self.items.append(item)
    
    def print_inventory(self):
        return self.items

    def update_quantity(self, barcode, quantity):
        for item in self.items:
            if item["barcode"]==barcode:
                item["quantity"]+=quantity
        return
    
i1=inventory()
i1.add_item("anan", "31", 300, 45)
i1.add_item("baban", "32", 290, 40)
i1.add_item("baban", "35", 290, 43)
i1.update_quantity("69", 11)
result1 = i1.print_inventory()
print(result1)

class restaurant:
    def __init__(self, name, cousine):
        self.name=name
        self.cousine=cousine
        self.ratings=0
        self.total_ratings=0
        self.menu_items={}
    
    def add_menu_item(self, item_name, price):
        if item_name not in self.menu_items:
            self.menu_items[item_name]=price
    
    def rating_update(self,rating):
        self.ratings= (self.ratings*self.total_ratings+rating)/(self.total_ratings+1)
        self.total_ratings+=1
    
    def generate_menu(self):
        menu= f"{self.name} - {self.cousine}\n "
        for name,price in self.menu_items.items():
            menu+=f"{name}: ${price}\n"
        return menu 

r1=restaurant("La Masa", "Italian")
r1.add_menu_item("Pizza", 12.99)
r1.add_menu_item("Pasta", 7.99)
r1.add_menu_item("Pana Cotta", 10.99)
r1.add_menu_item("Pita", 4.99)
r1.rating_update(10)
r1.rating_update(9)
r1.rating_update(10)
r1.rating_update(10)
print(r1.generate_menu())
print(f"Average rating for {r1.name} is {r1.ratings}\n")

r2=restaurant("Domino's", "Pizza")
r2.add_menu_item("Margerita", 10.99)
r2.add_menu_item("Bol Malzemos", 13.99)
r2.rating_update(9)
r2.rating_update(7)
r2.rating_update(5)
print(r2.generate_menu())
print(f"Average rating for {r2.name} is {r2.ratings}")


class car:
    def __init__(self, make, model, model_year):
        self.make=make
        self.model=model
        self.model_year=model_year
        self.speed=0
    
    def brake(self):
        self.speed-=5
    
    def accelerate(self):
        self.speed+=10
    
    def current_speed(self):
        return self.speed

    def car_info(self):
        return f"Your current car's make is: {self.make}, the model is: {self.model}, and the model year is: {self.model_year}"

z1=car("Tesla", "Model Y", 2023)
z1.accelerate()
z1.accelerate()
z1.accelerate()
z1.brake()
print(z1.current_speed())
print(z1.car_info())