import tkinter as tk
from random import randint


# Creating Window
root = tk.Tk()
root.wm_title('Roll the dice!')  # Setting window title
root.geometry('300x100')
root.resizable(False, False)  # Window should not be resized

# The widgets and functions
dice_value_label = tk.Label(master=root, text='', fg='black', bg='snow')  # Tkinter label to display dice roll number.
def roll_dice():
	dice_value_label['text'] = str(randint(1, 6))
roll_dice_button = tk.Button(master=root, text='Roll the dice!', fg='black', bg='snow', command=roll_dice)  # Button to roll dice.
dice_value_label.pack()
roll_dice_button.pack()

root.mainloop()  # Calling mainloop!
