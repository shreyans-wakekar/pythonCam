import tkinter
import csv
from tkinter import messagebox

window = tkinter.Tk()

# to rename the title of the window window.title("GUI")

# pack is used to show the object in the window

window.geometry('1300x750')


def edit_clicked():
    entry1.configure(state=tkinter.NORMAL)
    entry2.configure(state=tkinter.NORMAL)
    entry3.configure(state=tkinter.NORMAL)
    entry4.configure(state=tkinter.NORMAL)
    entry5.configure(state=tkinter.NORMAL)
    entry6.configure(state=tkinter.NORMAL)
    entry7.configure(state=tkinter.NORMAL)
    entry8.configure(state=tkinter.NORMAL)
    entry9.configure(state=tkinter.NORMAL)
    entry10.configure(state=tkinter.NORMAL)
    entry11.configure(state=tkinter.NORMAL)
    entry12.configure(state=tkinter.NORMAL)
    entry13.configure(state=tkinter.NORMAL)
    entry14.configure(state=tkinter.NORMAL)
    entry15.configure(state=tkinter.NORMAL)


def submit_clicked():
    with open('config.csv', mode='w') as csv_file:
        fieldnames = ['Key', 'Value']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Key': config_key_list[0], 'Value': entry1.get()})
        writer.writerow({'Key': config_key_list[1], 'Value': entry2.get()})
        writer.writerow({'Key': config_key_list[2], 'Value': entry3.get()})
        writer.writerow({'Key': config_key_list[3], 'Value': entry4.get()})
        writer.writerow({'Key': config_key_list[4], 'Value': entry5.get()})
        writer.writerow({'Key': config_key_list[5], 'Value': entry6.get()})
        writer.writerow({'Key': config_key_list[6], 'Value': entry7.get()})
        writer.writerow({'Key': config_key_list[7], 'Value': entry8.get()})
        writer.writerow({'Key': config_key_list[8], 'Value': entry9.get()})
        writer.writerow({'Key': config_key_list[9], 'Value': entry10.get()})
        writer.writerow({'Key': config_key_list[10], 'Value': entry11.get()})
        writer.writerow({'Key': config_key_list[11], 'Value': entry12.get()})
        writer.writerow({'Key': config_key_list[12], 'Value': entry13.get()})
        writer.writerow({'Key': config_key_list[13], 'Value': entry14.get()})
        writer.writerow({'Key': config_key_list[14], 'Value': entry15.get()})

    entry1.configure(state=tkinter.DISABLED)
    entry2.configure(state=tkinter.DISABLED)
    entry3.configure(state=tkinter.DISABLED)
    entry4.configure(state=tkinter.DISABLED)
    entry5.configure(state=tkinter.DISABLED)
    entry6.configure(state=tkinter.DISABLED)
    entry7.configure(state=tkinter.DISABLED)
    entry8.configure(state=tkinter.DISABLED)
    entry9.configure(state=tkinter.DISABLED)
    entry10.configure(state=tkinter.DISABLED)
    entry11.configure(state=tkinter.DISABLED)
    entry12.configure(state=tkinter.DISABLED)
    entry13.configure(state=tkinter.DISABLED)
    entry14.configure(state=tkinter.DISABLED)
    entry15.configure(state=tkinter.DISABLED)

    messagebox.showinfo('Data Saved', 'Data Saved Sucessfully.')


with open('config.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count: int = 0
    config_key_list = []
    config_value_list = []
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t Key : {row["Key"]}, Value : {row["Value"]}')
        config_key_list.append(row["Key"])
        config_value_list.append(row["Value"])
        line_count += 1

    print(f'Processed {line_count} lines.')

label1 = tkinter.Label(window, text=config_key_list[0])
label1.grid(column=0, row=2)

v1 = tkinter.StringVar(window, value=config_value_list[0])
entry1 = tkinter.Entry(window, textvariable=v1, width=70, state=tkinter.DISABLED)
entry1.grid(column=1, row=2)

label2 = tkinter.Label(window, text=config_key_list[1])
label2.grid(column=0, row=3)

v2 = tkinter.StringVar(window, value=config_value_list[1])
entry2 = tkinter.Entry(window, textvariable=v2, width=70, state=tkinter.DISABLED)
entry2.grid(column=1, row=3)

label3 = tkinter.Label(window, text=config_key_list[2])
label3.grid(column=0, row=4)

v3 = tkinter.StringVar(window, value=config_value_list[2])
entry3 = tkinter.Entry(window, textvariable=v3, width=70, state=tkinter.DISABLED)
entry3.grid(column=1, row=4)

label4 = tkinter.Label(window, text=config_key_list[3])
label4.grid(column=0, row=5)

v4 = tkinter.StringVar(window, value=config_value_list[3])
entry4 = tkinter.Entry(window, textvariable=v4, width=70, state=tkinter.DISABLED)
entry4.grid(column=1, row=5)

label5 = tkinter.Label(window, text=config_key_list[4])
label5.grid(column=0, row=6)

v5 = tkinter.StringVar(window, value=config_value_list[4])
entry5 = tkinter.Entry(window, textvariable=v5, width=70, state=tkinter.DISABLED)
entry5.grid(column=1, row=6)

label6 = tkinter.Label(window, text=config_key_list[5])
label6.grid(column=0, row=7)

v6 = tkinter.StringVar(window, value=config_value_list[5])
entry6 = tkinter.Entry(window, textvariable=v6, width=70, state=tkinter.DISABLED)
entry6.grid(column=1, row=7)

label7 = tkinter.Label(window, text=config_key_list[6])
label7.grid(column=0, row=8)

v7 = tkinter.StringVar(window, value=config_value_list[6])
entry7 = tkinter.Entry(window, textvariable=v7, width=70, state=tkinter.DISABLED)
entry7.grid(column=1, row=8)

label8 = tkinter.Label(window, text=config_key_list[7])
label8.grid(column=0, row=9)

v8 = tkinter.StringVar(window, value=config_value_list[7])
entry8 = tkinter.Entry(window, textvariable=v8, width=70, state=tkinter.DISABLED)
entry8.grid(column=1, row=9)

label9 = tkinter.Label(window, text=config_key_list[8])
label9.grid(column=0, row=10)

v9 = tkinter.StringVar(window, value=config_value_list[8])
entry9 = tkinter.Entry(window, textvariable=v9, width=70, state=tkinter.DISABLED)
entry9.grid(column=1, row=10)

label10 = tkinter.Label(window, text=config_key_list[9])
label10.grid(column=0, row=11)

v10 = tkinter.StringVar(window, value=config_value_list[9])
entry10 = tkinter.Entry(window, textvariable=v10, width=70, state=tkinter.DISABLED)
entry10.grid(column=1, row=11)

label11 = tkinter.Label(window, text=config_key_list[10])
label11.grid(column=0, row=12)

v11 = tkinter.StringVar(window, value=config_value_list[10])
entry11 = tkinter.Entry(window, textvariable=v11, width=70, state=tkinter.DISABLED)
entry11.grid(column=1, row=12)

label12 = tkinter.Label(window, text=config_key_list[11])
label12.grid(column=0, row=13)

v12 = tkinter.StringVar(window, value=config_value_list[11])
entry12 = tkinter.Entry(window, textvariable=v12, width=70, state=tkinter.DISABLED)
entry12.grid(column=1, row=13)

label13 = tkinter.Label(window, text=config_key_list[12])
label13.grid(column=0, row=14)

v13 = tkinter.StringVar(window, value=config_value_list[12])
entry13 = tkinter.Entry(window, textvariable=v13, width=70, state=tkinter.DISABLED)
entry13.grid(column=1, row=14)

label14 = tkinter.Label(window, text=config_key_list[13])
label14.grid(column=0, row=15)

v14 = tkinter.StringVar(window, value=config_value_list[13])
entry14 = tkinter.Entry(window, textvariable=v14, width=70, state=tkinter.DISABLED)
entry14.grid(column=1, row=15)

label15 = tkinter.Label(window, text=config_key_list[14])
label15.grid(column=0, row=16)

v15 = tkinter.StringVar(window, value=config_value_list[14])
entry15 = tkinter.Entry(window, textvariable=v15, width=70, state=tkinter.DISABLED)
entry15.grid(column=1, row=16)

labela = tkinter.Label(window, text="")
labela.grid(column=0, row=17)

btn_enable = tkinter.Button(window, text="EDIT", command=edit_clicked, width=18)
btn_enable.grid(column=0, row=20)

btn_submit = tkinter.Button(window, text="SUBMIT", command=submit_clicked, width=18)
btn_submit.grid(column=1, row=20)

window.mainloop()