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