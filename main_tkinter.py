'''
UNESC (UNIVERSITARY CENTER OF ESPIRITO SANTO)
CREATED BY: VINÍCIUS DE SOUZA BOY (STUDENT) 2nd PERIOD
'''

import patient_database
import tkinter as tk
from tkinter import messagebox, ttk
from view_tkinter.menu_tkinter import show_main_menu

def main():
    # Initialize database (código original mantido)
    patient_database.init_database()

    window = tk.Tk()


    window.title("Unesc Saúde")
    window.geometry("400x400")
    window.resizable(False, False)
    
    # Inicia interface Tkinter
    show_main_menu()

if __name__ == '__main__':
    main()
