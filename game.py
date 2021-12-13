# Импорты
from os import system
from time import sleep
import random

# Функции
def run(infFuel):
    if infFuel == True:
        IS_FUEL_INFINITY = True
        print("Cheat Mode!\nInfinity Fuel active!")
    
    game()
    
def death():
    system("cls")
    
    print("You dead!\n\nGame Over")
    sleep(10)
    exit()
    
def game():
    # Параметры
    global IS_FUEL_INFINITY
    global ENGINE
    global ALT
    global MAX_THRUST
    global YEAR
    global STEP
    global THRUST
    global SPEED
    global FUEL
    
    IS_FUEL_INFINITY = False
    ENGINE = False
    ALT = 0
    MAX_THRUST = 1500
    YEAR = 0
    STEP = 0
    THRUST = 0
    SPEED = 0
    FUEL = 10000
    
    # Цикл
    while True:
        STEP = STEP + 1
        
        fuelforce = random.randint(1,5)
        upforce = random.randint(1,5)
        if ALT > 10000:
            downforce = 0
        else:
            downforce = random.randint(1,3)
        
        if FUEL <= 0:
            ENGINE = False
        
        if (ENGINE == True) and (THRUST <= MAX_THRUST):
            THRUST = THRUST + upforce
            SPEED = SPEED + (upforce * 2)
            ALT = ALT + (THRUST / 2)
            FUEL = FUEL - fuelforce
        elif ENGINE == False:
            if ALT < 0:
                if THRUST < -100:
                    death()
                ALT = 0
                THRUST = 0
                SPEED = 0
            else:
                SPEED = SPEED - (downforce / 2)
                THRUST = THRUST - downforce * 2
                ALT = ALT + (THRUST / 2)
        
        system("cls")
        
        if ENGINE == True:
            formatedEngine = "Enabled"
        else:
            formatedEngine = "Disabled"
        
        print(f"Step: {STEP}\nAlt: {ALT}\nEngine: {formatedEngine}\nFuel: {FUEL}\nSpeed: {SPEED}\nThrust: {THRUST}\n\n1) Enable engine\n2) Disable Engine\n")
        inputed = input("Action > ")
            
        if inputed == "1":
            ENGINE = True
        elif inputed == "2":
            ENGINE = False
    
