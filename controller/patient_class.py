from datetime import date

class Patient:
    def __init__(self, id, name, birthdate, height, weight, gender):
        self.id = id
        self.name = name
        self.birthdate = birthdate
        self.height = height
        self.weight = weight
        self.gender = gender
    
    @property
    def age(self):
        return self.calculate_age()
    
    def calculate_age(self):
        today_date = date.today()
        age = today_date.year - self.birthdate.year
        if (today_date.month, today_date.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age
    
    def calculate_cmi(self):
        #CMI CALCULATOR 
        cmi = self.weight / (self.height ** 2)
        return cmi
    
    def cmi_classification(self):
        #CLASSIFYING CMI
        cmi_value = self.calculate_cmi()  

        if cmi_value < 18.5:
            classification = '(Low weight)'
        elif 18.5 <= cmi_value <= 24.9:
            classification = '(Normal weight)'
        elif 25 <= cmi_value <= 29.9:
            classification = '(Pre-obese)'
        elif 30 <= cmi_value <= 34.9:
            classification = '(Obesity class I)'
        elif 35 <= cmi_value <= 39.9:
            classification = '(Obesity class II)'
        else:
            classification = '(Obesity class III)'
        return classification
    
    def calculate_bmr(self):
        # METABOLIC BASAL RATE CALCULATOR 
        if self.gender == 'F':
            bmr = 447.593 + (9.247 * self.weight) + (3.098 * (self.height * 100)) - (4.330 * self.age)
        else:
            bmr = 88.362 + (13.397 * self.weight) + (4.799 * (self.height * 100)) - (5.677 * self.age)
        return bmr
    
    def display_info(self):
        # SHOWS THE COMPLETE INFO OF THE PATIENT 
        from view.view import patient_class_info_display

        import os
        os.system('cls')

        cmi_value = self.calculate_cmi()
        classification = self.cmi_classification()

        patient_class_info_display(self, cmi_value, classification)


        
        
        

            

        