import json
import os

from modules.animals import Cat, Dog
import modules.text as sc

def save_progress(pet, day, used_events, food_history_day):
    progress = {
        "day": day,
        "pet_type": pet.__class__.__name__.lower(),
        "name": pet.name,
        "health": pet.get_health(),
        "mood": pet.get_mood(),
        "energy": pet.get_energy(),
        "hunger": pet.get_hunger(),
        "sleep": pet.get_sleep(),
        "used_events": used_events,
        "food_history_day": food_history_day
    }

    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=4)

def load_progress():
    with open("save.json", "r", encoding="utf-8") as f:
        progress = json.load(f)

    if progress["pet_type"] == "cat":
        pet = Cat(progress["name"])
    else:
        pet = Dog(progress["name"])

    pet.set_mood(progress["mood"])
    pet.set_energy(progress["energy"])
    pet.set_health(progress["health"])
    pet.set_hunger(progress["hunger"])
    pet.set_sleep(progress["sleep"])

    day = progress["day"]
    used_events = progress.get("used_events", [])
    food_history_day = progress.get("food_history_day", {})

    return pet, day, used_events, food_history_day

def next_day(pet):
    if pet.get_health() <= 40 or pet.get_energy() <= 40 or pet.get_hunger() >= 60 or pet.get_mood() <= 30 or pet.get_sleep() <= 30:
        return False

    return True

def restart_game():
    choice = input("Хотите попробовать снова? (да/нет): ").lower()
    
    if choice == "да":
        if os.path.exists("save.json"):
            os.remove("save.json")
            
        sc.clear_screen()
    
        final_choice = sc.start_screen()
        while final_choice is None:
            input("Нажми Enter, чтобы попробовать снова...")
            final_choice = sc.start_screen()
    
        pet_name = sc.name_screen(final_choice)

        while pet_name is None or pet_name.strip() == "":
            sc.print_center_screen("""
                [ОШИБКА! Вы не ввели имя питомца!]
            """)
            input("Нажми Enter, чтобы попробовать снова!")

            pet_name = sc.name_screen(final_choice)
    
        if final_choice == "cat":
            pet = Cat(pet_name)
        elif final_choice == "dog":
            pet = Dog(pet_name)

        used_events = []
        food_history_day = {}
    
        day = 1
        save_progress(pet, day, used_events, food_history_day)
    
        input("Нажми Enter...")

        return pet, day, used_events, food_history_day
    elif choice == "нет":
        sc.clear_screen()
        sc.print_center_screen("""
            ["ИГРА ЗАВЕРШЕНА"]
        """)
        exit()