import shutil
import os


def print_center_screen(text):
    width = shutil.get_terminal_size().columns
    height = shutil.get_terminal_size().lines

    lines = text.split("\n")
    top_space = max(0, (height - len(lines)) // 2)

    print("\n" * top_space, end="")

    for line in lines:
        print(line.center(width))

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def make_bar(value):
    filled = value // 10
    empty = 10 - filled

    return "█" * filled + "░" * empty + f" {value}/100"

def check_pet(pet):
    reminder = ""

    if pet.get_hunger() >= 60:
        reminder += "[!! ПИТОМЕЦ ГОЛОДЕН] \n"
        

    if pet.get_energy() <= 40:
        reminder += "[!! У ПИТОМЦА НЕТ ЭНЕРГИИ НА ДЕЙСТВИЯ! Ему нужно поспать.]\n "
        

    if pet.get_health() <= 40:
        reminder += "[!! У ПИТОМЦА МАЛО ЗДОРОВЬЯ! Нужно подлечить его!] \n"
        

    if pet.get_sleep() <= 30:
        reminder += "[!! ПИТОМЕЦ ХОЧЕТ СПАТЬ] \n"
        

    if pet.get_mood() <= 30:
        reminder += "[!! ПИТОМЕЦ БЕЗ НАСТРОЕНИЯ] \n"
        
    if reminder == "":
        return "С питомцем всё в порядке. Можно заканчивать день."

    return reminder

def get_pet_art(pet):
    if pet.__class__.__name__ == "Cat":
        return """
    ╭━╮┈╭━╮┈┈┈┈┈╭━╮
    ┃╭╯┈┃┊┗━━━━━┛┊┃
    ┃╰┳┳┫┏━▅╮┊╭━▅┓┃
    ┃┫┫┫┫┃┊▉┃┊┃┊▉┃┃
    ┃┫┫┫╋╰━━┛▅┗━━╯╋
    ┃┫┫┫╋┊┊┊┣┻┫┊┊┊╋
    ┃┊┊┊╰┈┈┈┈┈┈┈┳━╯
    """

    elif pet.__class__.__name__ == "Dog":
        return """
    ┈┈╱▔▔▔╲┈┈┈┈┈
    ▇▔┈▍▍┃┈┃╭━╮┈
    ╲━╯┈┈┃┈┃╰╮┃┈
    ┈▔▔┃┈╰━╯╲┃┃┈
    ┈┈┈┃┃┃┈┈▕┃┃┈
    ┈┈┈┃┃┃╭┛▕╯┃┈
    ┈┈┈┗┻┛┗━╯━╯┈
    """

def show_menu(pet):
    clear_screen()

    print_center_screen(f"""
    === Тамагочи ===

    {get_pet_art(pet)}

    ==============================
    Питомец: {pet.name}

    Здоровье:   {make_bar(pet.get_health())}

    Голод:      {make_bar(pet.get_hunger())}

    Энергия:    {make_bar(pet.get_energy())}

    Сон:        {make_bar(pet.get_sleep())}
    
    Настроение: {make_bar(pet.get_mood())}

    {check_pet(pet)}

    1. Покормить
    2. Поиграть
    3. Поспать
    4. Инструкция
    5. Перейти на следующий день
    6. Выход
    """
    )

def instruction_screen():
    clear_screen()

    with open("instruction.txt", "r", encoding="utf-8") as f:
        text = f.read()

    print_center_screen(text)

    input("Нажми Enter...")


def name_screen(choice):
    clear_screen()

    if choice == "dog":
        print_center_screen("""
            ======================================
            ⠄⠄⣠⣤⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣄⠄⠄
            ⠄⢀⡿⣝⢽⢷⣄⠄⠄⢄⠢⡂⡢⢂⠢⠠⡀⢀⣴⢟⡽⣽⡆⠄
            ⠄⢸⣟⢎⣏⢯⣫⣦⡡⣁⣅⣂⣂⣁⣊⢌⡴⣟⢵⡫⡺⣼⡇⠄
            ⠄⠘⣯⢇⢧⢳⣕⢷⢝⡷⣝⡮⡯⣫⢯⣳⣻⣪⢇⢯⢺⣺⠇⠄
            ⠄⢄⢻⣝⢮⣻⡪⡯⡳⣝⣞⢮⢯⡳⣝⡮⣺⡪⣯⣳⣳⡻⢐⠄
            ⡈⡢⢀⣯⢯⣺⣺⣿⣿⣺⡪⡯⣳⢽⢵⢽⣿⢿⣪⢞⣮⡁⡂⡣
            ⠪⠐⣞⣗⢟⣾⠈⠉⠺⣞⡾⡽⣕⡯⣯⠟⠋⠁⣿⢝⡮⣷⠠⡑
            ⢅⢹⣗⡽⣝⣞⢟⡶⡦⡬⣫⣾⣼⣞⡥⡴⣶⡻⡽⣝⣞⢽⡇⢨
            ⡢⢸⣾⣼⣮⣮⣫⢞⣽⣾⡟⠛⠛⢻⣿⣯⡺⣺⣹⣼⣼⣵⡇⢢
            ⠐⠄⢻⣿⣿⣿⣿⣧⣿⣿⣧⣀⢀⣼⣿⣿⣾⣿⣿⣿⣿⡿⢁⠎
            ⠄⠡⡡⠙⢿⣿⣿⣿⣿⣍⢛⠋⠘⣻⢩⣿⣿⣿⣿⡿⠋⡐⠄⠄
            ⠄⠄⠄⠑⡄⠌⠛⠿⣿⣿⣾⣿⣿⣿⣿⣿⡿⠛⡉⡐⡌⠂⠄⠄
            ======================================

    """)
    elif choice == "cat":
        print_center_screen("""
            ======================================
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠄⠄⠄⠄⠄⠄⠄
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡀⠄⠄⠄⠄⠄
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠄⠄⠄⠄
            ⣿⣿⣿⠟⠋⠁⣀⣀⡈⠙⣿⣿⣿⣿⡿⠿⠿⠿⠿⢡⣤⣄⡈⠙⢧⠄⠄⠄
            ⣏⣉⣀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠷⠶⠶⠤⣉⠙⠷⣼⣇⠄⠄
            ⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠄⠄⣿⣿⣶⣈⠙⣄⠄
            ⣿⣷⡶⠶⠶⠶⠒⠂⠄⠈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣆⠄⣿⣿⣷⡶⠖⠄⣶
            ⣁⣤⣴⣶⣶⠾⠟⠛⠛⢛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⣿⣿⣿⣓⠂⠄⣤
            ⠟⢛⣉⣥⣤⣶⡶⠛⢋⣉⡴⢟⣙⠶⣋⣿⣿⣿⠿⠛⠄⠛⠻⢧⡙⠾⢂⣄
            ⣾⣿⣿⡿⠓⣀⠐⠲⠞⣡⣶⠟⢁⣴⠽⠛⣉⣠⣶⣿⣿⣿⣶⣤⠉⣠⣌⠻
            ⣿⣿⣫⣶⣾⣿⡟⣠⣤⣤⠄⣀⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⡿⢋⡄⢻⣿⣷
            ======================================
            """)

    
    pet_name = input("Введите имя питомца: ")

    if len(pet_name) >= 7 or pet_name.isdigit():
        print("Вы должны ввести имя корректно. Имя должно содержать буквы и минимум 6 символов")
    elif pet_name.strip() == "":
        return None
    else:
        return pet_name.strip()
    


def start_screen():

    print_center_screen("""
    Выбери питомца
    ===========================================

          КОТ                         СОБАКА

    ╭━╮┈╭━╮┈┈┈┈┈╭━╮             ┈┈╱▔▔▔╲┈┈┈┈┈
    ┃╭╯┈┃┊┗━━━━━┛┊┃             ▇▔┈▍▍┃┈┃╭━╮┈
    ┃╰┳┳┫┏━▅╮┊╭━▅┓┃             ╲━╯┈┈┃┈┃╰╮┃┈
    ┃┫┫┫┫┃┊▉┃┊┃┊▉┃┃             ┈▔▔┃┈╰━╯╲┃┃┈
    ┃┫┫┫╋╰━━┛▅┗━━╯╋             ┈┈┈┃┃┃┈┈▕┃┃┈
    ┃┫┫┫╋┊┊┊┣┻┫┊┊┊╋             ┈┈┈┃┃┃╭┛▕╯┃┈
    ┃┊┊┊╰┈┈┈┈┈┈┈┳━╯             ┈┈┈┗┻┛┗━╯━╯┈

          [1] КОТ                  [2] СОБАКА

    Величественный пушистик!      Лучший компаньон!
""")
    
    pet_choice = input("Какого питомца вы выберете (1/2)? Напишите ответ: ")

    if pet_choice == "1":
        clear_screen()
        print_center_screen("""
            [ВЫ ВЫБРАЛИ КОТА! ВСТРЕЧАЙТЕ СВОЕГО ПИТОМЦА!]
        """)
        
        return "cat"
    elif pet_choice == "2":
        clear_screen()
        print_center_screen("""
            [ВЫ ВЫБРАЛИ CОБАКУ! ВСТРЕЧАЙТЕ СВОЕГО ПИТОМЦА!]
        """)  
        return "dog"
    else: 
        clear_screen()
        print_center_screen("""
            [НЕПРАВИЛЬНЫЙ ВВОД]
        """)  
              
        return None