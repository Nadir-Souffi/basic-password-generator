import tkinter as tk
from password_generator_logic import generate_password
def on_click():
    new_password = generate_password(16)
    entry.config(state="normal")
    entry.delete(0, tk.END)  
    entry.insert(0, new_password)  
    entry.config(state="readonly")

root = tk.Tk()
root.title("Password Generator")
root.geometry("640x480")
entry = tk.Entry(root, font=("Arial", 14), width=36, justify="center", state="readonly")
entry.pack(pady=20)
btn = tk.Button(
    root,
    text="Generate Password",
    command=on_click,
    font=("Arial", 16, "bold"),
)
btn.pack()
root.mainloop() 