import tkinter as tk
from tkinter import messagebox
from Contracts import contract_list

choose_contracts = []  # The contracts that user choose.
for contract_num in range(30):
    choose_contracts.append("")

main_window = tk.Tk()
main_window.title('my window')
main_window.geometry('200x700')

user_num_label = tk.Label(main_window, bg='gray', width=20, text='使用者編號', font=("Arial", 11, "bold"))
user_num_label.pack()

user_num = tk.Entry(width=7)  # Entry
user_num.focus()
user_num.pack()

var = tk.StringVar()
judge_label = tk.Label(main_window, textvariable=var, font=("Arial", 11, "bold"))
judge_label.pack()


def checkbutton_used_1():
    if checked_state_1.get() == 1:
        choose_contracts[0] = contract_list[0]
    if checked_state_1.get() == 0:
        choose_contracts[0] = ""


def checkbutton_used_2():
    if checked_state_2.get() == 1:
        choose_contracts[1] = contract_list[1]
    if checked_state_2.get() == 0:
        choose_contracts[1] = ""


def checkbutton_used_3():
    if checked_state_3.get() == 1:
        choose_contracts[2] = contract_list[2]
    if checked_state_3.get() == 0:
        choose_contracts[2] = ""


def checkbutton_used_4():
    if checked_state_4.get() == 1:
        choose_contracts[3] = contract_list[3]
    if checked_state_4.get() == 0:
        choose_contracts[3] = ""


def checkbutton_used_5():
    if checked_state_5.get() == 1:
        choose_contracts[4] = contract_list[4]
    if checked_state_5.get() == 0:
        choose_contracts[4] = ""


checked_state_1 = tk.IntVar()  # variable to hold on to checked state, 0 is off, 1 is on.
checkbutton_1 = tk.Checkbutton(text="基本身體清潔", variable=checked_state_1, command=checkbutton_used_1)
checked_state_1.get()
checkbutton_1.pack()

checked_state_2 = tk.IntVar()
checkbutton_2 = tk.Checkbutton(text="基本日常照顧", variable=checked_state_2, command=checkbutton_used_2)
checked_state_2.get()
checkbutton_2.pack()

checked_state_3 = tk.IntVar()
checkbutton_3 = tk.Checkbutton(text="測量生命徵象", variable=checked_state_3, command=checkbutton_used_3)
checked_state_3.get()
checkbutton_3.pack()

checked_state_4 = tk.IntVar()
checkbutton_4 = tk.Checkbutton(text="協助餵食或灌食", variable=checked_state_4, command=checkbutton_used_4)
checked_state_4.get()
checkbutton_4.pack()

checked_state_5 = tk.IntVar()
checkbutton_5 = tk.Checkbutton(text="餐食照顧", variable=checked_state_5, command=checkbutton_used_5)
checked_state_5.get()
checkbutton_5.pack()

list_to_string = ""  # 將使用者勾選的合約list轉成字串, 存到.txt中


def button_click():
    global list_to_string
    if user_num.get() == "":
        var.set("請輸入使用者編號")
        return
    num = int(user_num.get())  # 使用者編號
    list_to_string = f"使用者編號: {num}\n\n"
    if num < 0 or num > 99:
        var.set("請輸入介於0~99的數字")
    else:
        var.set("")
        for contracts in choose_contracts:
            if contracts != "":
                list_to_string += contracts
                list_to_string += " \n"

        is_ok = messagebox.askokcancel(title="Health Care 2.0", message=f"您輸入的資料如下:\n\n{list_to_string}\n\n"
                                                                        f"請確認資料是否正確?")
        if is_ok:
            f = open(f"User_{num}.txt", "x")
            f.write(list_to_string)
            f.close()
            f = open(f"User_{num}.txt", "r")  # check if work
            print(f.read())


button = tk.Button(text="送出", command=button_click)
button.pack()


main_window.mainloop()

# x = 0
#
#
# def checkbutton_used():
#     if checkbutton.checked_state.get() == 1:
#         choose_contracts[x] = contract_list[x]
#     if checkbutton.checked_state.get() == 0:
#         choose_contracts[x] = ""
#
#
# for checkbutton in contract_list:
#     checked_state = tk.IntVar()  # variable to hold on to checked state, 0 is off, 1 is on.
#     checkbutton = tk.Checkbutton(text=contract_list[x], variable=checked_state, command=checkbutton_used)
#     x += 1
#     checked_state.get()
#     checkbutton.pack()

