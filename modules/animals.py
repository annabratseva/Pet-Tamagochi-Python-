import modules.mini_games as game
from abc import ABC, abstractmethod

def calculate_hunger(hunger, food_stat):
    new_hunger = hunger - food_stat

    if new_hunger < 0:
        return 0
    elif new_hunger > 100:
        return 100
    else:
        return new_hunger

class Animal(ABC):
    def __init__(self, health, hunger, sleep, energy, mood, name):
        self.__health = max(0, min(100, health))
        self.__hunger = max(0, min(100, hunger))
        self.__sleep = max(0, min(100, sleep))
        self.__energy = max(0, min(100, energy))
        self.__mood = max(0, min(100, mood))
        self.name = name

    @abstractmethod
    def eat(self, food):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def reset_stats(self):
        pass

    def new_day(self):
        self.set_hunger(self.get_hunger() + 35)
        self.set_sleep(self.get_sleep() - 30)
        self.set_energy(self.get_energy() - 25)
        self.set_mood(self.get_mood() - 25)

    # ГЕТТЕРЫ

    def get_health(self):
        return self.__health

    def get_hunger(self):
        return self.__hunger

    def get_energy(self):
        return self.__energy

    def get_mood(self):
        return self.__mood

    def get_sleep(self):
        return self.__sleep

    # СЕТТЕРЫ

    def set_hunger(self, value):
        self.__hunger = max(0, min(100, value))

    def set_energy(self, value):
        self.__energy = max(0, min(100, value))

    def set_mood(self, value):
        self.__mood = max(0, min(100, value))

    def set_sleep(self, value):
        self.__sleep = max(0, min(100, value))

    def set_health(self, value):
        self.__health = max(0, min(100, value))

class Dog(Animal):
    def __init__(self, name):
        super().__init__(100, 80, 30, 50, 60, name)

    def eat(self, food):
        food_stat = food.get("hunger", 0)
        food_energy = food.get("energy", 0)
        food_mood = food.get("mood", 0)
        food_health = food.get("health", 0)
                
        health = self.get_health()
        energy = self.get_energy()
        mood = self.get_mood()

        if self.get_hunger() == 0:
            print("Питомец сыт...")

        if food["name"] == "Стейк":
            print(f"[{self.name}] очень доволен/довольна. Это оказывается любимой едой!")
            print("[ВЫ ПОЛУЧАЕТЕ БОНУС К КОРМЛЕНИЮ. +10]")
            food_stat += 10 
        elif food["name"] == "???":
            print(f"У[{self.name}] появляются подозрения, но всё равно съедает это!")
            print(f"Это оказался вонючий носок.. {self.name} не наедается! [ВЫ ПОЛУЧАЕТЕ ДЕБАФФ НА НАСТРОЕНИЕ! ДОП. -10]")
            food_mood -= 10
        elif food["name"] == "Сосиска": print(f"[{self.name}] все собаки любят такое лакомство. {self.name} не исключение!")  
        elif food["name"] == "Сухой корм":
            print(f"[{self.name}] не удивлён/удивлена вашему недостатку креативности! Но всё равно это съедает, даже несмотря на испорчённое настроение.")
            print("[НАСТРОЕНИЕ ИСПОРТИЛОСЬ НА 10!]")
            food_mood -= 10
        elif food["name"] == "Лекарство":
            if health >= 70:
                print("Питомец вполне здоров!")
            else:
                print(f"[{self.name}] проглотил лекарство! Вкус.. так себе.")
                self.set_health(health + food_health)
        else: print(f"[{self.name}] вкусно поел/поела и доволен/довольна собой!")
            

        new_hunger = calculate_hunger(self.get_hunger(), food_stat)

        self.set_mood(mood + food_mood)
        self.set_hunger(new_hunger)
        self.set_energy(energy + food_energy)

    def sleep(self):
        sleep_lvl = self.get_sleep()
        hunger = self.get_hunger()
        mood = self.get_mood()
        energy = self.get_energy()

        if hunger >= 70:
            print(f"[{self.name}] очень хочет кушать. Сначала покормите его/её! Он/она не ляжет на голодный желудок.")

        elif hunger <= 20:
            print(f"[{self.name}] чувствует себя отлично. Он/она хорошо поспал/а и получает: [БОНУС К НАСТРОЕНИЮ +10]")
            mood += 10
            sleep_lvl += 70
            energy += 40
        else:
            print(f"[{self.name}] поспал нормально.")
            energy += 30
            sleep_lvl += 60

        self.set_energy(energy)
        self.set_mood(mood)
        self.set_sleep(sleep_lvl)


    def play(self):
        if self.get_energy() <= 40:
            print("Собака не может играть, ей нужно поспать.")
        else:
            game.dog_game(self)

    
    def reset_stats(self):
        self.set_health(100)
        self.set_hunger(80)
        self.set_sleep(30)
        self.set_energy(50)
        self.set_mood(60)

    
class Cat(Animal):
    def __init__(self, name):
         super().__init__(90, 80, 20, 10, 30, name)
    def eat(self, food):
        food_stat = food.get("hunger", 0)
        food_energy = food.get("energy", 0)
        food_mood = food.get("mood", 0)
        food_health = food.get("health", 0)
        
        health = self.get_health()
        energy = self.get_energy()
        mood = self.get_mood()

        if self.get_hunger() == 0:
            print("Питомец сыт...")
            
        if food["name"] == "Яблоко" or food["name"] == "Банан":
            print(f"[{self.name}] съел/съела неохотно. Ему/ей явно такое не по нраву.")
            print("[ВЫ ПОЛУЧАЕТЕ ДЕБАФФ НА НАСТРОЕНИЕ! -20]")
            food_mood -= 20
        elif food["name"] == "Стейк":
            print(f"[{self.name}] очень рад/рада. Наконец-то хорошая еда для своего величества.")
        elif food["name"] == "???":
            print(f"[{self.name}] не понимает что это такое. Он считает вас безумцем.")
            print("[ВЫ ПОЛУЧАЕТЕ ДЕБАФФ НА НАСТРОЕНИЕ! -5]")
            food_mood -= 5
        elif food["name"] == "Лекарство":
            if health >= 70:
                print("Питомец вполне здоров!")
            else:
                print(f"[{self.name}] проглотил лекарство! Вкус.. так себе.")
                self.set_health(health + food_health)
        else:
            print(f"[{self.name}] считает это нормой. Ничего примечательного..")
        
        new_hunger = calculate_hunger(self.get_hunger(), food_stat)

        
        self.set_mood(mood + food_mood)
        self.set_hunger(new_hunger)
        self.set_energy(energy + food_energy)

    def sleep(self):
        sleep_lvl = self.get_sleep()
        hunger = self.get_hunger()
        mood = self.get_mood()
        energy = self.get_energy()

        if hunger >= 70:
            print(f"[{self.name}] голодна/голоден и не может уснуть! Сначала покормите её/его.")

        elif hunger <= 20:
            print(f"[{self.name}] сладко мурлычет во сне!")
            print("БОНУС К НАСТРОЕНИЮ +15")
            mood += 15
            sleep_lvl += 60
            energy += 40

        else:
            print(f"[{self.name}] спокойно спит в своём уютном уголке.")
            sleep_lvl += 40
            energy += 30

        self.set_energy(energy)
        self.set_mood(mood)
        self.set_sleep(sleep_lvl)

    def play(self):
        mood = self.get_mood()
        energy = self.get_energy()

        result = game.cat_game()

        if result == 1:
            mood += 5
        elif result == 2:
            mood += 10
        elif result == 3:
            mood += 15
        elif result == 0:
            print("[Вы ничего не получаете.]")

        print("\n [Питомец немного выдохся после игры, но это не сильно повлияло на него!] \n")

        energy -= 15

        self.set_mood(mood)
        self.set_energy(energy)

    def reset_stats(self):
        self.set_health(90)
        self.set_hunger(80)
        self.set_sleep(20)
        self.set_energy(10)
        self.set_mood(30)