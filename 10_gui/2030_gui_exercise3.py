"""Opgave "GUI step 3":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2030.png

Genbrug din kode fra "GUI step 2".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                treeview and scrollbar
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
from tkinter import ttk


main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

padx = 10
pady = 10
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#773333"

def empty_entry():
    print("Clear Entry Boxes was pressed")
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)

# Frame
frame = tk.LabelFrame(main_window, text="frame")
frame.grid(row=0, column=0, padx=padx, pady=pady)

frame3 = tk.LabelFrame(frame)
frame3.grid(row=0, column=0, padx=padx, pady=pady)

frame1 = tk.LabelFrame(frame)
frame1.grid(row=3, column=0, padx=padx, pady=pady)

frame2 = tk.LabelFrame(frame, text="frame2")
frame2.grid(row=4, column=0, padx=padx, pady=pady)

# Style
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

"Treeview & Scrollbar"
# tree_scrollbar = tk.Scrollbar(frame)
# tree_scrollbar.grid(row=1, column=4, padx=padx, pady=pady, sticky='ns')
# tree = ttk.Treeview(frame, yscrollcommand=tree_scrollbar.set, selectmode="browse")
# tree.grid(row=1, column=1, columnspan=3, padx=0, pady=pady)
# tree_scrollbar.config(command=tree.yview)

tree_scrollbar = tk.Scrollbar(frame3)  # define the scrollbar
tree_scrollbar.grid(row=1, column=6, padx=padx, pady=pady, sticky='ns')  # place the scrollbar
tree = ttk.Treeview(frame3, yscrollcommand=tree_scrollbar.set, selectmode="browse")  # define the treeview, connect it with the scrollbar
tree.grid(row=1, column=1, columnspan=5, padx=0, pady=pady)  # place the treeview
tree_scrollbar.config(command=tree.yview)  # connect the scrollbar with the treeview

tree['columns'] = ("col1", "col2", "col3")
tree.column("#0", width=0, stretch=tk.NO)
tree.column("col1", anchor=tk.E, width=40)
tree.column("col2", anchor=tk.W, width=80)
tree.column("col3", anchor=tk.W, width=180)

tree.heading("#0", text="", anchor=tk.W)
tree.heading("col1", text="Id", anchor=tk.CENTER)
tree.heading("col2", text="Weight", anchor=tk.CENTER)
tree.heading("col3", text="Destination", anchor=tk.CENTER)

# Labels
label = tk.Label(frame1, text="Id")
label.grid(row=2, column=1, padx=padx, pady=pady)

label = tk.Label(frame1, text="Weight")
label.grid(row=2, column=2, padx=padx, pady=pady)

label = tk.Label(frame1, text="Destination")
label.grid(row=2, column=3, padx=padx, pady=pady)

label = tk.Label(frame1, text="Weather")
label.grid(row=2, column=4, padx=padx, pady=pady)

# Entrys
entry1 = tk.Entry(frame1, width=4)
entry1.grid(row=3, column=1, padx=padx, pady=pady)
entry1.insert(0, "")

entry2 = tk.Entry(frame1, width=8)
entry2.grid(row=3, column=2, padx=padx, pady=pady)
entry2.insert(0, "")

entry3 = tk.Entry(frame1, width=20)
entry3.grid(row=3, column=3, padx=padx, pady=pady)
entry3.insert(0, "")

entry4 = tk.Entry(frame1, width=14)
entry4.grid(row=3, column=4, padx=padx, pady=pady)
entry4.insert(0, "")

# Buttons
create_button = tk.Button(frame2, text="Create")
create_button.grid(row=4, column=1, padx=padx, pady=pady)

update_button = tk.Button(frame2, text="Update")
update_button.grid(row=4, column=2, padx=padx, pady=pady)

delete_button = tk.Button(frame2, text="Delete")
delete_button.grid(row=4, column=3, padx=padx, pady=pady)

empty_entry_button = tk.Button(frame2, text="Clear Entry Boxes", command=empty_entry)
empty_entry_button.grid(row=4, column=4, padx=padx, pady=pady)


if __name__ == "__main__":
    main_window.mainloop()
