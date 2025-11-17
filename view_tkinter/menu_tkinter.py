import tkinter as tk
from tkinter import ttk, messagebox
import patient_database
from controller.patient_class import Patient
from datetime import datetime



#  FUNÇÃO DE DEGRADÊ 

def create_gradient(frame, color1="#bbdefb", color2="#ffffff"):
    frame.update_idletasks()
    width = frame.winfo_width()
    height = frame.winfo_height()

    canvas = tk.Canvas(frame, width=width, height=height,
                       highlightthickness=0, bd=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)

    r1, g1, b1 = frame.winfo_rgb(color1)
    r2, g2, b2 = frame.winfo_rgb(color2)

    for i in range(height):
        r = int(r1 + (i * (r2 - r1) / height))
        g = int(g1 + (i * (g2 - g1) / height))
        b = int(b1 + (i * (b2 - b1) / height))
        color = f"#{r:04x}{g:04x}{b:04x}"
        canvas.create_line(0, i, width, i, fill=color)

    canvas.lower("all")



# ESTILO DOS BOTÕES

def setup_styles():
    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "Blue.TButton",
        foreground="white",
        background="#1976d2",
        borderwidth=0,          
        focusthickness=0,
        highlightthickness=0,
        relief="flat",
        padding=8,
        font=("Arial", 11, "bold")
    )

    style.map(
        "Blue.TButton",
        background=[("active", "#0d47a1")],
        relief=[("pressed", "flat"), ("active", "flat")]
    )

    style.configure("Title.TLabel",
                    font=("Arial", 17, "bold"),
                    foreground="#0d47a1",
                    background="#ffffff")


#  MENU PRINCIPAL


class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Pacientes - UNESC")
        self.root.state('zoomed')

        setup_styles()
        self.setup_ui()

    def setup_ui(self):

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        create_gradient(main_frame)

        title = tk.Label(main_frame, text="MENU PRINCIPAL",  font=("Arial", 17, "bold"),
        fg="#0d47a1", bg=None)
        title.pack(pady=20)

        buttons = [
            ("Check-in Patient", self.check_in_patient),
            ("List of Patients", self.list_patients),
            ("Patient Information", self.patient_information),
            ("Delete Patient", self.delete_patient),
            ("Exit", self.exit_app)
        ]

        for text, command in buttons:
            ttk.Button(main_frame,
                       text=text,
                       style="Blue.TButton",
                       command=command).pack(pady=8, ipadx=10)

    # CHAMADAS DOS BOTÕES

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



#  CHECK-IN WINDOW


class CheckInWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Check-in Patient")
        self.window.geometry("420x450")

        setup_styles()
        self.setup_form()

    def setup_form(self):

        frame = tk.Frame(self.window)
        frame.pack(fill=tk.BOTH, expand=True)

        frame.update_idletasks()
        create_gradient(frame)

        tk.Label(frame, text="CHECK-IN PATIENT", font=("Arial", 17, "bold"),
        fg="#0d47a1", bg=None).pack(pady=10)

        self.name_var = tk.StringVar()
        self.birthdate_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.height_var = tk.StringVar()
        self.weight_var = tk.StringVar()

        fields = [
            ("Name:", self.name_var),
            ("Birthdate (MM/DD/YYYY):", self.birthdate_var),
            ("Gender (M/F):", self.gender_var),
            ("Height (m):", self.height_var),
            ("Weight (kg):", self.weight_var),
        ]

        for label, var in fields:
            row = tk.Frame(frame, bg=frame["bg"])
            row.pack(pady=5, fill=tk.X, padx=20)
            tk.Label(row, text=label, width=25, bg=frame["bg"]).pack(side=tk.LEFT)
            tk.Entry(row,
                textvariable=var,
                width=25,
                relief="flat",
                highlightthickness=1,
                highlightbackground="#cccccc",
                highlightcolor="#1976d2",
            ).pack(side=tk.LEFT, ipady=3)
        
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=25)


        ttk.Button(btn_frame, text="Save", style="Blue.TButton",
                   command=self.save_patient).pack(side=tk.LEFT, padx=10)

        ttk.Button(btn_frame, text="Cancel", style="Blue.TButton",
                   command=self.window.destroy).pack(side=tk.LEFT, padx=10)

    def save_patient(self):
        try:
            from controller.bridge import catch_name, catch_birthdate, catch_gender, catch_height, catch_weight
            from patient_database import create_patient

            import builtins
            original_input = builtins.input

            inputs = [
                self.name_var.get(),
                self.birthdate_var.get(),
                self.gender_var.get(),
                self.height_var.get(),
                self.weight_var.get()
            ]

            it = iter(inputs)
            builtins.input = lambda prompt="": next(it)

            name = catch_name()
            birth = catch_birthdate()
            gender = catch_gender()
            height = catch_height()
            weight = catch_weight()

            builtins.input = original_input

            patient_id = create_patient(name, birth, height, weight, gender)

            messagebox.showinfo("Success", f"Patient registered!\nID: {patient_id}")
            self.window.destroy()

        except Exception as e:
            messagebox.showerror("Error", str(e))



#  LISTAR PACIENTES


class ListPatientsWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("List of Patients")
        self.window.geometry("600x450")

        setup_styles()
        self.setup_list()

    def setup_list(self):

        frame = tk.Frame(self.window)
        frame.pack(fill=tk.BOTH, expand=True)

        create_gradient(frame)

        ttk.Label(frame, text="LIST OF PATIENTS", style="Title.TLabel").pack(pady=15)

        tree_frame = ttk.Frame(frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=20)

        columns = ("ID", "Name", "Birthdate", "Gender")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)

        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.load_patients()

        ttk.Button(frame, text="Close", style="Blue.TButton",
                   command=self.window.destroy).pack(pady=10)

    def load_patients(self):
        patients = patient_database.list_all_patients()
        self.tree.delete(*self.tree.get_children())

        for p in patients:
            self.tree.insert("", "end",
                             values=(p.id, p.name, p.birthdate.strftime("%m/%d/%Y"), p.gender))



#  PATIENT INFO


class PatientInfoWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Patient Information")
        self.window.geometry("600x500")

        setup_styles()
        self.setup_ui()

    def setup_ui(self):

        frame = tk.Frame(self.window)
        frame.pack(fill=tk.BOTH, expand=True)

        create_gradient(frame)

        ttk.Label(frame, text="PATIENT INFORMATION", style="Title.TLabel").pack(pady=15)

        id_frame = ttk.Frame(frame)
        id_frame.pack(pady=10)

        ttk.Label(id_frame, text="Patient ID:").pack(side=tk.LEFT)
        self.id_var = tk.StringVar()
        ttk.Entry(id_frame, textvariable=self.id_var, width=10).pack(side=tk.LEFT, padx=5)

        ttk.Button(id_frame, text="Search", style="Blue.TButton",
                   command=self.search_patient).pack(side=tk.LEFT, padx=8)

        self.text = tk.Text(frame, height=15, width=70)
        self.text.pack(pady=15)

        ttk.Button(frame, text="Close", style="Blue.TButton",
                   command=self.window.destroy).pack()

    def search_patient(self):
        try:
            pid = int(self.id_var.get())
            patient = patient_database.get_patient_by_id(pid)

            self.text.delete(1.0, tk.END)

            if not patient:
                self.text.insert(tk.END, "Patient not found!")
                return

            info = f"""
--- Patient Information ---
ID: {patient.id}
Name: {patient.name}
Birthdate: {patient.birthdate.strftime('%m/%d/%Y')}
Age: {patient.age}
Height: {patient.height:.2f}
Weight: {patient.weight:.2f}
Gender: {patient.gender}

CMI: {patient.calculate_cmi():.2f} ({patient.cmi_classification()})
BMR: {patient.calculate_bmr():.2f} calories
"""
            self.text.insert(tk.END, info)

        except:
            messagebox.showerror("Error", "Invalid ID!")



#  DELETE PATIENT


class DeletePatientWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Delete Patient")
        self.window.geometry("600x450")

        setup_styles()
        self.setup_ui()

    def setup_ui(self):

        frame = tk.Frame(self.window)
        frame.pack(fill=tk.BOTH, expand=True)

        create_gradient(frame)

        ttk.Label(frame, text="DELETE PATIENT", style="Title.TLabel").pack(pady=15)

        id_frame = ttk.Frame(frame)
        id_frame.pack(pady=10)

        ttk.Label(id_frame, text="Patient ID:").pack(side=tk.LEFT)
        self.id_var = tk.StringVar()
        ttk.Entry(id_frame, textvariable=self.id_var, width=10).pack(side=tk.LEFT, padx=5)

        ttk.Button(id_frame, text="Delete",
                   style="Blue.TButton",
                   command=self.delete_patient).pack(side=tk.LEFT, padx=8)

        tree_frame = ttk.Frame(frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=20)

        columns = ("ID", "Name")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.load_patients()

        ttk.Button(frame, text="Close", style="Blue.TButton",
                   command=self.window.destroy).pack(pady=10)

    def load_patients(self):
        self.tree.delete(*self.tree.get_children())
        patients = patient_database.list_all_patients()

        for p in patients:
            self.tree.insert("", "end", values=(p.id, p.name))

    def delete_patient(self):
        try:
            pid = int(self.id_var.get())

            if messagebox.askyesno("Confirm", "Are you sure you want to delete this patient?"):
                if patient_database.delete_patient(pid):
                    messagebox.showinfo("Success", "Patient deleted!")
                    self.load_patients()
                else:
                    messagebox.showerror("Error", "Patient not found!")

        except:
            messagebox.showerror("Error", "Invalid ID!")



#  RUN APP


def show_main_menu():
    app = MainMenu()
    app.run()