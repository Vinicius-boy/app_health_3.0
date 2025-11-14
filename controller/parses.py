import os
from datetime import date, datetime, timedelta
import controller.patient_form as patient_form
import patient_database

from view.view import no_patients_checked_in, patient_list_display, list_of_patients_title
from view.view import information_of_the_patients_title, id_patient_request,patient_not_found
from view.view import invalid_id, delete_patient_display, id_to_be_deleted, id_to_be_deleted_confirm
from view.view import succesfully_deleted, operation_canceled, name_error_resquest, birthdate_invalid_error
from view.view import birthdate_future_error, age_limit_error, invalid_gender_error, invalid_height_error
from view.view import value_height_error, invalid_weight_error, value_weight_error, go_back_error_display
from view.view import go_back_to_menu, sign_out, warn_menu


def parse_show_menu(menu):
    while True:
        match menu:
            case '1':
                os.system('cls')
                patient_form.check_in_patient()
                go_back_to_menu()
            case '2':
                os.system('cls')
                list_patients_menu()
                go_back_to_menu()
            case '3':
                os.system('cls')
                patient_information_menu()
                go_back_to_menu()
            case '4':
                os.system('cls')
                delete_patient_menu()
                go_back_to_menu()
            case '5':
                sign_out()
            case _:
                menu = warn_menu()

def list_patients_menu():
    #MENU TO LIST PATIENTS
    list_of_patients_title()
    patients = patient_database.list_all_patients()
    
    if not patients:
        no_patients_checked_in()
        return
    
    patient_list_display(patients)

def patient_information_menu():
    information_of_the_patients_title()
    
    patients = patient_database.list_all_patients()
    if not patients:
        no_patients_checked_in()
        return
    
    patient_list_display(patients)

    try:
        id_patient = id_patient_request()
        patient = patient_database.get_patient_by_id(id_patient)
        
        if patient:
            patient.display_info()
        else:
            patient_not_found()
    except ValueError:
        invalid_id()

def delete_patient_menu():
    #MENU TO DELETE PATIENTS
    delete_patient_display()
    
    patients = patient_database.list_all_patients()
    if not patients:
        no_patients_checked_in()
        return
    
    patient_list_display(patients)
    
    try:
        patient_id = id_to_be_deleted()
        
        confirm = id_to_be_deleted_confirm(patient_id)
        if confirm == 'Y':
            if patient_database.delete_patient(patient_id):
                succesfully_deleted()
            else:
                patient_not_found()
        else:
            operation_canceled()
    except ValueError:
        invalid_id()

def parse_name(name):
    while True:
        if not name:
            name = name_error_resquest()
        else:
            return name

def parse_birthdate(age):
    from model.rules import TODAY, MIN_DATE, MAX_DATE

    while True:
        try:
            birthdate = datetime.strptime(age.strip(), "%m/%d/%Y").date()
        except ValueError:
            age = birthdate_invalid_error()
            continue

        if birthdate > TODAY:
            age = birthdate_future_error()
            continue

        if not (MIN_DATE <= birthdate <= MAX_DATE):
            age = age_limit_error()
            continue

        else:
            return birthdate

def parse_gender(gender):
    while True:
        if gender not in ['M', 'F']:
            gender = invalid_gender_error()
        else:
            return gender

def parse_height(height):
    from model.rules import MIN_HEIGHT, MAX_HEIGHT
    while True:
        try:
            value = float(height.replace(',', '.'))
            if not (MIN_HEIGHT <= value <= MAX_HEIGHT):
                height = invalid_height_error()
            else:
                return value
        except ValueError:
            height = value_height_error()

def parse_weight(weight):
    from model.rules import MIN_WEIGHT, MAX_WEIGHT
    while True:
        try:
            value = float(weight.replace(',', '.'))
            if not (MIN_WEIGHT <= value <= MAX_WEIGHT):
                weight = invalid_weight_error()
            else:
                return value
        except ValueError:
            weight = value_weight_error()

def parse_go_back(go_back):
    while True:
        if go_back not in ['1', '0']:
            go_back = go_back_error_display()
        else:
            return go_back