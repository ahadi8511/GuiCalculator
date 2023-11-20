from tkinter import *
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x250")
        self.root.title("")
        self.font = ('Arial', 22)
        self.nums = []
        self.operate = None

        self.textbox = Text(self.root,  height=1, font=self.font)
        self.textbox.insert(END, '0')  # Starting 0
        self.textbox.pack(padx=10, pady=20)
        # self.textbox = Entry(self.root, font=self.font, justify='right', state='disabled')
        # self.textbox.pack(padx=10, pady=20, fill='x')

        # Creating buttons with grid
        self.button_frame = Frame(self.root)
        self.create_buttons_grid()

        # Creating header menu
        self.menubar = Menu(self.root, font=self.font)
        self.create_menu()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def create_menu(self):
        # File menu
        file_menu = Menu(self.menubar, tearoff=0)
        file_menu.add_command(label='Close', command=self.on_close)
        self.menubar.add_cascade(label='File', menu=file_menu)  # Add help_menu to the main menu

        # Help menu
        help_menu = Menu(self.menubar, tearoff=0)
        help_menu.add_command(label='Contact', command=self.show_contact)
        self.menubar.add_cascade(label='Help', menu=help_menu)  # Add help_menu to the main menu

        self.root.config(menu=self.menubar)  # Set the menubar as the menu for the root window

    def create_buttons_grid(self):
        # Set up the columns
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.columnconfigure(2, weight=1)
        self.button_frame.columnconfigure(3, weight=1)

        # Creating the chars
        chars = ['x', '-', '+']
        rows= 4
        columns = 4

        Button(self.button_frame, text='=', height=2).grid(row=3, column=3, sticky=W + E)

        # Creating the nums
        for i in range(rows-1):
            for n in range(columns):
                button_text = (i * 3 + n + 1) if n != 3 else chars[i]
                Button(self.button_frame, text=str(button_text), height=2, command=lambda
                    text=button_text:self.on_click(text)).grid(row=i, column=n, sticky=W + E)

        self.button_frame.pack(fill=X)

    def show_contact(self):
        messagebox.showinfo(title="Contact", message='alihesenhadi@gmail.com')

    def on_click(self, button_text):
        if isinstance(button_text, int):
            self.textbox.delete('1.0', END)
            self.textbox.insert(END, str(button_text))
            self.nums.append(button_text)

        if isinstance(button_text, str):
            self.operate = button_text

        if len(self.nums) == 2:
            res = self.calculate()
            self.textbox.delete('1.0', END)
            self.textbox.insert(END, str(res))

    def calculate(self):
        res = None
        if self.operate == '+':
            res = self.nums[0] + self.nums[1]

        elif self.operate == 'x':
            res = self.nums[0] * self.nums[1]


        elif self.operate == '-':
            res = self.nums[0] - self.nums[1]

        return res

    def on_close(self):
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?"):
            self.root.destroy()

def main():
    Calculator()

if __name__ == '__main__':
    main()
