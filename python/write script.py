import tkinter as tk
from tkinter import filedialog

def save_text():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                     filetypes=[("Text Documents", "*.txt")])
    if file:
        content = text_area.get("1.0", tk.END)
        file.write(content)
        file.close()

root = tk.Tk()
root.title("Just Write Something")
root.geometry("800x600")

text_area = tk.Text(root, wrap="word", font=("Consolas", 14))
text_area.pack(expand=True, fill="both")

save_button = tk.Button(root, text="Save", command=save_text, font=("Arial", 12))
save_button.pack(pady=10)

root.mainloop()
