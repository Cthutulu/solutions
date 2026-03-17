import tkinter as tk
import random
import math

fake_buttons = []
spawning = False
cheat_mode = False

# -------------------------
# CHEAT SYSTEM
# -------------------------

def toggle_cheat(event):
    global cheat_mode

    # Check if Ctrl + Shift are pressed
    if (event.state & 0x4) and (event.state & 0x1):
        cheat_mode = not cheat_mode

        if cheat_mode:
            print("Cheat mode ON")
            real_button.config(text="Go ahead...")
        else:
            print("Cheat mode OFF")
            real_button.config(text="Catch me!")

# -------------------------
# REAL BUTTON MOVEMENT
# -------------------------

def move_button_if_close(event):
    global cheat_mode

    if cheat_mode:
        return

    mouse_x = event.x
    mouse_y = event.y

    button_x = real_button.winfo_x()
    button_y = real_button.winfo_y()

    distance = math.sqrt((mouse_x - button_x)**2 + (mouse_y - button_y)**2)

    if distance < 100:
        new_x = random.randint(0, 350)
        new_y = random.randint(0, 250)
        real_button.place(x=new_x, y=new_y)

def win():
    real_button.config(text="GGs")

# -------------------------
# FAKE BUTTON SYSTEM
# -------------------------

def spawn_fake_buttons():
    global fake_buttons, spawning
    spawning = True

    base_x = real_button.winfo_x()
    base_y = real_button.winfo_y()

    for i in range(5):
        x = base_x + random.randint(-80, 80)
        y = base_y + random.randint(-80, 80)

        btn = tk.Button(root, text="Click me!", cursor="X_cursor")
        btn.place(x=x, y=y)

        btn.config(command=lambda b=btn: fake_click(b))

        fake_buttons.append(btn)

def fake_click(btn):
    global fake_buttons, spawning

    btn.destroy()
    fake_buttons.remove(btn)

    if len(fake_buttons) == 0:
        spawning = False
        schedule_fake_buttons()

def schedule_fake_buttons():
    delay = random.randint(60000, 180000)  # 1–3 minutes
    root.after(delay, spawn_fake_buttons)

# -------------------------
# WINDOW SETUP
# -------------------------

root = tk.Tk()
root.title("Really Cool Button")
root.geometry("400x300")

real_button = tk.Button(root, text="Click me!", command=win)
real_button.place(x=150, y=120)

# Mouse tracking
root.bind("<Motion>", move_button_if_close)

# 🔥 THIS IS THE IMPORTANT LINE (cheat key)
root.bind_all("<KeyPress>", toggle_cheat)

# Start fake button cycle
schedule_fake_buttons()

root.mainloop()