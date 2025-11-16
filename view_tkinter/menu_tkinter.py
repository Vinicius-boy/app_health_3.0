import tkinter as tk
from tkinter import ttk, messagebox
import patient_database
import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw



class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Pacientes - UNESC")
        self.root.geometry("600x500")
        self.setup_ui()
    
        

    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        

        # Título

        title_label = ttk.Label(main_frame, text="-----------( MENU )------------", 
                               font=('Arial', 14, 'bold'))
        title_label.pack(pady=10)

        

        # Botões do menu
        buttons = [
            ("1 - Check-in patient", self.check_in_patient),
            ("2 - List of patients", self.list_patients),
            ("3 - Patient Information", self.patient_information),
            ("4 - Delete patient", self.delete_patient),
            ("5 - Exit", self.exit_app)
        ]
        
        for text, command in buttons:
            btn = ttk.Button(main_frame, text=text, command=command, width=30)
            btn.pack(pady=5)
    

    def check_in_patient(self):
        CheckInWindow(self.root)
    
    def list_patients(self):
        ListPatientsWindow(self.root)
    
    def patient_information(self):
        PatientInfoWindow(self.root)
    
    def delete_patient(self):
        DeletePatientWindow(self.root)
    
    def exit_app(self):
        self.root.quit()
    
    def run(self):
        self.root.mainloop()

class CheckInWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Check-in Patient")
        self.window.geometry("400x400")
        
        self.setup_form()
    
    def setup_form(self):
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)


        ttk.Label(main_frame, text="-----------( CHECK-IN PATIENT )------------", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Campos do formulário
        self.name_var = tk.StringVar()
        self.birthdate_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.height_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        
        fields = [
            ("Name:", self.name_var),
            ("Birthdate (MM/DD/YYYY):", self.birthdate_var),
            ("Gender (M/F):", self.gender_var),
            ("Height (meters):", self.height_var),
            ("Weight (kilograms):", self.weight_var)
        ]
        
        for label, var in fields:
            frame = ttk.Frame(main_frame)
            frame.pack(fill=tk.X, pady=5)
            ttk.Label(frame, text=label, width=20).pack(side=tk.LEFT)
            ttk.Entry(frame, textvariable=var, width=20).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Botões
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=20)
        
        ttk.Button(btn_frame, text="Save", command=self.save_patient).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Cancel", command=self.window.destroy).pack(side=tk.LEFT, padx=5)
    
    def save_patient(self):
        try:
            # Usando as funções ORIGINAIS do seu código
            from controller.bridge import catch_name, catch_birthdate, catch_gender, catch_height, catch_weight
            from patient_database import create_patient
            
            # Simulando as entradas do usuário
            import builtins
            original_input = builtins.input
            
            # Configura as respostas para as funções originais
            inputs = [
                self.name_var.get(),
                self.birthdate_var.get(),
                self.gender_var.get(),
                self.height_var.get(),
                self.weight_var.get()
            ]
            
            input_iterator = iter(inputs)
            builtins.input = lambda prompt="": next(input_iterator)
            
            # Chama as funções ORIGINAIS do seu sistema
            name = catch_name()
            birthdate = catch_birthdate()
            gender = catch_gender()
            height = catch_height()
            weight = catch_weight()
            
            # Restaura input original
            builtins.input = original_input
            
            # Salva no banco usando função ORIGINAL
            patient_id = create_patient(name, birthdate, height, weight, gender)
            
            # Mostra confirmação
            messagebox.showinfo("Success", 
                              f"Patient successfully checked-in!\nPatient ID: {patient_id}\nName: {name}")
            self.window.destroy()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error saving patient: {str(e)}")

class ListPatientsWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("List of Patients")
        self.window.geometry("500x400")
        
        self.setup_list()
    
    def setup_list(self):
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="-----------( LIST OF PATIENTS )------------", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Treeview para lista de pacientes
        tree_frame = ttk.Frame(main_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        columns = ('ID', 'Name', 'Birthdate', 'Gender')
        self.tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Carrega os dados
        self.load_patients()
        
        ttk.Button(main_frame, text="Close", command=self.window.destroy).pack(pady=10)
    
    def load_patients(self):
        # Usa função ORIGINAL para listar pacientes
        patients = patient_database.list_all_patients()
        
        if not patients:
            self.tree.insert('', 'end', values=("No patients", "checked-in", "", ""))
            return
        
        for patient in patients:
            self.tree.insert('', 'end', values=(
                patient.id,
                patient.name,
                patient.birthdate.strftime('%m/%d/%Y'),
                patient.gender
            ))

class PatientInfoWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Patient Information")
        self.window.geometry("500x400")
        
        self.setup_ui()
    
    def setup_ui(self):
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="-----------( INFORMATION OF THE PATIENTS )------------", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Frame para entrada de ID
        id_frame = ttk.Frame(main_frame)
        id_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(id_frame, text="Patient ID:").pack(side=tk.LEFT)
        self.id_var = tk.StringVar()
        ttk.Entry(id_frame, textvariable=self.id_var, width=10).pack(side=tk.LEFT, padx=5)
        ttk.Button(id_frame, text="Search", command=self.search_patient).pack(side=tk.LEFT, padx=5)
        
        # Área de informações
        self.info_text = tk.Text(main_frame, height=15, width=50)
        self.info_text.pack(fill=tk.BOTH, expand=True, pady=10)
        
        ttk.Button(main_frame, text="Close", command=self.window.destroy).pack()
    
    def search_patient(self):
        try:
            patient_id = int(self.id_var.get())
            # Usa função ORIGINAL para buscar paciente
            patient = patient_database.get_patient_by_id(patient_id)
            
            self.info_text.delete(1.0, tk.END)
            
            if patient:
                # Usa método ORIGINAL para display
                cmi_value = patient.calculate_cmi()
                classification = patient.cmi_classification()
                
                info = f"""--- Patient information ---
ID: {patient.id}
Name: {patient.name}
Date of birth: {patient.birthdate.strftime('%m/%d/%Y')}
Age: {patient.age} years
Height: {patient.height:.2f}m
Weight: {patient.weight:.2f}kg
Gender: {patient.gender}

Corporal Mass Index (CMI): {cmi_value:.2f} - {classification}
Basal Metabolic Rate (BMR): {patient.calculate_bmr():.2f} calories"""
                
                self.info_text.insert(1.0, info)
            else:
                self.info_text.insert(1.0, "Patient not found!")
                
        except ValueError:
            messagebox.showerror("Error", "Invalid ID!")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

class DeletePatientWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Delete Patient")
        self.window.geometry("500x400")
        
        self.setup_ui()
    
    def setup_ui(self):
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="-----------( DELETE PATIENT )------------", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Frame para entrada de ID
        id_frame = ttk.Frame(main_frame)
        id_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(id_frame, text="Patient ID to delete:").pack(side=tk.LEFT)
        self.id_var = tk.StringVar()
        ttk.Entry(id_frame, textvariable=self.id_var, width=10).pack(side=tk.LEFT, padx=5)
        ttk.Button(id_frame, text="Delete", command=self.delete_patient).pack(side=tk.LEFT, padx=5)
        
        # Lista de pacientes
        tree_frame = ttk.Frame(main_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        columns = ('ID', 'Name')
        self.tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.load_patients()
        
        ttk.Button(main_frame, text="Close", command=self.window.destroy).pack(pady=10)
    
    def load_patients(self):
        patients = patient_database.list_all_patients()
        
        if not patients:
            self.tree.insert('', 'end', values=("No patients", "checked-in"))
            return
        
        for patient in patients:
            self.tree.insert('', 'end', values=(patient.id, patient.name))
    
    def delete_patient(self):
        try:
            patient_id = int(self.id_var.get())
            
            # Confirmação
            confirm = messagebox.askyesno("Confirm", 
                                        f"Are you sure you want to delete patient {patient_id}?")
            
            if confirm:
                # Usa função ORIGINAL para deletar
                if patient_database.delete_patient(patient_id):
                    messagebox.showinfo("Success", "Patient has been successfully deleted!")
                    self.load_patients()  # Recarrega a lista
                else:
                    messagebox.showerror("Error", "Patient not found!")
                    
        except ValueError:
            messagebox.showerror("Error", "Invalid ID!")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

def show_main_menu():
    app = MainMenu()
    app.run()
    
    