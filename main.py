'''
>>>>>>>   UNESC (UNIVERSITARY CENTER OF ESPIRITO SANTO)
>>>>>>>   CREATED BY: VINÍCIUS DE SOUZA BOY (STUDENT) 2nd PERIOD
'''
import tkinter as tk
root = tk.Tk()

root.title('Unesc Saúde')
root.geometry('400x400')
root.mainloop()

import view.menu as menu
import patient_database

def main():
    # Initialize database
    patient_database.init_database()
    menu.show_menu()

if __name__ == '__main__':
    main()