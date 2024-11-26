import random
import time



def dnd_class(class_list):
    return random.choice(class_list)


def roll_dice_d6():
    return random.randint(1, 6)


def charecteristic_base_function():
    dice_list = []

    for dice_result in range(4):
        dice_list.append(roll_dice_d6())
    return sum(sorted(dice_list, reverse=True)[:3])


def weapon(weapon_list):
    return random.sample(weapon_list, 2)


def character_names(race_for_names):
    if race_for_names == 'Elf':
        names = ['Говнокострат', 'Хуебес', 'Келлимбримбор']
        return random.choice(names)
    elif race_for_names == 'Human':
        names = ['Письсись', 'Сисьпись', 'Пётр']
        return random.choice(names)
    elif race_for_names == 'Aasimar':
        names = ['Рома', 'Зератул', 'Гугу']
        return random.choice(names)
    elif race_for_names == 'Dwarf':
        names = ['Адрик', 'Тор', 'Музбек']
        return random.choice(names)
    elif race_for_names == 'Gnome':
        names = ['Алвин', 'Элайджа Вуд', 'Йу']
        return random.choice(names)
    elif race_for_names == 'Half-elf':
        names = ['Кель', 'Мраз', 'Галадриэль']
        return random.choice(names)
    elif race_for_names == 'Kenku':
        names = ['Шахтёр', 'Стукач', 'Сценарист']
        return random.choice(names)
    else:
        names = ['Гаррош', 'Зак-Зак', 'Лок']
        return random.choice(names)


first_weapon = True

charecteristic = {'Сила': charecteristic_base_function(),
                  'Ловкость': charecteristic_base_function(),
                  'Телосложение': charecteristic_base_function(),
                  'Интеллект': charecteristic_base_function(),
                  'Мудрость': charecteristic_base_function(),
                  'Харизма': charecteristic_base_function()}

race = ['Эльф', 'Человек', 'Аасимар', 'Дворф', 'Гном', 'Полуэльф', 'Кенку', 'Орк']

elf_dict = {'Ловкость': 2}
human_dict = {'Сила': 1, 'Ловкость': 1, 'Телосложение': 1, 'Интеллект': 1, 'Мудрость': 1, 'Харизма': 1}
aasimar_dict = {'Харизма': 2}
dwarf_dict = {'Телосложение': 2, 'Сила': 1}
gnome_dict = {'Интеллект': 2}
half_elf_dict = {'Харизма': 2, 'charecteristic_base_function()': 1, 'charecteristic_base_function()': 1}
kenku_dict = {'Харизма': 2, 'Мудрость': 1}
orc_dict = {'Сила': 2, 'Телосложение': 1}



game_class = ['Паладин', 'Жрец', 'Воин', 'Волшебник', 'Варвар',
              'Изобретатель', 'Плут', 'Колдун', 'Монах', 'Друид', 'Бард']
weapon_choice = ['Палаш', 'Глефа', 'Полуторник', 'Однорук', 'Копьё']
true_class = dnd_class(game_class)
spells_cells = 0
worldview = ['Добро', 'Зло', 'Закон', 'Хаос', 'Законопослушный добрый', 'Законопослушный нейтральный',
             'Законопослушный злой', 'Нейтральный добрый', 'Истинно нейтральный', 'Нейтральный злой',
             'Хаотичный добрый', 'Хаотичный нейтральный']
true_worldview = random.choice(worldview)
backstory = ['Артист', 'Беспризорник', 'Благородный', 'Гильдейский ремесленник', 'Моряк',
             'Мудрец', 'Народный герой', 'Отшельник', 'Пират', 'Преступник', 'Прислужник',
             'Солдат', 'Чужеземец', 'Шарлатан']
true_backstory = random.choice(backstory)
true_race = random.choice(race)

print('Ваша предыстория:', true_backstory)
print('Мировоззрение:', true_worldview)
print('Ваша раса:', true_race)
print('Ваше имя:', character_names(true_race))
print('Ваш класс:', true_class)
print('Ваш под-класс:', dnd_class(game_class))

for dots in charecteristic:
    print(dots, ':', charecteristic.get(dots))

if true_race == 'Эльф':
    for base_char in charecteristic:
        for race_char in elf_dict:
            if race_char == base_char:
                charecteristic[base_char] += elf_dict.get(race_char)
elif true_race == 'Человек':
    for base_char in charecteristic:
        for race_char in human_dict:
            if race_char == base_char:
                charecteristic[base_char] += human_dict.get(race_char)
elif true_race == 'Аасимар':
    for base_char in charecteristic:
        for race_char in aasimar_dict:
            if race_char == base_char:
                charecteristic[base_char] += aasimar_dict.get(race_char)
elif true_race == 'Дворф':
    for base_char in charecteristic:
        for race_char in dwarf_dict:
            if race_char == base_char:
                charecteristic[base_char] += dwarf_dict.get(race_char)
elif true_race == 'Гном':
    for base_char in charecteristic:
        for race_char in gnome_dict:
            if race_char == base_char:
                charecteristic[base_char] += gnome_dict.get(race_char)
elif true_race == 'Полуэльф':
    for base_char in charecteristic:
        for race_char in half_elf_dict:
            if race_char == base_char:
                charecteristic[base_char] += half_elf_dict.get(race_char)
elif true_race == 'Кенку':
    for base_char in charecteristic:
        for race_char in kenku_dict:
            if race_char == base_char:
                charecteristic[base_char] += kenku_dict.get(race_char)
else:
    for base_char in charecteristic:
        for race_char in orc_dict:
            if race_char == base_char:
                charecteristic[base_char] += orc_dict.get(race_char)

for dots in charecteristic:
    print(dots, ':', charecteristic.get(dots))

for i in weapon(weapon_choice):
    if true_class == 'Монах':
        print('Ты лох, начинаешь без оружия.')
        break
    if first_weapon:
        print('Ваше оружие: ', i, end=' ')
        first_weapon = False
    else:
        print(i, end=' ')
if true_class == 'Плут':
    print('\nТы идёшь нахуй.')
else:
    spells_cells = 2
print('\nЯчеек заклинаний: ', spells_cells)

