import os
from controller.parses import parse_show_menu
from view.view import show_menu_display
import tkinter as tk



def show_menu():
    from patient_database import init_database
    init_database()
    
    while True:
        os.system('cls')
        show_menu_display()
        
        
        menu_choice = input('Select an option to access: ')
        parse_show_menu(menu_choice)






