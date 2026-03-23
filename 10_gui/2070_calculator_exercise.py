"""Opgave "Calculator with GUI"

Løs opgave 0700_calculator_exercise.py med en GUI

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""
import tkinter as tk
from tkinter import ttk


main_window = tk.Tk()
main_window.title('Calculator')
main_window.geometry("600x700")

padx = 10
pady = 10


number_frame = tk.LabelFrame(main_window,)
number_frame.grid(row=2, rowspan=6, column=0, columnspan=2)

operator_frame = tk.LabelFrame(main_window)
operator_frame.grid(row=2, rowspan=7, column=2)

other_frame = tk.LabelFrame(main_window)
other_frame.grid(row=1, column=0, columnspan=2)


entry = tk.Entry(main_window, width=40)
entry.grid(row=0, column=0, columnspan=5)
entry.insert(0, "")


zero_button = tk.Button(number_frame, text="0")
zero_button.grid(row=5, column=1)

one_button = tk.Button(number_frame, text="1")
one_button.grid(row=4, column=0)

two_button = tk.Button(number_frame, text="2")
two_button.grid(row=4, column=1)

three_button = tk.Button(number_frame, text="3")
three_button.grid(row=4, column=2)

four_button = tk.Button(number_frame, text="4")
four_button.grid(row=3, column=0)

five_button = tk.Button(number_frame, text="5")
five_button.grid(row=3, column=1)

six_button = tk.Button(number_frame, text="6")
six_button.grid(row=3, column=2)

seven_button = tk.Button(number_frame, text="7")
seven_button.grid(row=2, column=0)

eight_button = tk.Button(number_frame, text="8")
eight_button.grid(row=2, column=1)

nine_button = tk.Button(number_frame, text="9")
nine_button.grid(row=2, column=2)

period_button = tk.Button(number_frame, text=".")
period_button.grid(row=5, column=0)

equals_button = tk.Button(operator_frame, text="=")
equals_button.grid(row=5, column=3)

plus_button = tk.Button(operator_frame, text="+")
plus_button.grid(row=4, column=3)

minus_button = tk.Button(operator_frame, text="-")
minus_button.grid(row=3, column=3)

multiply_button = tk.Button(operator_frame, text="*")
multiply_button.grid(row=2, column=3)

devide_button = tk.Button(operator_frame, text="/")
devide_button.grid(row=1, column=3)

reset_button = tk.Button(other_frame, text="CE")
reset_button.grid(row=1, column=0)

delete_button = tk.Button(other_frame, text="DEL")
delete_button.grid(row=1, column=1)























if __name__ == "__main__":
    main_window.mainloop()