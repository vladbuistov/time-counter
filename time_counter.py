from tkinter import *
from tkinter import ttk
import datetime as dt
from tkinter import Tk, BOTH
from datetime import datetime


def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')


def get_days():
    errmsg.set('')
    label["text"] = ""
    label1["text"] = ""
    label2["text"] = ""
    label3["text"] = ""
    label4["text"] = ""

    name1 = name.get()
    yearD = int(year.get())
    year1D = int(year1.get())
    monthD = int(month.get())
    month1D = int(month1.get())
    dayD = int(day.get())
    day1D = int(day1.get())

    try:
        dt_string = f'{dayD}/{monthD}/{yearD}'
        dt_string1 = f'{day1D}/{month1D}/{year1D}'
        datetime.strptime(dt_string, "%d/%m/%Y")
        datetime.strptime(dt_string1, "%d/%m/%Y")
        if dt.date(year1D, month1D, day1D) < dt.date(yearD, monthD, dayD):
            errmsg.set("Текущая дата не может быть меньше даты события")
        else:
            sh1 = str((dt.date(year1D, month1D, day1D) - dt.date(yearD, monthD, dayD)).days)
            sh2 = str((dt.date(year1D, month1D, day1D) - dt.date(yearD, monthD, dayD)).days * 24)
            sh3 = str((dt.date(year1D, month1D, day1D) - dt.date(yearD, monthD, dayD)).days * 24 * 60)
            sh4 = str((dt.date(year1D, month1D, day1D) - dt.date(yearD, monthD, dayD)).days * 24 * 60 * 60)
            label["text"] = f'С момента события "{name1}" прошло:'
            label1["text"] = f'В днях: {sh1}'
            label2["text"] = f'В часах: {sh2}'
            label3["text"] = f'В минутах: {sh3}'
            label4["text"] = f'В секундах: {sh4}'
    except:
        errmsg.set("Неправильный формат даты")


root = Tk()
root.title("Online-Hakaton")
root.geometry("500x450")

label_frame = LabelFrame(root, text="Введите название события: ")
label_frame.pack(anchor=NW, padx=8, pady=8, fill=X)

name = Entry(label_frame)
name.insert(0, "Запуск на орбиту первого искусственного спутника Земли")
name.configure(state='disabled')
name_focus_in = name.bind('<Button-1>', lambda x: on_focus_in(name))
name_focus_out = name.bind(
    '<FocusOut>', lambda x: on_focus_out(name, 'Запуск на орбиту первого искусственного спутника Земли'))
name.pack(anchor=NW, padx=5, pady=5, fill=X)

label_frame1 = LabelFrame(root, text="Введите дату события: ")
label_frame1.pack(anchor=NW, padx=8, pady=8, fill=X)

year = Entry(label_frame1)
year.grid(row=0, column=0, padx=5, pady=5)
year.insert(0, 1957)
year.configure(state='disabled')
year_focus_in = year.bind('<Button-1>', lambda x: on_focus_in(year))
year_focus_out = year.bind(
    '<FocusOut>', lambda x: on_focus_out(year, 1957))

month = Entry(label_frame1)
month.grid(row=0, column=1, padx=5, pady=5)
month.insert(0, 10)
month.configure(state='disabled')
month_focus_in = month.bind('<Button-1>', lambda x: on_focus_in(month))
month_focus_out = month.bind(
    '<FocusOut>', lambda x: on_focus_out(month, 10))

day = Entry(label_frame1)
day.grid(row=0, column=2, padx=5, pady=5)
day.insert(0, 4)
day.configure(state='disabled')
day_focus_in = day.bind('<Button-1>', lambda x: on_focus_in(day))
day_focus_out = day.bind(
    '<FocusOut>', lambda x: on_focus_out(day, 4))

label_frame2 = LabelFrame(root, text="Введите текущую дату: ")
label_frame2.pack(anchor=NW, padx=8, pady=8, fill=X)

today_date = dt.date.today()

year1 = Entry(label_frame2)
year1.grid(row=0, column=0, padx=5, pady=5)
year1.insert(0, today_date.year)
year1.configure(state='disabled')
year1_focus_in = year1.bind('<Button-1>', lambda x: on_focus_in(year1))
year1_focus_out = year1.bind(
    '<FocusOut>', lambda x: on_focus_out(year1, today_date.year))

month1 = Entry(label_frame2)
month1.grid(row=0, column=1, padx=5, pady=5)
month1.insert(0, today_date.month)
month1.configure(state='disabled')
month1_focus_in = month1.bind('<Button-1>', lambda x: on_focus_in(month1))
month1_focus_out = month1.bind(
    '<FocusOut>', lambda x: on_focus_out(month1, today_date.month))

day1 = Entry(label_frame2)
day1.grid(row=0, column=2, padx=5, pady=5)
day1.insert(0, today_date.day)
day1.configure(state='disabled')
day1_focus_in = day1.bind('<Button-1>', lambda x: on_focus_in(day1))
day1_focus_out = day1.bind(
    '<FocusOut>', lambda x: on_focus_out(day1, today_date.day))

errmsg = StringVar()

error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=400)
error_label.pack(padx=5, pady=5)

btn = Button(root, text="Посчитать", command=get_days)
btn.pack(padx=6, pady=6, fill=X)

label = ttk.Label(root, wraplength=400, justify=CENTER)
label1 = ttk.Label(root)
label2 = ttk.Label(root)
label3 = ttk.Label(root)
label4 = ttk.Label(root)
label.pack(padx=6, pady=6)
label1.pack(padx=6, pady=6)
label2.pack(padx=6, pady=6)
label3.pack(padx=6, pady=6)
label4.pack(padx=6, pady=6)

Grid.columnconfigure(label_frame, 0, weight=1)
Grid.columnconfigure(label_frame1, 0, weight=1)
Grid.columnconfigure(label_frame1, 1, weight=1)
Grid.columnconfigure(label_frame1, 2, weight=1)
Grid.columnconfigure(label_frame2, 0, weight=1)
Grid.columnconfigure(label_frame2, 1, weight=1)
Grid.columnconfigure(label_frame2, 2, weight=1)

root.mainloop()
