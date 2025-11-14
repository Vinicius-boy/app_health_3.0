def check_in_patient_display():
    print('\n-----------( CHECK-IN PATIENT )------------')
    return

def patient_check_in_confirmation(patient_id, name, birthdate, height, weight, gender):
    print(f"\n>>> Patient successfully checked-in")
    print(f"Patient ID: {patient_id}")
    print(f"Name: {name}")
    print(f"Date of birth: {birthdate.strftime('%m/%d/%Y')}")
    print(f"Height: {height:.2f}m")
    print(f"Weight: {weight:.2f}kg")
    print(f"Gender: {gender}")
    return