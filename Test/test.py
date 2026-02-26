import tkinter as tk

# Create main window
root = tk.Tk()
root.title("My First Desktop App")
root.geometry("300x200")

# Add a label
label = tk.Label(root, text="Hello, PyCharm!", font=("Arial", 14))
label.pack(pady=20)

# Add a button
def on_click():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

# Run the app
root.mainloop()
