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

def empty_entry():
    print("Clear Entry Boxes was pressed")
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)

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
entry1 = tk.Entry(frame, width=4)
entry1.grid(row=2, column=1, padx=padx, pady=pady)
entry1.insert(0, "")

entry2 = tk.Entry(frame, width=8)
entry2.grid(row=2, column=2, padx=padx, pady=pady)
entry2.insert(0, "")

entry3 = tk.Entry(frame, width=20)
entry3.grid(row=2, column=3, padx=padx, pady=pady)
entry3.insert(0, "")

entry4 = tk.Entry(frame, width=14)
entry4.grid(row=2, column=4, padx=padx, pady=pady)
entry4.insert(0, "")

# Buttons
create_button = tk.Button(frame, text="Create")
create_button.grid(row=3, column=1, padx=padx, pady=pady)

update_button = tk.Button(frame, text="Update")
update_button.grid(row=3, column=2, padx=padx, pady=pady)

delete_button = tk.Button(frame, text="Delete")
delete_button.grid(row=3, column=3, padx=padx, pady=pady)

empty_entry_button = tk.Button(frame, text="Clear Entry Boxes", command=empty_entry)
empty_entry_button.grid(row=3, column=4, padx=padx, pady=pady)


if __name__ == "__main__":
    main_window.mainloop()
