from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from functioncalculate import toc_calculate
from excel_csv_data_importer import retrive_value_from_xlsxandcsv

rootmain = Tk()
width_Of_Window = 565
height_of_Window = 277  # 525
user_Screen_Width = rootmain.winfo_screenwidth()
user_Screen_height = rootmain.winfo_screenheight()
pop_Up_X_Co_ordinate = (user_Screen_Width / 2) - (width_Of_Window / 2)
pop_Up_Y_Co_ordinate = (user_Screen_height / 2) - (height_of_Window / 2)
rootmain.resizable(0, 0)
rootmain.configure(background='#191919')
rootmain.geometry("%dx%d+%d+%d" % (width_Of_Window, height_of_Window, pop_Up_X_Co_ordinate, pop_Up_Y_Co_ordinate))
rootmain.title("Tc Calculator")
rootmain.iconbitmap('.\images\calculator.ico')

# image import
bgimg = PhotoImage(file="./images/Background.png")
Calimage = PhotoImage(file="./images/Calculate.png")
Loadimage = PhotoImage(file="./images/load_file.png")
onimage = PhotoImage(file="./images/bon.png")
offimage = PhotoImage(file="./images/boff.png")

# background image
bglabel = Label(rootmain, image=bgimg, bd=0)
bglabel.place(x=10, y=10)

# Two variables for ptvalue & grade
PTvalue = DoubleVar()
opts = StringVar()
Tau_c = DoubleVar()


# function to open dialogbox
def File_dialog():
    global path
    path = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                      filetype=(("xlsx files", "*.xlsx"), ("csv files", "*.csv")))
    showpath()


def showpath():
    pathlabel = ttk.Label(rootmain, text=(f"File path = {path}\t\t\t\t\t\t\t\t\t\t"), background='#191919',
                          foreground='#ffffff')
    if state == 0:
        pathlabel.place_forget()
    else:
        pathlabel.place(x=55, y=15)


# ask when th window going to close
def Exit():
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=rootmain)
    if sure:
        rootmain.destroy()


rootmain.protocol("WM_DELETE_WINDOW", Exit)


# Calculation method in manual mode
def getvalmanual():
    try:
        inptvalue = PTvalue.get()
    except:
        inptvalue = 0

    ingradevalue = opts.get()
    Tau_c.set(toc_calculate(inptvalue, ingradevalue))
    showtau_c()


# Command to show the tau_c value on screen
def showtau_c():
    labelgetvalres = ttk.Label(rootmain, text=(f"{Tau_c.get()}\t\t\t\t\t\t\t\t"), font=(16))
    labelgetvalres.configure(background='#191919', foreground='#ffffff')
    labelgetvalres.place(x=95, y=233)


# Calculation method in excel mode
def getvalexcel():
    inptvalue = retrive_value_from_xlsxandcsv(path, 0, 1)
    ingradevalue = retrive_value_from_xlsxandcsv(path, 0, 2)
    PTvalue.set(inptvalue)
    opts.set(ingradevalue)
    Tau_c.set(toc_calculate(inptvalue, ingradevalue))
    showtau_c()


# State for excel button
state = 1


def onoff(event):
    global state
    if state == 1:
        exceswitch.config(image=offimage)
        PTvaluentrybox.configure(state=NORMAL)
        gradetextcombo.configure(state=NORMAL)
        PTvaluentrybox.place(x=190, y=76)
        gradetextcombo.place(x=190, y=130)
        button1.configure(command=getvalmanual)
        button2.place_forget()
        state = 0
    else:
        exceswitch.config(image=onimage)
        PTvaluentrybox.configure(state=DISABLED)
        gradetextcombo.configure(state=DISABLED)
        button1.configure(command=getvalexcel)
        button2.place(x=50, y=173, height=32, width=135)
        state = 1


# On/off button excel mode
exceswitch = ttk.Label(rootmain, image=offimage, background='#2f2f2f')
exceswitch.bind("<Button-1>", onoff)
exceswitch.place(x=390, y=120)

# ptvalue entrybox
PTvaluentrybox = Entry(rootmain, textvariable=PTvalue, font=(16), width=13)

# grade value entry box
gradetextcombo = ttk.Combobox(rootmain, textvariable=opts, font=(16), width=8)
gradetextcombo['values'] = ['', 'M15', "M20", "M25", "M30", "M35", "M40"]

# File path show text label
# pathlabel = ttk.Label(rootmain, text=path, background='#2f2f2f', foreground='#ffffff')
# Calculate button
button1 = Button(rootmain, image=Calimage)
button1.configure(bg="#191919", fg="#ffffff", activebackground='#191919', image=Calimage, bd=0, height=70, width=150)
button1.place(x=190, y=170, height=40, width=140)

# Load file button
button2 = Button(rootmain, command=File_dialog)
button2.configure(bg="#191919", fg="#ffffff", activebackground='#191919', image=Loadimage, bd=0)
# state is set to 0(off) for opening at first time
onoff(0)
rootmain.mainloop()
