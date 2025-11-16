
#UNESC (UNIVERSITARY CENTER OF ESPIRITO SANTO)
#CREATED BY: VINÍCIUS DE SOUZA BOY (STUDENT) 2nd PERIOD


import patient_database
import tkinter as tk
from tkinter import messagebox, ttk
from view_tkinter.menu_tkinter import show_main_menu

def main():
    # Initialize database 
    patient_database.init_database()
    
    # initialize tkinter interface
    show_main_menu()

if __name__ == '__main__':
    main()