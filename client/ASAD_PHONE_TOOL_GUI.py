import tkinter as tk

root = tk.Tk()
root.title("ASAD PHONE TOOL")
root.geometry("1000x650")
root.configure(bg="#E9F7FA")

title = tk.Label(
    root,
    text="ASAD PHONE TOOL",
    font=("Segoe UI", 24, "bold"),
    fg="#16445C",
    bg="#E9F7FA"
)
title.pack(pady=40)

status = tk.Label(
    root,
    text="OFFLINE MODE",
    font=("Segoe UI", 12),
    fg="#43AE73",
    bg="#E9F7FA"
)
status.pack()

root.mainloop()
