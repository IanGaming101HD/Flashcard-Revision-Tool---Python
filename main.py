import os
import json
from tkinter import Tk, messagebox, Label, Text, filedialog, Button

global window, folder

window = Tk()

try:
    file = open('config.json', 'r')
    data = json.load(file)
except:
    data = {}

if (not data['path'] or data['path'] == ''):
    folder = f'{os.path.dirname(__file__)}\Flashcards'
else:
    try:
        open(rf'' + data['path'], 'r')
    except:
        folder = f'{os.path.dirname(__file__)}\Flashcards'
    else:
        folder = data['path']
with open('config.json', 'w', encoding = 'utf-8') as f:
    data['path'] = folder
    json.dump(data, f, ensure_ascii = False, indent = 4) 

def clear_frame(window):
    for widgets in window.winfo_children():
        widgets.destroy()

def main_menu_window():
    clear_frame(window)
    background_color = 'GREY20'
    x, y = 1000, 600
    
    window.title('Flashcards Revision Tool')
    # window.wm_attributes('-toolwindow', 'True')
    window.configure(bg = background_color)
    window.geometry(f'{x}x{y}')

    def start_session(background_color):
        try:
            file = open(rf'{folder}\cards.json', 'r')
            cards = json.load(file)
        except:
            cards = []

        def show_hide_answer(widget, bg, button):
            global value
            if (value == 0):
                widget.config(fg = 'WHITE')
                button.config(text = 'Hide Answer')
                value = 1
            else:
                widget.config(fg = bg)
                button.config(text = 'Show Answer')
                value = 0

        def card(x):
            global value
            value = 0

            clear_frame(window)

            if (x > (len(cards) - 1)):
                label = Label(window, text = 'There are no more cards left!\nTo add more cards select \"Main Menu\"\nand to restart the flash cards select \"Retry\".', bg = background_color, fg = 'WHITE', font = ('Arial Bold', 30))
                main_menu_button = Button(window, text = 'Main Menu', padx = 125, bg = 'ROYALBLUE3', fg = 'WHITE', activebackground = 'ROYALBLUE4', activeforeground = 'WHITE', borderwidth = 0, pady = 5, font = ('Arial Bold', 10), command = lambda: main_menu_window())    
                retry_button = Button(window, text = 'Retry', padx = 125, bg = 'ROYALBLUE3', fg = 'WHITE', activebackground = 'ROYALBLUE4', activeforeground = 'WHITE', borderwidth = 0, pady = 5, font = ('Arial Bold', 10), command = lambda: card(0))
                
                label.place(relx = 0.5, y = 250, anchor = 'center')
                main_menu_button.place(relx = 0.405, y = 350, anchor = 'center', height = 40, width = 150)
                retry_button.place(relx = 0.595, y = 350, anchor = 'center', height = 40, width = 150)
                return None

            first_label = Label(window, text = cards[x][0], bg = background_color, fg = 'WHITE', font = ('Arial Bold', 50))
            second_label = Label(window, text = cards[x][1], bg = background_color, fg = background_color, font = ('Arial Bold', 25))
            show_hide_answer_button = Button(window, text = 'Show Answer', padx = 125, bg = 'ROYALBLUE3', fg = 'WHITE', activebackground = 'ROYALBLUE4', activeforeground = 'WHITE', borderwidth = 0, pady = 5, font = ('Arial Bold', 10), command = lambda: show_hide_answer(second_label, background_color, show_hide_answer_button))
            main_menu_button = Button(window, text = 'Main Menu', padx = 125, bg = 'ROYALBLUE3', fg = 'WHITE', activebackground = 'ROYALBLUE4', activeforeground = 'WHITE', borderwidth = 0, pady = 5, font = ('Arial Bold', 10), command = lambda: main_menu_window())    
            next_button = Button(window, text = 'Next', padx = 125, bg = 'ROYALBLUE3', fg = 'WHITE', activebackground = 'ROYALBLUE4', activeforeground = 'WHITE', borderwidth = 0, pady = 5, font = ('Arial Bold', 10), command = lambda: card(x+1))
            
            first_label.place(relx = 0.5, y = 200, anchor = 'center')
            second_label.place(relx = 0.5, y = 250, anchor = 'center')
            show_hide_answer_button.place(relx = 0.5, y = 300, anchor = 'center', height = 40, width = 150)
            main_menu_button.place(relx = 0.405, y = 350, anchor = 'center', height = 40, width = 150)
            next_button.place(relx = 0.595, y = 350, anchor = 'center', height = 40, width = 150)
        card(0)

    def create_card(first_value, second_value):
        if (first_value == '' or second_value == ''):
            messagebox.showerror('Error', 'Fields cannot be empty!')
        else:
            try:
                file = open(rf'{folder}\cards.json', 'r')
                data = json.load(file)
            except:
                data = []

            if ([first_value, second_value] in data):
                return messagebox.showerror('Error', 'This card has already been added!')

            with open(rf'{folder}\cards.json', 'w', encoding = 'utf-8') as f:
                data.append([first_value, second_value])
                json.dump(data, f, ensure_ascii = False, indent = 4)
            messagebox.showinfo('Success', 'Card has been added!')

    if (window.attributes('-fullscreen') == True):
        window.overrideredirect(True)
    else:
        window.overrideredirect(False)
    
    def select_folder():
        global folder
        new_folder = filedialog.askdirectory(initialdir = folder, title = window.title())
        
        if (new_folder != ''):
            folder = new_folder
            with open('config.json', 'w', encoding = 'utf-8') as f:
                data['path'] = folder
                json.dump(data, f, ensure_ascii = False, indent = 4) 

    menu_label = Label(window, text = 'Menu', bg = background_color, fg = 'WHITE', font = ('Arial Bold', 40))
    create_card_label = Label(window, text = 'Create Card', bg = background_color, fg = 'WHITE', font = ('Arial Bold', 25))
    first_text_box = Text(window, bg = 'WHITE', fg = 'BLACK', font = ('Arial', 15))
    second_text_box = Text(window, bg = 'WHITE', fg = 'BLACK', font = ('Arial', 15)) 
    start_session_button = Button(window, text = 'Start Session', padx = 125, bg = 'ROYALBLUE3', fg = 'WHITE', activebackground = 'ROYALBLUE4', activeforeground = 'WHITE', borderwidth = 0, pady = 5, font = ('Arial Bold', 10), command = lambda: start_session(background_color))
    create_button = Button(window, text = 'Create', padx = 75, bg = 'ROYALBLUE3', fg = 'WHITE', activebackground = 'ROYALBLUE4', activeforeground = 'WHITE', borderwidth = 0, pady = 5, font = ('Arial Bold', 10), command = lambda: create_card(first_text_box.get('1.0','end-1c'), second_text_box.get('1.0','end-1c')))
    change_dir_button =  Button(window, text = 'Change Directory', bg = background_color, fg = 'WHITE', font = ('Arial Bold', 10), activeforeground = 'GRAY', activebackground = background_color, borderwidth = 0, command = select_folder)

    menu_label.place(relx = 0.5, y = 50, anchor = 'center')
    start_session_button.place(relx = 0.5, y = 115, anchor = 'center')
    create_card_label.place(relx = 0.5, y = 165, anchor = 'center')
    first_text_box.place(relx = 0.5, y = 210, anchor = 'center', height = 30, width = 500)
    second_text_box.place(relx = 0.5, y = 290, anchor = 'center', height = 100, width = 500)
    create_button.place(relx = 0.5, y = 370, anchor = 'center')
    change_dir_button.place(relx = 0.5, y = 400, anchor = 'center')

    first_text_box.configure(selectbackground = first_text_box.cget('bg'), inactiveselectbackground = first_text_box.cget('bg'))
    second_text_box.configure(selectbackground = second_text_box.cget('bg'), inactiveselectbackground = second_text_box.cget('bg'))

    window.mainloop()
main_menu_window()
