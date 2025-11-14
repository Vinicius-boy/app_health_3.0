import controller.patient_colector as patient_colector

def catch_name():
    return patient_colector.get_name()

def catch_birthdate():
    return patient_colector.get_birthdate()

def catch_gender():
    return patient_colector.get_gender()

def catch_height():
    return patient_colector.get_height()

def catch_weight():
    return patient_colector.get_weight()