from tkinter import *

root = Tk()
root.geometry("400x540")
root.title("Interest calculator")
root.config(bg="#e6e6e6")

title = Label(root, text="💰 Interest Calculator", bg="#f63b3b", fg="#ffffff", font=("Arial", 24, "bold"))
p_label = Label(root, text="Principle Amount:", bg="#e6e6e6", fg="#333333", font=("Arial", 14))
p_entry = Entry(root, font=("Arial", 14), width=20, bg="#ffffff", fg="#f63b3b", relief="flat", bd=0)
r_label = Label(root, text="Rate of Interest (%):", bg="#e6e6e6", fg="#333333", font=("Arial", 14))
r_entry = Entry(root, font=("Arial", 14), width=20, bg="#ffffff", fg="#f63b3b", relief="flat", bd=0)
t_label = Label(root, text="Time (years):", bg="#e6e6e6", fg="#333333", font=("Arial", 14))
t_entry = Entry(root, font=("Arial", 14), width=20, bg="#ffffff", fg="#f63b3b", relief="flat", bd=0)
result_label = Label(root, text="", bg="#ffffff", fg="#0f5132", font=("Arial", 14, "bold"), padx=15, pady=15, relief="flat")

def cal_interest():
    try:
        principle = float(p_entry.get())
        rate = float(r_entry.get())
        time = float(t_entry.get())

        result_label.config(text=f"{principle * rate * time / 100}")

    except ValueError:
        result_label.config(text="Please enter a valid number", bg="#efe444", fg="#000000")

cal_btn = Button(root)
cal_btn.config(text="Calculate Interest", font=("Arial", 14, "bold"), bg="#f63b3b", fg="#ffffff", relief="flat", bd=0, cursor="hand2", activebackground="#eb2525", padx=25, pady=12)
cal_btn.config(command=cal_interest)

title.pack(pady=20, padx=0, fill="x")
p_label.pack(pady=(10, 5))
p_entry.pack(pady=10, padx=40)
r_label.pack(pady=(10, 5))
r_entry.pack(pady=10, padx=40)
t_label.pack(pady=(10, 5))
t_entry.pack(pady=10, padx=40)
cal_btn.pack(pady=20)
result_label.pack(pady=15, padx=40, fill="x")
root.mainloop()