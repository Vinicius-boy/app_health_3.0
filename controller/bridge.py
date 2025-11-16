import controller.patient_colector as patient_colector

def catch_name(value):
    value = value.strip().title()
    if not value:
        raise ValueError("Nome não pode estar vazio.")
    return value
    
    
#return patient_colector.get_name()

def catch_birthdate(value):
    value = value.strip()
    if not value:
        raise ValueError("Data de nascimento não pode estar vazia.")
    return value
    
    
#return patient_colector.get_birthdate()

def catch_gender(value):
    value = value.strip().upper()
    if value not in ("M", "F"):
        raise ValueError("Gênero deve ser M ou F.")
    return value

#return patient_colector.get_gender()

def catch_height(value):
    try:
        h = float(value)
        if h <= 0:
            raise ValueError("Altura deve ser maior que zero.")
        return h
    except:
        raise ValueError("Altura inválida.")

#return patient_colector.get_height()

def catch_weight(value):
    try:
        w = float(value)
        if w <= 0:
            raise ValueError("Peso deve ser maior que zero.")
        return w
    except:
        raise ValueError("Peso inválido.")
     
#return patient_colector.get_weight()