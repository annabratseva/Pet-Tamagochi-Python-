import os

from modules.animals import Cat, Dog
from modules.save_game import save_progress, load_progress, next_day, restart_game
import modules.text as sc
import modules.events as events

FOOD = [
    {"name": "Стейк", "hunger": 70, "energy": 30, "mood": 60},
    {"name": "Сухой корм", "hunger": 30},
    {"name": "Жидкий корм", "hunger": 20},
    {"name": "Яблоко", "hunger": 10, "mood": 10},
    {"name": "Сосиска", "hunger": 25, "mood": 20},
    {"name": "Банан", "hunger": 15},
    {"name": "???", "hunger": -20, "mood": -30},
    {"name": "Лекарство", "health": 60, "hunger": 10}
]

food_history_day = {}
fed_today = []

FOOD.sort(key=lambda food: food["hunger"])

def show_food():
    for i in range(len(FOOD)):
        print(i + 1, FOOD[i]["name"])

# --------------------------------------


# CHECKS YOUR SAVE
if os.path.exists("save.json") and os.path.getsize("save.json") > 0:
    pet, day, loaded_events, food_history_day = load_progress()
    events.used_events = loaded_events

    if day >= 5:
        sc.clear_screen()
        sc.print_center_screen("""
            [ВЫ ЗАКОНЧИЛИ ИГРУ!]
            Приключения с питомцем ещё не закончились...
        """)

        result = restart_game()

        if result is not None:
            pet, day, used_events, food_history_day = result
            events.used_events = used_events
            fed_today.clear()
        else:
            exit()

    else:
        for food_name in food_history_day:
            if food_history_day[food_name] == day:
                fed_today.append(food_name)

        sc.print_center_screen(f"""
            Добро пожаловать обратно!
            Ваш питомец {pet.name} ждёт вас!
            День: {day}
        """)
        input("Нажми Enter...")

else:
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

    day = 1
    food_history_day = {}
    fed_today.clear()
    events.used_events.clear()


while True:
    if pet.get_health() == 0 or pet.get_energy() == 0 or pet.get_hunger() == 100 or pet.get_mood() == 0 or pet.get_sleep() == 0:
        sc.clear_screen()
        sc.print_center_screen(f"""
            [ИГРА ОКОНЧЕНА! [{pet.name}] не удалось спасти...]

            Одна из характеристик достигла предела.

        """)

        save_progress(pet, day, events.used_events, food_history_day)
        input("Нажми Enter для продолжения...")

        result = restart_game()

        if result is not None:
            pet, day, used_events, food_history_day = result
            events.used_events = used_events
            fed_today.clear()
            continue    
        else:
            break


    sc.show_menu(pet)

    choice = input("Введите ваш выбор цифрами: ")

    # FEED THE PET
    if choice == "1":
        show_food()

        food_choice = input("Выберите, чем хотите покормить питомца (число): ")

        if food_choice.isdigit():
            food_choice = int(food_choice)

            if 1 <= food_choice <= len(FOOD):
                food = FOOD[food_choice - 1]
                food_name = food["name"]

                if food_name in fed_today:
                    print("Эту еду уже сегодня давали!")
                    input("Нажми Enter...")
                elif food_name in food_history_day and day - food_history_day[food_name] < 2:
                    print("Эту еду нельзя давать два дня подряд!")
                    input("Нажми Enter...")
                else:
                    pet.eat(food)
                    food_history_day[food_name] = day
                    fed_today.append(food_name)
                    input("Нажми Enter...")
            else:
                print("Такой еды нет.")
                input("Нажми Enter...")
        else:
            print("Нужно ввести число!")

    # PLAY
    elif choice == "2":
        sc.clear_screen()
        pet.play()
        input("Нажми Enter...")

    # SLEEP
    elif choice == "3":
        pet.sleep()
        input("Нажми Enter...")

    # INSTRUCTION
    elif choice == "4":
        sc.instruction_screen()

    # NEXT DAY
    elif choice == "5":
        if next_day(pet):
            if day < 5:
                sc.clear_screen()

                pet.new_day()
                day += 1
                fed_today.clear()
                sc.print_center_screen(f"""
                    [Питомец спокойно засыпает...и начинается новый день!]
                    [ДЕНЬ: {day}]

                    [Какое же событие произойдёт сегодня?]
                """)

                event = events.random_event()
                pet_type = pet.__class__.__name__.lower()

                events.apply_event(pet, event, pet_type)

                save_progress(pet, day, events.used_events, food_history_day)
            else:
                sc.clear_screen()
                sc.print_center_screen("""
                    [ИГРА ЗАВЕРШЕНА! ПОЗДРАВЛЯЕМ!]
                """)
                save_progress(pet, day, events.used_events, food_history_day)

                break
        else:
            sc.clear_screen()
            sc.print_center_screen("""
                [НЕВОЗМОЖНО ПЕРЕЙТИ НА СЛЕДУЮЩИЙ ДЕНЬ! ПИТОМЕЦ СЛИШКОМ СЛАБ. 
                Сначала позаботесь о нём!]
            """)
        
            input("Нажми Enter...")
        
        input("Нажми Enter...")

    # EXIT FROM CONSOLE
    elif choice == "6":
        save_progress(pet, day, events.used_events, food_history_day)
        print("Завершаем игру...")
        break
    else:
        print("Неверный выбор.")
        input("Нажми Enter...")