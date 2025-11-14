def ask_name():
    name = input('Insert your name: ').title().strip()
    return name

def ask_birthdate():
    birthdate = input('Please, enter your birthdate (MM/DD/YYYY - american format ): ')
    return birthdate

def ask_gender():
    gender = input('Please, enter your biological gender (M/F): ').upper().strip()
    return gender

def ask_height():
    height = input('\nInsert your height (in meters): ')
    return height

def ask_weight():
    weight = input('\nInsert your weight (in kilograms): ')
    return weight