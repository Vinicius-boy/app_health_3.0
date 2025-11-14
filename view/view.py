import os, controller.parses as parses

def sign_out():
    os.system('cls')
    print('''\nSigning out...\n
Thank you for using this application\n''')
    exit()

def warn_menu():
    return input('Please, enter a valid option from the MENU: ')

def go_back_to_menu():
    import view.menu as menu
    go_back = input('\nWould you like to go back to MENU (1 for YES / 0 for NO): ')
    value = parses.parse_go_back(go_back)
    if value == '1':
        os.system('cls')
        menu.show_menu()
    else:
        os.system('cls')
        print('\nThank you for using this application, signing out...\n')
        exit()

def show_menu_display():
        print('\n-----------( MENU )------------')
        print('''
1 - Check-in patient
2 - List of patients
3 - Patient Information
4 - Delete patient
5 - Exit\n''')
        return

def no_patients_checked_in():
    print("No patients checked-in.")
    return

def patient_list_display(patients):
    for patient in patients:
        print(f"{patient.name} (cod: {patient.id})")
    return

def list_of_patients_title():
    print('\n-----------( LIST OF PATIENTS )------------')
    return

def information_of_the_patients_title():
    print('\n-----------( INFORMATION OF THE PATIENTS )------------')
    return

def id_patient_request():
    patient_id = int(input('\nEnter the ID of the patient to see their information: '))
    return patient_id

def patient_not_found():
    print("Patient not found!")
    return

def invalid_id():
    print("Invalid ID!")
    return

def delete_patient_display():
    print('\n-----------( DELETE PATIENT )------------')
    return

def id_to_be_deleted():
    id = int(input('\nEnter the ID of the patient to be deleted: '))
    return id

def id_to_be_deleted_confirm(patient_id):
    choise = input(f'Are you sure you want to delete thepatient {patient_id}? (Y/N): ').upper()
    return choise

def succesfully_deleted():
    print("Patient has been succesfully deleted!")
    return

def operation_canceled():
    print("Operation canceled.")

def name_error_resquest():
    name = input(">>> This field can't be empty, please enter your name: ").title().strip()
    return name

def birthdate_invalid_error():
    birthdate = input('Enter a valid birthdate (MM/DD/YYYY): ')
    return birthdate

def birthdate_future_error():
    birthdate = input("Birthdate cannot be in the future. Enter it again: ")
    return birthdate

def age_limit_error():
    birthdate = input("Patient must be between 18 and 120 years old: ")
    return birthdate

def invalid_gender_error():
    gender = input('>>> Invalid gender. Please use M or F: ').upper()
    return gender

def invalid_height_error():
    height = input('Invalid height. Please enter between 0.54 and 2.50 meters: ')
    return height

def value_height_error():
    height = input('>>> Invalid height, use numbers: ')
    return height

def invalid_weight_error():
    weight = input('Invalid weight. Please enter between 2 and 635 kilograms: ')
    return weight

def value_weight_error():
    weight = input('>>> Invalid weight, use numbers: ')
    return weight

def go_back_error_display():
    choise = input('Please, enter a valid option (1 or 0): ')
    return choise

def patient_class_info_display(self, cmi_value, classification):
    print(f"\n--- Patient information ---")
    print(f"ID: {self.id}")
    print(f"Name: {self.name}")
    print(f"Date of birth: {self.birthdate.strftime('%m/%d/%Y')}")
    print(f"Age: {self.age} years")
    print(f"Height: {self.height:.2f}m")
    print(f"Weight: {self.weight:.2f}kg")
    print(f"Gender: {self.gender}")

    print(f"Corporal Mass Index (CMI): {cmi_value:.2f} - {classification}")
    print(f"Basal Metabolic Rate (BMR): {self.calculate_bmr():.2f} calories")