import sqlite3
from controller.patient_class import Patient
from datetime import datetime

def init_database():
    #INITIALIZE DATABASE
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birthdate DATE NOT NULL,
            height REAL NOT NULL,
            weight REAL NOT NULL,
            gender TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def create_patient(name, birthdate, height, weight, gender):
    #FUNCTION CREATE NEW PATIENT
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO patients (name, birthdate, height, weight, gender)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, birthdate, height, weight, gender))
    
    patient_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return patient_id

def list_all_patients():
    #FUNCTION TO LIST ALL PATIENTS (ALPHABETICALLY)
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM patients ORDER BY name')
    patients_data = cursor.fetchall()
    conn.close()
    
    patients = []
    for patient_data in patients_data:
        patient = Patient(
            id=patient_data[0],
            name=patient_data[1],
            birthdate=datetime.strptime(patient_data[2], '%Y-%m-%d').date(),
            height=patient_data[3],
            weight=patient_data[4],
            gender=patient_data[5]
        )
        patients.append(patient)
    
    return patients

def delete_patient(patient_id):
    #DELETE PATIENT USING ID
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM patients WHERE id = ?', (patient_id,))
    deleted = cursor.rowcount > 0
    
    conn.commit()
    conn.close()
    
    return deleted

def get_patient_by_id(patient_id):
    #SELECT SPECIFIC PATIENT
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM patients WHERE id = ?', (patient_id,))
    patient_data = cursor.fetchone()
    conn.close()
    
    if patient_data:
        patient = Patient(
            id=patient_data[0],
            name=patient_data[1],
            birthdate=datetime.strptime(patient_data[2], '%Y-%m-%d').date(),
            height=patient_data[3],
            weight=patient_data[4],
            gender=patient_data[5]
        )
        return patient
    return 