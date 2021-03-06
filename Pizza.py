import random
from tkinter import BooleanVar, Text, scrolledtext, Menu, messagebox
import tkinter
from tkinter.ttk import Label, Checkbutton, Menubutton, Button

delivery_charge = 3.00
# list of dictionaries (pizzas) with name and price
pizzas_available = (
    {"name": "Hawaiian", "price": 8.5},
    {"name": "Meat Lovers", "price": 8.5},
    {"name": "Pepperoni", "price": 8.5},
    {"name": "Ham & Cheese", "price": 8.5},
    {"name": "Classic Cheese", "price": 8.5},
    {"name": "Veg Hot 'n' Spicy", "price": 8.5},
    {"name": "Beef & Onion", "price": 8.5},
    {"name": "Seafood Deluxe", "price": 13.5},
    {"name": "Summer Shrimp", "price": 13.5},
    {"name": "BBQ Bacon & Mushroom", "price": 13.5},
    {"name": "BBQ Hawaiian", "price": 13.5},
    {"name": "Italiano", "price": 13.5},
)

toppings = {
    "Pepperoni":0.9,
    "Mushrooms":1.6,
    "Onions":0.2,
    "Bacon":1.5,            
    "Extra cheese":2.1,
    "Black olives":1.7,
    "Green pepper":2.1
}

sauces = {
    "Tomato":1.9,
    "Garlic":1.6,
    "Chilly":3.2
}

class Order(object):

    def __init__(self, name, address, pickup):
        self.name = name;
        self.address = address
        self.pickup = pickup
        self.pizzas = []
        
    def add_pizza(self, newPizza):
        if(len(self.pizzas)>0):
            for pizza in self.pizzas:
                if(not pizza.get_name() == newPizza.get_name()):
                    self.pizzas.append(newPizza)
        else:
            self.pizzas.append(newPizza)
    def remove_pizza(self, name):
        for pizza in self.pizzas:
                if(pizza.get_name() == name):
                    del pizza
                    
    def get_pizza(self, name):
        for pizza in self.pizzas:
                if(pizza.get_name() == name):
                    return pizza;
        return None
    def get_pizzas(self):
        return self.pizzas
    
    def get_address(self):
        return self.address
    
    def get_name(self):
        return self.name
    
    def is_pickup(self):
        return self.pickup

    def set_name(self, name):
        self.name = name
    
    def set_address(self, address):
        self.address = address
    
    def set_pickup(self, pickup):
        self.pickup = pickup



class Pizza(object):

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.sauces = []
        self.toppings = []
        
    def get_name(self):
        return self.name
    
    def get_sauces(self):
        return self.sauces
    
    def get_toppings(self):
        return self.toppings;
    
    def add_topping(self, topping):
        if(topping not in self.toppings):
            self.toppings.append(topping)
    def remoce_topping(self, topping):
        if(topping  in self.toppings):
            del self.toppings[topping]
            
    def add_sause(self, sause):
        if(sause not in self.sauces):
            self.sauces.append(sause)
    def remove_sause(self, sause):
        if(sause  in self.sauces):
            del self.sauces[sause]
    def get_cost(self):
        return self.cost

def addPizza(order, name,price):
    pizza=Pizza(name,price)    
    order.add_pizza(pizza)
    price=0;
    for pizza in order.get_pizzas():
        price+=pizza.get_cost()
        for sause in pizza.get_sauces():
            price+=sauces[sause]
        for topping in pizza.get_toppings():
            price+=toppings[topping]
    info=order.get_name()+" cost is $"+str(price)
    messagebox.showinfo('Order Cost',info)

def removePizza(order, name):
    order.remove_pizza(name)
    price=0;
    for pizza in order.get_pizzas():
        price+=pizza.get_cost()
        for sause in pizza.get_sauces():
            price+=sauces[sause]
        for topping in pizza.get_toppings():
            price+=toppings[topping]
    info=order.get_name()+" cost is $"+str(price)
    messagebox.showinfo('Order Cost',info)

def placeOrder(order,name,isPickup,address):
    order.set_pickup(isPickup)
    order.set_name(name)
    order.set_address(address)
    errors=""
    if( order.get_name().strip()=="") :
        errors+="Name to order is required\n" 
    if(not order.is_pickup() and order.get_address().strip()=="") :
        errors+="Address to order is required to non pickup orders\n" 
    if(len(order.get_pizzas())==0):
        errors+="Pizza is not selected to order\n" 
        
    if(not errors==""):
        messagebox.showerror('Errors',errors)
    else:
        price=0;
        
        for pizza in order.get_pizzas():
            price+=pizza.get_cost()
            for sause in pizza.get_sauces():
                price+=sauces[sause]
            for topping in pizza.get_toppings():
                price+=toppings[topping]
        info="Name:"+order.get_name()+ "\n"
        info+="Address:"+order.get_address()+"\n"
        info+="Pickup:"
        if(order.is_pickup):
            info+="Yes\n"
        else:
            info+="No\n"
         
        info+=" Total Cost of order: $"+str(price)
        messagebox.showinfo('Order Cost',info)
        messagebox.showinfo('Order Delivery Time',str(random.randint(15,25))+" minutes")

def updateToppings(order,name,topping):
    pizza=order.get_pizza(name)
    if(None==pizza):
        pass
        #messagebox.showinfo('Error',"First Add the pizza,then add toppings")
    else:
        if(topping not in pizza.get_toppings()):
            pizza.add_topping(topping)
        else:
            pizza.remove_topping(topping)
        price=pizza.get_cost()
        
        for sause in pizza.get_sauces():
            price+=sauces[sause]
            
        for topping in pizza.get_toppings():
            price+=toppings[topping]
            
        info=name+" cost is $"+str(price)
        messagebox.showinfo('Pizza Cost',info)

def updatesauces(order,name,sause):
    pizza=order.get_pizza(name)
    if(None==pizza):
        pass
    else:
        if(sause not in pizza.get_sauces()):
            pizza.add_sause(sause)
        else:
            pizza.remove_sause(sause)
        
        price=pizza.get_cost()
        
        for sause in pizza.get_sauces():
            price+=sauces[sause]
        
        for topping in pizza.get_toppings():
            price+=toppings[topping]
        
        info=name+" cost is $"+str(price)
        messagebox.showinfo('Pizza Cost',info)

if __name__ == '__main__':      
    window = tkinter.Tk()
    window.title("Pizza Ordering System")
    window.geometry('650x600')
    r = 0
    lbl = Label(window, text="Name:")
    lbl.grid(column=0, row=r)    
    nameText = Text(window, width=30, height=1.5)
    nameText.grid(column=1, row=r)
    r += 1
    
    lbl = Label(window, text="Address:")
    lbl.grid(column=0, row=r)    
    address = scrolledtext.ScrolledText(window, width=30, height=5)
    address.grid(column=1, row=r)
    r += 1
    
    chk_state = BooleanVar()
    chk_state.set(False)  # set check state
    chk = Checkbutton(window, text='Pickup', var=chk_state) 
    chk.grid(column=0, row=r)
    r += 1
    
    order = Order("", "", "");
    window.grid_rowconfigure(10, weight=0)
   
    for i in range(len(pizzas_available)):
        pizza = pizzas_available[i];
        name = pizza["name"]
        price = pizza["price"]
        Label(text=name, width=10).grid(row=r, column=0)
        
        mb = Menubutton (text="")
        mb.grid(row=r, column=1)
        mb.menu = Menu (mb, tearoff=0)
        mb["menu"] = mb.menu
        
        for key,value in toppings.items():
            mb.menu.add_checkbutton(label=key, variable=key,command=lambda:updateToppings(order,name,key))
        
        smb = Menubutton (text="")
        smb.grid(row=r, column=2)
        smb.menu = Menu (smb, tearoff=0)
        smb["menu"] = smb.menu
        
        for key1,value in sauces.items():
            smb.menu.add_checkbutton(label=key1, variable=key1,command=lambda:updatesauces(order,name,key1))
        
        btn = Button(text="Add", command=lambda:addPizza(order,name,price))
        btn.grid(row=r, column=3);
        btn = Button(text="Remove", command=lambda:removePizza(order, name))
        btn.grid(row=r, column=4);
        r = r + 1
    btn = Button(text="Place Order", command=lambda:placeOrder(order,nameText.get("1.0","end-1c"),chk_state.get(),address.get("1.0","end-1c")))
    btn.grid(row=r, column=0)
    window.mainloop()