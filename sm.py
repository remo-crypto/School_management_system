# from tkinter import *
# from PIL import Image, ImageTk
# mn = Tk()
# mn.geometry("856x698")
# mn.title("School Management System")
# mn.config(bg='light blue')

# def students():
#     pass

# i = Image.open("logo2.jpg")
# p = ImageTk.PhotoImage(i)
# a = Label(image=p)
# a.pack(anchor="n")

# distxt = Label(text="Welcome to School Management System", font=("Lucida Calligraphy", 22, "bold"), bg="blue", fg="white")
# distxt.pack()

# b1 = Button(text="Add new student", relief=RIDGE, font=("Lucida console", 18), fg="blue", command=students)
# b1.pack(side="top", anchor="center", padx=198, pady=20)

# b2 = Button(text="Search student", relief=RIDGE, font=("Lucida console", 18), fg="blue")
# b2.pack()

# mn.mainloop()
m = input()
if len(m)<2:
    m = f"0{m}"
print(m)