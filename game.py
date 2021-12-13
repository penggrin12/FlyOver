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
    
def game():
    # Параметры
    
    IS_FUEL_INFINITY = False
    ENGINE = False
    HOVER = False
    HOVERALT = 0
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
        
        # гравитация
        fuelforce = random.randint(1,5)
        upforce = random.randint(1,5)
        if ALT > 100000:
            downforce = 0
        elif ALT > 10000:
            downforce = random.randint(0,1)
        elif ALT > 1000:
            downforce = random.randint(1,3)
        elif ALT > 0:
            downforce = random.randint(1,3)
        elif ALT <= 0:
            if THRUST < -20:
                system("cls")
    
                print("You dead!\n\nGame Over")
                sleep(10)
                exit()
            ALT = 0
            SPEED = 0
            THRUST = 0
            downforce = 0
        
        # выключение двигателя без топлива
        if FUEL <= 0:
            ENGINE = False
            print("No fuel!\nEngine disabled")
        
        # Двигатель
        if (ENGINE == True) and (THRUST <= MAX_THRUST):
            THRUST = THRUST + upforce
            SPEED = SPEED + (upforce * 2)
            ALT = ALT + (THRUST / 2)
            FUEL = FUEL - fuelforce
        elif ENGINE == False:
            if ALT < 0:
                ALT = 0
                THRUST = 0
                SPEED = 0
            else:
                SPEED = SPEED - (downforce / 2)
                THRUST = THRUST - downforce * 2
                ALT = ALT + (THRUST / 2)
        
        if (HOVER == True) and (FUEL > 0):
            ALT = HOVERALT
            FUEL = FUEL - 35
            SPEED = 0
            THRUST = 0
        
        system("cls")
        
        # форматим параметры
        if ENGINE == True:
            formatedEngine = "Enabled"
        else:
            formatedEngine = "Disabled"
            
        if HOVER == True:
            formatedHover = "Enabled"
        else:
            formatedHover = "Disabled"
        
        # выключение всего без топлива
        if FUEL <= 0:
            FUEL = 0
            ENGINE = False
            HOVER = False
        
        # вывод
        print(f"Step: {STEP}\nAlt: {ALT}\nEngine: {formatedEngine}\nAuto Hover: {formatedHover}\nFuel: {FUEL}\nSpeed: {SPEED}\nDown Force: {downforce}\nThrust: {THRUST}\n\n")
        print("1) Engine\n2) Auto Hover")
        inputed = input("\nAction > ")
           
        # обработчик входа
        if (inputed == "1") and (FUEL > 0):
            if ENGINE == True:
                ENGINE = False
                print("Engine disabled")
            else:
                ENGINE = True
                print("Engine enabled")
        elif (inputed == "2") and (FUEL > 0):
            if HOVER == True:
                HOVER = False
                print("Auto Hover disabled")
            else:
                HOVER = True
                HOVERALT = ALT
                print("Auto Hover enabled")
    
