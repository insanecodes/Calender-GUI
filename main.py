from tkinter import *
import calendar

class calender_window:
    def __init__(self, root):
        self.root = root
        # Change the title
        self.root.title("Calender")
        # Change the window size
        self.root.geometry("350x250")
        # no resize for both directions
        self.root.resizable(False, False)
        # Change icon
        self.root.iconbitmap('icon.ico')

        # set gui widgets
        lbl_month= Label(self.root, text="Month",
                        font=('verdana', '10', 'bold'))
        lbl_month.place(x=40, y=20)

        self.month = Spinbox(self.root, from_=1, to=12, width="5")
        self.month.place(x=110, y=20)

        lbl_year = Label(self.root, text="Year", font=('verdana', '10', 'bold'))
        lbl_year.place(x=190, y=20)

        self.year = Spinbox(self.root, from_=1900, to=3000, width="8")
        self.year.place(x=245, y=20)

        self.calculate = Text(self.root, width=23, height=8,
                        relief=RIDGE, padx=40, borderwidth=2)
        self.calculate.place(x=40, y=55)

        btn_show = Button(self.root, text="Show", font=(
            'verdana', 10, 'bold'), command=self.show, width=6, relief=RIDGE, borderwidth=2, cursor="hand2")
        btn_show.place(x=90, y=205)

        btn_clear = Button(self.root, text="Clear", font=(
            'verdana', 10, 'bold'), command=self.clear, width=6, relief=RIDGE, borderwidth=2, cursor="hand2")
        btn_clear.place(x=190, y=205)

    def show(self):
        '''show output to the text widget'''
        self.clear()
        m = int(self.month.get())
        y = int(self.year.get())
        output = calendar.month(y, m)

        self.calculate.insert('end', output)

    def clear(self):
        '''Clear text widget'''
        self.calculate.delete(1.0, 'end')


# driver code
if __name__ == "__main__":
    root = Tk()
    obj = calender_window(root)
    root.mainloop()
