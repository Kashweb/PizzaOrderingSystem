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
