from abc import ABC
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart=Order()
    
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self,restaurant,item_name,quantity):
        item=restaurant.menu.find_item(item_name)
        if item:
            if quantity>item.quantity:
                print("Item quantity exceeded!!!") 
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print("Item Added!! ")
        else:
            print(f" Sorry {item_name} not found!!!")

    def view_cart(self):
        print("*******View Cart*******")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name} {item.price} {quantity}")
        print(f"Total Price: {self.cart.total_price()}")

class Order:
    def __init__(self):
        self.items={}
    def add_item(self,item): 
        if item in self.items: #jodi items er moddhe  item(name,price,quantity diye object)ta thake tahole shodhu quantity add hobe. 
            self.items[item]+=item.quantity
        else:
            self.items[item]=item.quantity

    def remove(self,item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(item.price*quantity for item,quantity in self.items.items())
    
    def clear(self):
        self.items={}


class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary

    
class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        
    
    def add_employee(self,restaurant,employee): #এখানে restaurant,employee নামের দুটি অবজেক্ট পাস করা হয়েছে এগুলো যথাক্রমে Restaurant Employee ক্লাসের, যে অবজেক্ট আমাদের বানিয়া পাস করাতে হবে। restaurant হচ্ছে  Restaurant class এর অবজেক্ট আর employee হচ্ছে  Employee ক্লাসের অবজেক্ট। 
       restaurant.add_employee(employee)
    
    def view_employee(self,restaurant):
        restaurant.view_employee()
    def add_new_item(self,restaurant,item):
        restaurant.menu.add_menu_item(item)
    def remove_item(self,restaurant,item):
        restaurant.menu.remove_item(item)
       
            
class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees=[]
        self.menu=Menu()
      
    def add_employee(self,employee):
        self.employees.append(employee)
    def view_employee(self):
        for em in self.employees:
            print(f"Name: {em.name},Phone: {em.phone}") 

class Menu:
    def __init__(self):
        self.items=[]
    
    def add_menu_item(self,item): #এখানে item নামের অবজেক্ট আসবে যেখানে name,price,quantity থাকবে। অন্য ক্লাস(FoodItem) বানিয়ে সেটার অবজেক্ট বানাবো। তারপর item এ পাস করবো। 
        self.items.append(item)

    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower()==item_name.lower():
                return item
        return None
    
    def remove_item(self,item_name):
        item= self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"{item_name} Delete Successfully!")
        else:
            print(f"{item_name} Could not find in the menu.")
    def show_menu(self):
        print("*********Menu**********")
        print("=======================")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")
        
class FoodItem:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

mamar_restaurant=Restaurant('Mamar Restaurant')
mn=Menu()
item=FoodItem("pizza",500,15)
item2=FoodItem("burger",250,15)
admin=Admin('Rafi',1232,'rafi@gmail.com','dhaka')
admin.add_new_item(mamar_restaurant,item)
admin.add_new_item(mamar_restaurant,item2)

customer1=Customer('Rafi',1232,'rafi@gmail.com','dhaka')
customer1.view_menu(mamar_restaurant)

item_name=input("Enter item name: ")
item_quantity=int(input("Enter item Quantity: "))
customer1.add_to_cart(mamar_restaurant,item_name,item_quantity)
customer1.view_cart()
           
        
            
