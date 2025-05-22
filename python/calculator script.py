import tkinter as tk

# Functions
def click(symbol):
    entry.insert(tk.END, symbol)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

# Styling
BG_COLOR = "#1e1e1e"
BTN_COLOR = "#333"
BTN_HOVER = "#555"
TEXT_COLOR = "#fff"
FONT = ("Segoe UI", 20)

# Create window
window = tk.Tk()
window.title("Nice Calculator")
window.geometry("350x500")
window.configure(bg=BG_COLOR)

# Entry
entry = tk.Entry(window, font=FONT, bg=BTN_COLOR, fg=TEXT_COLOR, borderwidth=0, justify='right')
entry.pack(padx=20, pady=20, fill='x', ipady=15)

# Button data
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Button hover effect
def on_enter(e):
    e.widget['background'] = BTN_HOVER

def on_leave(e):
    e.widget['background'] = BTN_COLOR

# Create buttons
for row in buttons:
    frame = tk.Frame(window, bg=BG_COLOR)
    frame.pack(expand=True, fill='both')
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font=FONT, bg=BTN_COLOR, fg=TEXT_COLOR, bd=0,
                        activebackground=BTN_HOVER,
                        command=(calculate if btn_text == '=' else lambda x=btn_text: click(x)))
        btn.pack(side='left', expand=True, fill='both', padx=5, pady=5)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

# Clear button
clear_btn = tk.Button(window, text="Clear", font=FONT, bg="#d32f2f", fg="white", bd=0, command=clear)
clear_btn.pack(pady=10, fill='x', padx=20, ipady=10)

window.mainloop()
