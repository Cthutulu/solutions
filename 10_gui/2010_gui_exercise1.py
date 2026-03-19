"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

padx = 25
pady = 10

frame = tk.LabelFrame(main_window, text="Container")
frame.grid(row=0, column=0, padx=padx, pady=pady)

label = tk.Label(frame, text="Id")
label.grid(row=1, column=1, padx=padx, pady=pady)

entry = tk.Entry(frame, width=4)
entry.grid(row=2, column=1, padx=padx, pady=pady)
entry.insert(0, "")

button = tk.Button(frame, text="Create")
button.grid(row=3, column=1, padx=padx, pady=pady)











if __name__ == "__main__":
    main_window.mainloop()
