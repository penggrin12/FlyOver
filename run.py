from game import run
from os import system

system("cls")

infFuel = input("Infinity Fuel (0/1) > ")

if infFuel == "1":
    infFuel = True
else:
    infFuel = False

run(infFuel)