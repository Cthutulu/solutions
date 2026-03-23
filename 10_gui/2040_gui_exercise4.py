""" Opgave "GUI step 4":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2040.png

Genbrug din kode fra "GUI step 3".

Fyld treeview'en med testdata.
Leg med farveværdierne. Find en farvekombination, som du kan lide.

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).
    Hvis du klikker på en datarække i træoversigten, kopieres dataene i denne række til indtastningsfelterne.

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
odd_row = "antiquewhite"
even_row = "bisque2"


def empty_entry():
    print("Clear Entry Boxes was pressed")
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)

def read_table(tree):
    count = 0
    for record in test_data_list:
        if count % 2 == 0:
            tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
        else:
            tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
        count += 1

def edit_records(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    entry1.delete(0, tk.END)
    entry1.insert(0, values[0])
    entry2.delete(0, tk.END)
    entry2.insert(0, values[1])
    entry3.delete(0, tk.END)
    entry3.insert(0, values[2])



test_data_list = []
test_data_list.append(("1", "1000", "oslo"))
test_data_list.append(("2", "2000", "chicago"))
test_data_list.append(("3", "3000", "milano"))
test_data_list.append(("4", "4000", "amsterdam"))


# Frame
frame = tk.LabelFrame(main_window, text="frame")
frame.grid(row=0, column=0, padx=padx, pady=pady)

frame3 = tk.LabelFrame(frame)
frame3.grid(row=0, column=0, padx=padx, pady=pady)

frame1 = tk.LabelFrame(frame)
frame1.grid(row=3, column=0, padx=padx, pady=pady)

frame2 = tk.LabelFrame(frame)
frame2.grid(row=4, column=0, padx=padx, pady=pady)

# Style
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

"Treeview & Scrollbar"
tree_scrollbar = tk.Scrollbar(frame3)
tree_scrollbar.grid(row=1, column=6, padx=padx, pady=pady, sticky='ns')
tree = ttk.Treeview(frame3, yscrollcommand=tree_scrollbar.set, selectmode="browse")
tree.grid(row=1, column=1, columnspan=5, padx=0, pady=pady)
tree_scrollbar.config(command=tree.yview)

tree['columns'] = ("col1", "col2", "col3")
tree.column("#0", width=0, stretch=tk.NO)
tree.column("col1", anchor=tk.E, width=40)
tree.column("col2", anchor=tk.W, width=80)
tree.column("col3", anchor=tk.W, width=180)

tree.heading("#0", text="", anchor=tk.W)
tree.heading("col1", text="Id", anchor=tk.CENTER)
tree.heading("col2", text="Weight", anchor=tk.CENTER)
tree.heading("col3", text="Destination", anchor=tk.CENTER)

tree.tag_configure('oddrow', background=odd_row)
tree.tag_configure('evenrow', background=even_row)

tree.bind("<ButtonRelease-1>", lambda event: edit_records(event, tree))

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


read_table(tree)

if __name__ == "__main__":
    main_window.mainloop()