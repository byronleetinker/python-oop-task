from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tickets Sales")
window.geometry("600x600")
window["bg"] = "pink"
variable = StringVar(window)


class Tickets:
    result = StringVar()
    variable.set("Select your choice")

    def __init__(self, window):
        self.cellphone = Label(window, text="Enter Cellphone Number: ", bg="pink")
        self.cellphone.place(x=100, y=50)
        self.cellphone_entry = Entry(window)
        self.cellphone_entry.place(x=280, y=50)
        self.ticketcat = Label(window, text="Select a Category: ", bg="pink")
        self.ticketcat.place(x=100, y=90)
        self.optmenu = OptionMenu(window, variable, "Soccer", "Movie", "Theater")
        self.optmenu.place(x=280, y=90, width=170)
        self.ticketno = Label(window, text="Number of Tickets: ", bg="pink")
        self.ticketno.place(x=100, y=130)
        self.ticketno_entry = Entry(window)
        self.ticketno_entry.place(x=280, y=130)
        self.btncalc = Button(window, text="Calculate Price", command=self.calculate, bg="lightgreen", borderwidth=5)
        self.btncalc.place(x=240, y=170)
        self.clear = Button(window, text="Clear", command=self.delete, bg="lightgreen", borderwidth=5)
        self.clear.place(x=50, y=550)
        self.exit = Button(window, text="Exit", command=self.exit, bg="lightgreen", borderwidth=5)
        self.exit.place(x=500, y=550)
        self.lab1 = Label(window, width=50, height=15, text="", textvariable=self.result, bg="white")
        self.lab1.place(x=100, y=230)

    def calculate(self):
        try:
            if len(self.cellphone_entry.get()) != 10:
                raise ValueError
            if variable.get() == "Soccer":
                sol = 40 * int(self.ticketno_entry.get()) * 1.14
            elif variable.get() == "Movie":
                sol = 75 * int(self.ticketno_entry.get()) * 1.14
            elif variable.get() == "Theater":
                sol = 100 * int(self.ticketno_entry.get()) * 1.14
            self.result.set(sol)

        except ValueError:
            messagebox.showerror(title="Must be 10 numbers")

    def delete(self):
        self.cellphone_entry.delete(0, END)
        self.ticketno_entry.delete(0, END)
        variable.set("Select your choice")

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()


obj = Tickets(window)
window.mainloop()
