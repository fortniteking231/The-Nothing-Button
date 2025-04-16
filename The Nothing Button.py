import tkinter as Tk
import random


# Create a root window
root = Tk.Tk()
root.title("The Nothing Button")
root.resizable(False, False)
root.geometry("300x250")
index=1

def nothing():
    global index
    x = random.randint(0, root.winfo_screenwidth() - 300)
    y = random.randint(0, root.winfo_screenheight() - 250)
    root.geometry(f"300x250+{x}+{y}")
    if index >= 4:
        root.destroy()
    index += 1
    
    


# Create a button with the same size as the screen
s_width = root.winfo_screenwidth()
s_height = root.winfo_screenheight()
btn = Tk.Button(root,
                text="This will do nothing\n:)",
                command=lambda:nothing(),
                width=s_width, height=s_height,
                bg="blue", fg="white", font=("Arial", 12),
                activebackground="green",
                activeforeground="black",
                relief=Tk.RAISED,
                bd=3)
btn.pack()
root.mainloop()
