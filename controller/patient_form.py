from controller.bridge import catch_name, catch_birthdate, catch_gender, catch_height, catch_weight
from patient_database import create_patient
from view.view_patient_form import check_in_patient_display, patient_check_in_confirmation

def check_in_patient():
    check_in_patient_display()
    
    #COLECT DATA
    name = catch_name()
    birthdate = catch_birthdate()
    gender = catch_gender()
    height = catch_height()
    weight = catch_weight()

    #SAVE IN DATABASE
    patient_id = create_patient(name, birthdate, height, weight, gender)
    
    # SHOW CONFIRMATION
    patient_check_in_confirmation(patient_id, name, birthdate, height, weight, gender)