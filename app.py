import tkinter as tk
from password_generator_logic import generate_password
from password_checker_logic import check_password_strength

def on_generate_click():
    new_password = generate_password(16)
    gen_entry.config(state="normal")
    gen_entry.delete(0, tk.END)  
    gen_entry.insert(0, new_password)  
    gen_entry.config(state="readonly")

def on_check_click():
    user_password = check_entry.get()
    message, color = check_password_strength(user_password)
    result_label.config(text=message, fg=color)

root = tk.Tk()
root.title("Password Toolkit")
root.geometry("640x480")

gen_title = tk.Label(root, text="Password Generator", font=("Arial", 14, "bold"))
gen_title.pack(pady=(20, 5))

gen_entry = tk.Entry(
    root, font=("Arial", 14), width=36, justify="center", state="readonly"
)
gen_entry.pack(pady=10)

btn_generate = tk.Button(
    root,
    text="Generate Password",
    command=on_generate_click,
    font=("Arial", 16, "bold"),
)
btn_generate.pack(pady=5)
divider = tk.Frame(root, height=2, bd=1, relief="sunken")
divider.pack(fill="x", padx=40, pady=25)

check_title = tk.Label(
    root, text="Password Strength Checker", font=("Arial", 14, "bold")
)
check_title.pack(pady=(0, 5))

check_entry = tk.Entry(
    root, font=("Arial", 14), width=36, justify="center", show="*"
)
check_entry.pack(pady=10)

btn_check = tk.Button(
    root,
    text="Check Strength",
    command=on_check_click,
    font=("Arial", 12, "bold"),
)
btn_check.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 13, "bold"))
result_label.pack(pady=15)

root.mainloop() 