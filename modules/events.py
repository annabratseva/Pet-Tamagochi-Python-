import random
import modules.text as sc
from modules.animals import Cat, Dog

EVENTS = [
    "rain",
    "illness",
    "storm",
    "sunny day",
    "treat"
]

used_events = []

def random_event():
    available_events = []

    for event in EVENTS:
        if event not in used_events:
            available_events.append(event)

    if len(available_events) == 0:
        used_events.clear()
        available_events = EVENTS.copy()

    event = random.choice(available_events)
    used_events.append(event)

    return event

def event_screen(func):
    def event_wrapper(*args, **kwargs):
        
        
        result = func(*args, **kwargs)
        input("Начинается новый день!")

        return result
    return event_wrapper

@event_screen
def apply_event(pet, event, pet_type):
    if event == "rain":
        sc.print_center_screen("""
            [СОБЫТИЕ: ПОШЁЛ ДОЖДЬ! Мягкий шум за окном привлекает питомцев!]
        """)
        if pet_type == "dog":
            sc.print_center_screen("""
                [Ваш питомец радостно плещется в лужицах и пытается поймать капли языком!]
                [ВЫ ПОЛУЧАЕТЕ: +15 к настроению, -20 к энергии, -10 к здоровью]
        """)

        pet.set_mood(pet.get_mood() + 25)
        pet.set_energy(pet.get_energy() - 20)
        pet.set_health(pet.get_health() - 10)

        if pet_type == "cat":
            sc.print_center_screen("""
                [Ваш питомец заметно промокнул и явно этому очень недоволен...]
                [ВЫ ПОЛУЧАЕТЕ: -15 к настроению, -5 к энергии, -10 к здоровью]
            """)

        pet.set_mood(pet.get_mood() - 15)
        pet.set_energy(pet.get_energy() - 5)
        pet.set_health(pet.get_health() - 10)

    elif event == "illness":
        if "rain" in used_events:
            sc.print_center_screen("""
                [СОБЫТИЕ: ПИТОМЕЦ СИЛЬНО ЗАБОЛЕЛ! Дождь не пошёл ему на пользу...]
                [ВЫ ПОЛУЧАЕТЕ: -55 к здоровью, -30 к энергии, -20 к настроению]
            """)

            pet.set_health(pet.get_health() - 55)
            pet.set_energy(pet.get_energy() - 30)
            pet.set_mood(pet.get_mood() - 20)
        else:
            sc.print_center_screen("""
                [СОБЫТИЕ: ПИТОМЕЦ ПРОСТУДИЛСЯ! Питомец где-то подхватил лёгкую простуду...]
                [ВЫ ПОЛУЧАЕТЕ: -40 к здоровью, -20 к энергии, -10 к настроению]
                """)
            
            pet.set_health(pet.get_health() - 40)
            pet.set_energy(pet.get_energy() - 20)
            pet.set_mood(pet.get_mood() - 10)

    elif event == "storm":
        sc.print_center_screen("""
            [СОБЫТИЕ: ГРЕМИТ ГРОМ! Питомец напуган!]
            [ВЫ ПОЛУЧАЕТЕ: -40 к настроению, -10 к энергии]
        """)
        pet.set_energy(pet.get_energy() - 10)
        pet.set_mood(pet.get_mood() - 40)

    elif event == "sunny day":
        sc.print_center_screen("""
            [СОБЫТИЕ: СОЛНЕЧНЫЙ ДЕНЬ! Питомец нагулялся вдоволь!]
            [ВЫ ПОЛУЧАЕТЕ: +25 к настроению, -5 к энергии]
        """)
        pet.set_energy(pet.get_energy() - 5)
        pet.set_mood(pet.get_mood() + 25)
        
    elif event == "treat":
        sc.print_center_screen("""
                    [СОБЫТИЕ: ЛАКОМСТВО! Вы купили питомцу новое лакомство и он нереально счастлив!]
                    [ВЫ ПОЛУЧАЕТЕ: +25 к настроению, -20 к проценту голода]
                """)
        pet.set_hunger(pet.get_hunger() - 20)
        pet.set_mood(pet.get_mood() + 25)