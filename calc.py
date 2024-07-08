import customtkinter
from tkinter import END
from tkinter import messagebox

# Functionality Part

def clear():
    entryfield.delete(0, END)

def click(number):
    entryfield.insert(END, number)

def answer():
    expression = entryfield.get()
    try:
        result = eval(expression)
        ans = round(result, 3)
        entryfield.delete(0, END)
        entryfield.insert(0, ans)

    except SyntaxError:
        messagebox.showerror("Error", "Invalid Expression")
        entryfield.delete(0, END)

    except ZeroDivisionError:
        messagebox.showerror("Error", "Divivsion by zero is not possible")
        entryfield.delete(0, END)

    except NameError:
        messagebox.showerror("Error", "cannot evaluate characters.")
        entryfield.delete(0, END)

# GUI Part

root = customtkinter.CTk()
root.title("Modern Calculator")
root.geometry("300x320")
root.config(bg = "green")

entryfield = customtkinter.CTkEntry(root, font=("arial", 20, "bold"), text_color="white"
                                    , fg_color="black", border_color= "white", width = 280, height = 50)
entryfield.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 4)
b7 = customtkinter.CTkButton(root, text= "7", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", command = lambda :click("7"))
b7.grid(row=1, column=0, pady= 10)
b8 = customtkinter.CTkButton(root, text= "8", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", command = lambda :click("8"))
b8.grid(row=1, column=1)
b9 = customtkinter.CTkButton(root, text= "9", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", command = lambda :click("9"))
b9.grid(row=1, column=2)
bplus = customtkinter.CTkButton(root, text= "+", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", fg_color="orange", hover_color="red", command = lambda :click("+"))
bplus.grid(row=1, column=3)

b4 = customtkinter.CTkButton(root, text= "4", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", command = lambda :click("4"))
b4.grid(row=2, column=0, pady = 10)
b5 = customtkinter.CTkButton(root, text= "5", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", command = lambda :click("5"))
b5.grid(row=2, column=1)
b6 = customtkinter.CTkButton(root, text= "6", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", command = lambda :click("6"))
b6.grid(row=2, column=2)
bminus = customtkinter.CTkButton(root, text= "-", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", fg_color="orange", hover_color="red", command = lambda :click("-"))
bminus.grid(row=2, column=3)

b1 = customtkinter.CTkButton(root, text= "1", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", command = lambda :click("1"))
b1.grid(row=3, column=0, pady = 10)
b2 = customtkinter.CTkButton(root, text= "2", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", command = lambda :click("2"))
b2.grid(row=3, column=1)
b3 = customtkinter.CTkButton(root, text= "3", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", command = lambda :click("3"))
b3.grid(row=3, column=2)
bmultiply = customtkinter.CTkButton(root, text= "*", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", fg_color="orange", hover_color="red", command = lambda :click("*"))
bmultiply.grid(row=3, column=3)

b0 = customtkinter.CTkButton(root, text= "0", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", command = lambda :click("0"))
b0.grid(row=4, column=0, pady = 10)
bdot = customtkinter.CTkButton(root, text= ".", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", command = lambda :click("."))
bdot.grid(row=4, column=1)
bclear = customtkinter.CTkButton(root, text= "clr", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", fg_color="yellow", hover_color="yellow4", text_color="black",
                             command = clear)
bclear.grid(row=4, column=2)
bdivision = customtkinter.CTkButton(root, text= "/", font=("arial", 20, "bold"), width = 60, bg_color="green",
                             cursor = "hand2", fg_color="orange", hover_color="red", command = lambda :click("/"))
bdivision.grid(row=4, column=3)

bequal = customtkinter.CTkButton(root, text = "=", font = ("arial", 20, "bold"), width = 280, bg_color="green",
                                  cursor = "hand2", fg_color= "pink", hover_color= "pink4", text_color="black",
                                  command = answer)
bequal.grid(row=5, column=0, columnspan = 4, pady = 10)

root.mainloop()