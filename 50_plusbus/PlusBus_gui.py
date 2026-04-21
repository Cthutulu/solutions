import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import PlusBus_data as pbd
import PlusBus_sql as pbsql
import PlusBus_func as pbf

main_window = tk.Tk()
main_window.title('PlusBus')
main_window.geometry("1400x500")

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
    if not values:
        return
    clear_customer_entries()
    write_customer_entries(values)

    entry_booking_customer_id.delete(0, tk.END)
    entry_booking_customer_id.insert(0, values[0])

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
def read_journey_entries():
    return entry_journey_id.get(), entry_journey_route.get(), entry_journey_date.get(), entry_journey_capacity.get()

def clear_journey_entries():
    entry_journey_id.delete(0, tk.END)
    entry_journey_route.delete(0, tk.END)
    entry_journey_date.delete(0, tk.END)
    entry_journey_capacity.delete(0, tk.END)

def write_journey_entries(values):
    entry_journey_id.insert(0, values[0])
    entry_journey_route.insert(0, values[1])
    entry_journey_date.insert(0, values[2])
    entry_journey_capacity.insert(0, values[3])

def edit_journey(_, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    if not values:
        return
    clear_journey_entries()
    write_journey_entries(values)

    entry_booking_journey_id.delete(0, tk.END)
    entry_booking_journey_id.insert(0, values[0])
    entry_booking_route.delete(0, tk.END)
    entry_booking_route.insert(0, values[1])

def create_journey(tree, record):
    journey =pbd.Journey.convert_from_tuple(record)
    pbsql.create_record(journey)
    clear_journey_entries()
    refresh_treeview(tree, pbd.Journey)

def update_journey(tree, record):
    journey = pbd.Journey.convert_from_tuple(record)
    pbsql.update_journey(journey)
    clear_journey_entries()
    refresh_treeview(tree, pbd.Journey)

def delete_journey(tree, record):
    journey = pbd.Journey.convert_from_tuple(record)
    pbsql.delete_journey(journey)
    clear_journey_entries()
    refresh_treeview(tree, pbd.Journey)
#endregoin journey functions

# region bokking functions
def read_booking_entries():
    return entry_booking_journey_id.get(), entry_booking_route.get(), entry_booking_customer_id.get(), entry_booking_booked_seats.get()

def clear_booking_entries():
    entry_booking_id.delete(0, tk.END)
    entry_booking_journey_id.delete(0, tk.END)
    entry_booking_route.delete(0, tk.END)
    entry_booking_customer_id.delete(0, tk.END)
    entry_booking_booked_seats.delete(0, tk.END)

def write_booking_entries(values):
    entry_booking_journey_id.insert(0, values[1])
    entry_booking_route.insert(0, values[2])
    entry_booking_customer_id.insert(0, values[3])
    entry_booking_booked_seats.insert(0, values[4])

def edit_booking(_, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    if not values:
        return
    clear_booking_entries()
    write_booking_entries(values)
    entry_booking_id.delete(0, tk.END)
    entry_booking_id.insert(0, values[0])

def create_booking(tree, record):
    booking = pbd.Booking.convert_from_tuple((0, record[0], record[1], record[2], record[3]))
    pbsql.create_record(booking)
    clear_booking_entries()
    refresh_treeview(tree, pbd.Booking)

def update_booking(tree, record):
    booking = pbd.Booking.convert_from_tuple(
        (entry_booking_id.get(), record[0], record[1], record[2], record[3]))
    pbsql.update_booking(booking)
    clear_booking_entries()
    refresh_treeview(tree, pbd.Booking)

def delete_booking(tree, record):
    booking = pbd.Booking(id=entry_booking_id.get())
    pbsql.delete_booking(booking)
    clear_booking_entries()
    refresh_treeview(tree, pbd.Booking)

# endregion booking functions

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
tree_customer.column("id", anchor=tk.W, width=40)
tree_customer.column("surname", anchor=tk.W, width=140)
tree_customer.column("phone number", anchor=tk.E, width=160)
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
tree_journey = ttk.Treeview(tree_frame_journey, yscrollcommand=tree_scroll_journey.set, selectmode="browse")
tree_journey.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_journey.config(command=tree_journey.yview)

tree_journey['columns'] = ("id", "route", "date", "capacity")
tree_journey.column("#0", width=0, stretch=tk.NO)
tree_journey.column("id", anchor=tk.W, width=40)
tree_journey.column("route", anchor=tk.W, width=200)
tree_journey.column("date", anchor=tk.E, width=80)
tree_journey.column("capacity", anchor=tk.E, width=60)
tree_journey.heading("#0", text="", anchor=tk.W)
tree_journey.heading("id", text="id", anchor=tk.CENTER)
tree_journey.heading("route", text="Route", anchor=tk.CENTER)
tree_journey.heading("date", text="Date", anchor=tk.CENTER)
tree_journey.heading("capacity", text="Capacity", anchor=tk.CENTER)
tree_journey.tag_configure('oddrow', background=odd_row)
tree_journey.tag_configure('evenrow', background=even_row)

tree_journey.bind("<ButtonRelease-1>", lambda event: edit_journey(event, tree_journey))

controls_frame_journey = tk.Frame(frame_journey)
controls_frame_journey.grid(row=3, column=0, padx=padx, pady=pady)

edit_frame_journey = tk.Frame(controls_frame_journey)
edit_frame_journey.grid(row=0, column=0, padx=padx, pady=pady)

label_journey_id = tk.Label(edit_frame_journey, text="id")
label_journey_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_journey_id = tk.Entry(edit_frame_journey, width=5, justify="left")
entry_journey_id.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for customer id
label_journey_route = tk.Label(edit_frame_journey, text="Route")
label_journey_route.grid(row=0, column=1, padx=padx, pady=pady)
entry_journey_route = tk.Entry(edit_frame_journey, width=30, justify="left")
entry_journey_route.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for customer surnames
label_journey_date = tk.Label(edit_frame_journey, text="Date")
label_journey_date.grid(row=0, column=2, padx=padx, pady=pady)
entry_journey_date = tk.Entry(edit_frame_journey, width=10, justify="right")
entry_journey_date.grid(row=1, column=2, padx=padx, pady=pady)
# label and entry for customer phone numbers
label_journey_capacity = tk.Label(edit_frame_journey, text="capacity")
label_journey_capacity.grid(row=0, column=3, padx=padx, pady=pady)
entry_journey_capacity = tk.Entry(edit_frame_journey, width=5)
entry_journey_capacity.grid(row=1, column=3, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_journey = tk.Frame(controls_frame_journey)
button_frame_journey.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_journey = tk.Button(button_frame_journey, text="Create", command=lambda: create_journey(tree_journey, read_journey_entries()))
button_create_journey.grid(row=0, column=1, padx=padx, pady=pady)
button_update_journey = tk.Button(button_frame_journey, text="Update", command=lambda: update_journey(tree_journey, read_journey_entries()))
button_update_journey.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_journey = tk.Button(button_frame_journey, text="Delete", command=lambda: delete_journey(tree_journey, read_journey_entries()))
button_delete_journey.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_journey, text="Clear Entry Boxes", command=clear_journey_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)
#endregion journey treeview

# region Booking
'''Bookings:'''
frame_booking = tk.LabelFrame(main_window, text="Bookings")
frame_booking.grid(row=0, column=2, padx=0, pady=0, sticky=tk.N)

tree_frame_booking = tk.Frame(frame_booking)
tree_frame_booking.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_booking = tk.Scrollbar(tree_frame_booking)
tree_scroll_booking.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_booking = ttk.Treeview(tree_frame_booking, yscrollcommand=tree_scroll_booking.set, selectmode="browse")
tree_booking.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_booking.config(command=tree_booking.yview)

tree_booking['columns'] = ("id", "journey_id", "route", "customer_id", "booked_seats")
tree_booking.column("#0", width=0, stretch=tk.NO)
tree_booking.column("id", width=0, stretch=tk.NO)
tree_booking.column("journey_id", anchor=tk.W, width=40)
tree_booking.column("route", anchor=tk.W, width=200)
tree_booking.column("customer_id", anchor=tk.E, width=40)
tree_booking.column("booked_seats", anchor=tk.W, width=60)
tree_booking.heading("id", text="")
tree_booking.heading("#0", text="", anchor=tk.W)
tree_booking.heading("journey_id", text="Journey ID", anchor=tk.CENTER)
tree_booking.heading("route", text="Route", anchor=tk.CENTER)
tree_booking.heading("customer_id", text="Customer ID", anchor=tk.CENTER)
tree_booking.heading("booked_seats", text="Booked Seats", anchor=tk.CENTER)
tree_booking.tag_configure('oddrow', background=odd_row)
tree_booking.tag_configure('evenrow', background=even_row)

tree_booking.bind("<ButtonRelease-1>", lambda event: edit_booking(event, tree_booking))

controls_frame_booking = tk.Frame(frame_booking)
controls_frame_booking.grid(row=3, column=0, padx=padx, pady=pady)

edit_frame_booking = tk.Frame(controls_frame_booking)
edit_frame_booking.grid(row=0, column=0, padx=padx, pady=pady)

label_booking_id = tk.Label(edit_frame_booking, text="Booking ID")
label_booking_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_booking_id = tk.Entry(edit_frame_booking, width=5, justify="right")
entry_booking_id.grid(row=1, column=0, padx=padx, pady=pady)
label_booking_journey_id = tk.Label(edit_frame_booking, text="Journey ID")
label_booking_journey_id.grid(row=0, column=1, padx=padx, pady=pady)
entry_booking_journey_id = tk.Entry(edit_frame_booking, width=5, justify="left")
entry_booking_journey_id.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for customer id
label_booking_route = tk.Label(edit_frame_booking, text="Route")
label_booking_route.grid(row=0, column=2, padx=padx, pady=pady)
entry_booking_route = tk.Entry(edit_frame_booking, width=30, justify="left")
entry_booking_route.grid(row=1, column=2, padx=padx, pady=pady)
# label and entry for customer surnames
label_booking_customer_id = tk.Label(edit_frame_booking, text="Customer ID")
label_booking_customer_id.grid(row=0, column=3, padx=padx, pady=pady)
entry_booking_customer_id = tk.Entry(edit_frame_booking, width=5, justify="right")
entry_booking_customer_id.grid(row=1, column=3, padx=padx, pady=pady)
# label and entry for customer phone numbers
label_booking_booked_seats = tk.Label(edit_frame_booking, text="Booked Seats")
label_booking_booked_seats.grid(row=0, column=4, padx=padx, pady=pady)
entry_booking_booked_seats = tk.Entry(edit_frame_booking, width=5)
entry_booking_booked_seats.grid(row=1, column=4, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_booking = tk.Frame(controls_frame_booking)
button_frame_booking.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_booking = tk.Button(button_frame_booking, text="Create", command=lambda: create_booking(tree_booking, read_booking_entries()))
button_create_booking.grid(row=0, column=1, padx=padx, pady=pady)
button_update_booking = tk.Button(button_frame_booking, text="Update", command=lambda: update_booking(tree_booking, read_booking_entries()))
button_update_booking.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_booking = tk.Button(button_frame_booking, text="Delete", command=lambda: delete_booking(tree_booking, read_booking_entries()))
button_delete_booking.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_booking, text="Clear Entry Boxes", command=clear_booking_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)
# endregion booking



if __name__ == "__main__":
    refresh_treeview(tree_customer, pbd.Customer)
    refresh_treeview(tree_journey, pbd.Journey)
    refresh_treeview(tree_booking, pbd.Booking)
    main_window.mainloop()