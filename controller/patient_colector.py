import os
from view.view_patient_colector import ask_name, ask_birthdate, ask_gender, ask_height, ask_weight

def get_name():
    from controller.parses import parse_name

    name = ask_name()
    return parse_name(name)

def get_birthdate():
    from controller.parses import parse_birthdate

    os.system('cls')
    age = ask_birthdate()
    return parse_birthdate(age)

def get_gender():
    from controller.parses import parse_gender

    os.system('cls')
    gender = ask_gender()
    return parse_gender(gender)

def get_height():
    from controller.parses import parse_height

    os.system('cls')
    height = ask_height()
    return parse_height(height)

def get_weight():
    from controller.parses import parse_weight

    os.system('cls')
    weight = ask_weight()
    return parse_weight(weight)