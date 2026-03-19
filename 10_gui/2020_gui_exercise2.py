""" Opgave "GUI step 2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

padx = 10
pady = 10

# Frame
frame = tk.LabelFrame(main_window, text="Container")
frame.grid(row=0, column=0, padx=padx, pady=pady)


# Labels
label = tk.Label(frame, text="Id")
label.grid(row=1, column=1, padx=padx, pady=pady)

label = tk.Label(frame, text="Weight")
label.grid(row=1, column=2, padx=padx, pady=pady)

label = tk.Label(frame, text="Destination")
label.grid(row=1, column=3, padx=padx, pady=pady)

label = tk.Label(frame, text="Weather")
label.grid(row=1, column=4, padx=padx, pady=pady)

# Entrys
entry = tk.Entry(frame, width=4)
entry.grid(row=2, column=1, padx=padx, pady=pady)
entry.insert(0, "")

entry = tk.Entry(frame, width=8)
entry.grid(row=2, column=2, padx=padx, pady=pady)
entry.insert(0, "")

entry = tk.Entry(frame, width=20)
entry.grid(row=2, column=3, padx=padx, pady=pady)
entry.insert(0, "")

entry = tk.Entry(frame, width=14)
entry.grid(row=2, column=4, padx=padx, pady=pady)
entry.insert(0, "")

# Buttons
button = tk.Button(frame, text="Create")
button.grid(row=3, column=1, padx=padx, pady=pady)

button = tk.Button(frame, text="Update")
button.grid(row=3, column=2, padx=padx, pady=pady)

button = tk.Button(frame, text="Delete")
button.grid(row=3, column=3, padx=padx, pady=pady)

button = tk.Button(frame, text="Clear Entry Boxes")
button.grid(row=3, column=4, padx=padx, pady=pady)


if __name__ == "__main__":
    main_window.mainloop()
