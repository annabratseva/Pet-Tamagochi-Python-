import random

import modules.text as sc


def dog_game(pet):
    sc.clear_screen()
    sc.print_center_screen("""
    [ИГРА С СОБАКОЙ: КОМБИНАЦИИ]

    У вас будут комбинации из чисел, введите их правильно!
    Всего 3 раунда.
    """)

    rounds = 3
    score = 0

    for round_num in range(1, rounds + 1):
        combination = ""

        for i in range(5):
            combination += str(random.randint(0, 9))

        print(f"\nРаунд {round_num}")
        print(f"Запомни комбинацию: {combination}")

        input("Нажми Enter, когда будете готовы продолжить...")

        sc.clear_screen()

        answer = input("Введи комбинацию: ")

        if answer == combination:
            print("Правильно! Собака счастлива!")
            score += 1
        else:
            print(f"Ошибка! Правильная комбинация: {combination}")

    if score == 3:
        pet.set_mood(pet.get_mood() + 30)
        pet.set_health(pet.get_health() + 10)
        pet.set_energy(pet.get_energy() - 10)
        print("\nВы прошли все раунды! +30 настроения и +10 здоровья! Собака немного устала.")

    elif score == 2:
        pet.set_mood(pet.get_mood() + 20)
        pet.set_energy(pet.get_energy() - 10)
        print("\nХорошая работа! Вы отгадали 2. +20 настроения! Собака немного устала.")

    elif score == 1:
        pet.set_mood(pet.get_mood() + 15)
        pet.set_energy(pet.get_energy() - 10)
        print("\nХорошая работа! Вы отгадали 1. +15 настроения! Собака немного устала.")

    else:
        print("\nНе получилось! Попробуй ещё раз в следующий раз!")

    input("\nНажми Enter, чтобы вернуться в меню...")


def cat_game():
    cat_words = {
        "МЯУ": "я злюсь",
        "мяу": "хочу кушать",
        "Мяу": "привет",
        "МЯу?": "что?",
        "мяУ": "я ухожу",
        "мур мур": "спасибо за еду",
        "МЯЯЯУ": "уйди от меня"
    }

    result = 0
    print("\n [ПОДСКАЗКА: Смотрите как пишется каждое мяу (включая знаки)!] \n Давайте начнём! \n")

    print("СЛОВАРЬ ПОМОЩИ: \n")
    for word, translation in cat_words.items():
        print(f"[{word}: {translation}]")

    print("-----------------------------------\n")

    random_words = random.sample(list(cat_words.keys()), 3)
    
    print(f'ПЕРЕВЕДИТЕ БЫСТРЕЕ: {" ".join(random_words)} \n')

    for word in random_words:

        translated_words = input(f"Введите правильный перевод слова [{word}]: ").lower().strip()

        if translated_words == cat_words[word].lower().strip():
            print("Вы правильно перевели!")
            result += 1
        else:
            print("Неправильно!")

    sc.print_center_screen("""
        /---------------РЕЗУЛЬТАТ---------------/

    """)

    if result == 1:
        print("ВЫ РАСШИФРОВАЛИ ОДНО СЛОВО!")
        print("[Ваш питомец получает +5 к настроению.]")
    elif result == 2:
        print("ВЫ РАСШИФРОВАЛИ ДВА СЛОВА!")
        print("[Ваш питомец получает +10 к настроению.]")
    elif result == 3:
        print("ВЫ РАСШИФРОВАЛИ ВСЕ ТРИ СЛОВА!")
        print("[Ваш питомец получает +15 к настроению.]")
    elif result == 0:
        print("ВЫ НИЧЁ НЕ СМОГЛИ ПЕРЕВЕСТИ!")

    return result