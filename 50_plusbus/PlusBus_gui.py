import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import PlusBus_data as pbd
import PlusBus_sql as pbsql
import PlusBus_func as pbf

main_window = tk.Tk()
main_window.title('PlusBus')
main_window.geometry("1200x500")

padx = 8
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#773333"
odd_row = "antiquewhite"
even_row = "bisque2"

# region customer functions
'''Customer Functions'''
# Read content of entry boxes
def read_customer_entries():
    return entry_customer_id.get(), entry_customer_surname.get(), entry_customer_phone_number.get(),

# Clear entry boxes
def clear_customer_entries():
    entry_customer_id.delete(0, tk.END)
    entry_customer_surname.delete(0, tk.END)
    entry_customer_phone_number.delete(0, tk.END)

def write_customer_entries(values):
    entry_customer_id.insert(0, values[0])
    entry_customer_surname.insert(0, values[1])
    entry_customer_phone_number.insert(0, values[2])

def edit_customer(_, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_customer_entries()
    write_customer_entries(values)

def create_customer(tree, record):
    customer = pbd.Customer.convert_from_tuple(record)
    pbsql.create_record(customer)
    clear_customer_entries()
    refresh_treeview(tree, pbd.Customer)

def update_customer(tree, record):
    customer = pbd.Customer.convert_from_tuple(record)
    pbsql.update_customer(customer)
    clear_customer_entries()
    refresh_treeview(tree, pbd.Customer)

def delete_customer(tree, record):
    customer = pbd.Customer.convert_from_tuple(record)
    pbsql.delete_customer(customer)
    clear_customer_entries()
    refresh_treeview(tree, pbd.Customer)
# endregion customer functions

# region journey functions
# def read_journey_entries():

# def clear_journey_entries():





#endregoin journey functions

# region common functions
'''Common Functions'''
def read_table(tree, class_):
    count = 0
    result = pbsql.select_all(class_)
    for record in result:
        if record.valid():
            if count % 2 == 0:  # even
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))
            else:  # odd
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))
            count += 1


def refresh_treeview(tree, class_):
    empty_treeview(tree)
    read_table(tree, class_)

def empty_treeview(tree):
    tree.delete(*tree.get_children())
# endregion common functions

# region Treeview
'''Treeview'''
#Style
style = ttk.Style()
style.theme_use('default')

style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])
# endregion Treeview


# region Treeview Customers
'''#Customers:'''
frame_customer = tk.LabelFrame(main_window, text="Customers")
frame_customer.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_frame_customer = tk.Frame(frame_customer)
tree_frame_customer.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_customer = tk.Scrollbar(tree_frame_customer)
tree_scroll_customer.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_customer = ttk.Treeview(tree_frame_customer, yscrollcommand=tree_scroll_customer.set, selectmode="browse")
tree_customer.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_customer.config(command=tree_customer.yview)

#
tree_customer['columns'] = ("id", "surname", "phone number")
tree_customer.column("#0", width=0, stretch=tk.NO)
tree_customer.column("id", anchor=tk.E, width=40)
tree_customer.column("surname", anchor=tk.E, width=140)
tree_customer.column("phone number", anchor=tk.W, width=160)
tree_customer.heading("#0", text="", anchor=tk.W)
tree_customer.heading("id", text="Id", anchor=tk.CENTER)
tree_customer.heading("surname", text="Surname", anchor=tk.CENTER)
tree_customer.heading("phone number", text="Phone Number", anchor=tk.CENTER)
tree_customer.tag_configure('oddrow', background=odd_row)
tree_customer.tag_configure('evenrow', background=even_row)

tree_customer.bind("<ButtonRelease-1>", lambda event: edit_customer(event, tree_customer))

controls_frame_customer = tk.Frame(frame_customer)
controls_frame_customer.grid(row=3, column=0, padx=padx, pady=pady)

edit_frame_customer = tk.Frame(controls_frame_customer)
edit_frame_customer.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for customer id
label_customer_id = tk.Label(edit_frame_customer, text="Id")
label_customer_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_customer_id = tk.Entry(edit_frame_customer, width=4, justify="right")
entry_customer_id.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for customer surnames
label_customer_surname = tk.Label(edit_frame_customer, text="Surname")
label_customer_surname.grid(row=0, column=1, padx=padx, pady=pady)
entry_customer_surname = tk.Entry(edit_frame_customer, width=14, justify="right")
entry_customer_surname.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for customer phone numbers
label_customer_phone_number = tk.Label(edit_frame_customer, text="Phone Number")
label_customer_phone_number.grid(row=0, column=2, padx=padx, pady=pady)
entry_customer_phone_number = tk.Entry(edit_frame_customer, width=16)
entry_customer_phone_number.grid(row=1, column=2, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_customer = tk.Frame(controls_frame_customer)
button_frame_customer.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_customer = tk.Button(button_frame_customer, text="Create", command=lambda: create_customer(tree_customer, read_customer_entries()))
button_create_customer.grid(row=0, column=1, padx=padx, pady=pady)
button_update_customer = tk.Button(button_frame_customer, text="Update", command=lambda: update_customer(tree_customer, read_customer_entries()))
button_update_customer.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_customer = tk.Button(button_frame_customer, text="Delete", command=lambda: delete_customer(tree_customer, read_customer_entries()))
button_delete_customer.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_customer, text="Clear Entry Boxes", command=clear_customer_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)
# endregion Customer Treeview

#region journey treeview
'''Journeys:'''
frame_journey = tk.LabelFrame(main_window, text="Journeys")
frame_journey.grid(row=0, column=1, padx=0, pady=0, sticky=tk.N)

tree_frame_journey = tk.Frame(frame_journey)
tree_frame_journey.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_journey = tk.Scrollbar(tree_frame_journey)
tree_scroll_journey.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_journey = ttk.Treeview(tree_frame_journey, yscrollcommand=tree_scroll_customer.set, selectmode="browse")
tree_journey.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_journey.config(command=tree_journey.yview)

tree_journey['columns'] = ("route", "date", "capacity")
tree_journey.column("#0", width=0, stretch=tk.NO)
tree_journey.column("route", anchor=tk.E, width=200)
tree_journey.column("date", anchor=tk.E, width=80)
tree_journey.column("capacity", anchor=tk.W, width=60)
tree_journey.heading("#0", text="", anchor=tk.W)
tree_journey.heading("route", text="Route", anchor=tk.CENTER)
tree_journey.heading("date", text="Date", anchor=tk.CENTER)
tree_journey.heading("capacity", text="Capacity", anchor=tk.CENTER)
tree_journey.tag_configure('oddrow', background=odd_row)
tree_journey.tag_configure('evenrow', background=even_row)

# tree_journey.bind("<ButtonRelease-1>", lambda event: edit_journey(event, tree_journey))

controls_frame_journey = tk.Frame(frame_journey)
controls_frame_journey.grid(row=3, column=0, padx=padx, pady=pady)

edit_frame_journey = tk.Frame(controls_frame_journey)
edit_frame_journey.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for customer id
label_journey_route = tk.Label(edit_frame_journey, text="Route")
label_journey_route.grid(row=0, column=0, padx=padx, pady=pady)
entry_journey_route = tk.Entry(edit_frame_journey, width=4, justify="right")
entry_journey_route.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for customer surnames
label_journey_date = tk.Label(edit_frame_journey, text="Date")
label_journey_date.grid(row=0, column=1, padx=padx, pady=pady)
entry_journey_date = tk.Entry(edit_frame_journey, width=14, justify="right")
entry_journey_date.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for customer phone numbers
label_journey_capacity = tk.Label(edit_frame_journey, text="Phone Number")
label_journey_capacity.grid(row=0, column=2, padx=padx, pady=pady)
entry_journey_capacity = tk.Entry(edit_frame_journey, width=16)
entry_journey_capacity.grid(row=1, column=2, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_journey = tk.Frame(controls_frame_journey)
button_frame_journey.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_journey = tk.Button(button_frame_journey, text="Create", command=lambda: create_customer(tree_customer, read_customer_entries()))
button_create_journey.grid(row=0, column=1, padx=padx, pady=pady)
button_update_journey = tk.Button(button_frame_journey, text="Update", command=lambda: update_customer(tree_customer, read_customer_entries()))
button_update_journey.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_journey = tk.Button(button_frame_journey, text="Delete", command=lambda: delete_customer(tree_customer, read_customer_entries()))
button_delete_journey.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_journey, text="Clear Entry Boxes", command=clear_customer_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)
#endregion journey treeview





if __name__ == "__main__":
    refresh_treeview(tree_customer, pbd.Customer)
    main_window.mainloop()