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

# def plus(self, other):
#     if len(self) > len(other):
#         longer = self
#         shorter = other
#     else:
#         shorter = self
#         longer = other
#
#     test = []
#     test2 = []
#
#     for x in range(1, len(longer) + 1):
#         if x <= len(shorter):
#             test.append([longer[-x], shorter[-x]])
#         else:
#             test.append([longer[-x]])
#
#         # print(test)
#
#         test2.append(max(test[-1]))
#         # print(test2)
#
#     result = LunarInt([*reversed(test2)])
#     return result


# def multiply(self, other):
#     if len(self) > len(other):
#         longer = self
#         shorter = other
#     else:
#         shorter = self
#         longer = other
#
#     test3 = []
#
#     for y in range(1, len(shorter) + 1):
#         current_digit = shorter[-y]
#
#         test = []
#         test2 = [0] * (y - 1)
#
#         for x in range(1, len(longer) + 1):
#             test.append([longer[-x], current_digit])
#
#             test2.append(min(test[-1]))
#
#         # print(test)
#         # print(test2)
#
#         test3.append(test2)
#         # print(test3)
#
#     result = LunarInt("0")
#
#     for p in test3:
#         result = result.plus(LunarInt([*reversed(p)]))
#
#     return result