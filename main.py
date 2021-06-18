import tkinter as tk
from tkinter import messagebox
from Contracts import contract_list

choose_contracts = []  # The contracts that user choose.
for contract_num in range(30):
    choose_contracts.append("")

main_window = tk.Tk()
main_window.title('my window')
main_window.geometry('200x650')

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


def checkbutton_used_6():
    if checked_state_6.get() == 1:
        choose_contracts[5] = contract_list[5]
    if checked_state_6.get() == 0:
        choose_contracts[5] = ""


def checkbutton_used_7():
    if checked_state_7.get() == 1:
        choose_contracts[6] = contract_list[6]
    if checked_state_7.get() == 0:
        choose_contracts[6] = ""


def checkbutton_used_8():
    if checked_state_8.get() == 1:
        choose_contracts[7] = contract_list[7]
    if checked_state_8.get() == 0:
        choose_contracts[7] = ""


def checkbutton_used_9():
    if checked_state_9.get() == 1:
        choose_contracts[8] = contract_list[8]
    if checked_state_9.get() == 0:
        choose_contracts[8] = ""


def checkbutton_used_10():
    if checked_state_10.get() == 1:
        choose_contracts[9] = contract_list[9]
    if checked_state_10.get() == 0:
        choose_contracts[9] = ""


def checkbutton_used_11():
    if checked_state_11.get() == 1:
        choose_contracts[10] = contract_list[10]
    if checked_state_11.get() == 0:
        choose_contracts[10] = ""


def checkbutton_used_12():
    if checked_state_12.get() == 1:
        choose_contracts[11] = contract_list[11]
    if checked_state_12.get() == 0:
        choose_contracts[11] = ""


def checkbutton_used_13():
    if checked_state_13.get() == 1:
        choose_contracts[12] = contract_list[12]
    if checked_state_13.get() == 0:
        choose_contracts[12] = ""


def checkbutton_used_14():
    if checked_state_14.get() == 1:
        choose_contracts[13] = contract_list[13]
    if checked_state_14.get() == 0:
        choose_contracts[13] = ""


def checkbutton_used_15():
    if checked_state_15.get() == 1:
        choose_contracts[14] = contract_list[14]
    if checked_state_15.get() == 0:
        choose_contracts[14] = ""


def checkbutton_used_16():
    if checked_state_16.get() == 1:
        choose_contracts[15] = contract_list[15]
    if checked_state_16.get() == 0:
        choose_contracts[15] = ""


def checkbutton_used_17():
    if checked_state_17.get() == 1:
        choose_contracts[16] = contract_list[16]
    if checked_state_17.get() == 0:
        choose_contracts[16] = ""


def checkbutton_used_18():
    if checked_state_18.get() == 1:
        choose_contracts[17] = contract_list[17]
    if checked_state_18.get() == 0:
        choose_contracts[17] = ""


def checkbutton_used_19():
    if checked_state_19.get() == 1:
        choose_contracts[18] = contract_list[18]
    if checked_state_19.get() == 0:
        choose_contracts[18] = ""


def checkbutton_used_20():
    if checked_state_20.get() == 1:
        choose_contracts[19] = contract_list[19]
    if checked_state_20.get() == 0:
        choose_contracts[19] = ""


def checkbutton_used_21():
    if checked_state_21.get() == 1:
        choose_contracts[20] = contract_list[20]
    if checked_state_21.get() == 0:
        choose_contracts[20] = ""


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

checked_state_6 = tk.IntVar()
checkbutton_6 = tk.Checkbutton(text="協助沐浴", variable=checked_state_6, command=checkbutton_used_6)
checked_state_6.get()
checkbutton_6.pack()

checked_state_7 = tk.IntVar()
checkbutton_7 = tk.Checkbutton(text="協助沐浴及洗頭", variable=checked_state_7, command=checkbutton_used_7)
checked_state_7.get()
checkbutton_7.pack()

checked_state_8 = tk.IntVar()
checkbutton_8 = tk.Checkbutton(text="足部照護", variable=checked_state_8, command=checkbutton_used_8)
checked_state_8.get()
checkbutton_8.pack()

checked_state_9 = tk.IntVar()
checkbutton_9 = tk.Checkbutton(text="到宅沐浴車服務", variable=checked_state_9, command=checkbutton_used_9)
checked_state_9.get()
checkbutton_9.pack()

checked_state_10 = tk.IntVar()
checkbutton_10 = tk.Checkbutton(text="翻身拍背", variable=checked_state_10, command=checkbutton_used_10)
checked_state_10.get()
checkbutton_10.pack()

checked_state_11 = tk.IntVar()
checkbutton_11 = tk.Checkbutton(text="肢體關節活動", variable=checked_state_11, command=checkbutton_used_11)
checked_state_11.get()
checkbutton_11.pack()

checked_state_12 = tk.IntVar()
checkbutton_12 = tk.Checkbutton(text="協助上下樓梯", variable=checked_state_12, command=checkbutton_used_12)
checked_state_12.get()
checkbutton_12.pack()

checked_state_13 = tk.IntVar()
checkbutton_13 = tk.Checkbutton(text="陪同外出", variable=checked_state_13, command=checkbutton_used_13)
checked_state_13.get()
checkbutton_13.pack()

checked_state_14 = tk.IntVar()
checkbutton_14 = tk.Checkbutton(text="陪同就醫", variable=checked_state_14, command=checkbutton_used_14)
checked_state_14.get()
checkbutton_14.pack()

checked_state_15 = tk.IntVar()
checkbutton_15 = tk.Checkbutton(text="家務協助", variable=checked_state_15, command=checkbutton_used_15)
checked_state_15.get()
checkbutton_15.pack()

checked_state_16 = tk.IntVar()
checkbutton_16 = tk.Checkbutton(text="代購或代領或代送服務", variable=checked_state_16, command=checkbutton_used_16)
checked_state_16.get()
checkbutton_16.pack()

checked_state_17 = tk.IntVar()
checkbutton_17 = tk.Checkbutton(text="協助執行輔助性醫療", variable=checked_state_17, command=checkbutton_used_17)
checked_state_17.get()
checkbutton_17.pack()

checked_state_18 = tk.IntVar()
checkbutton_18 = tk.Checkbutton(text="安全看視", variable=checked_state_18, command=checkbutton_used_18)
checked_state_18.get()
checkbutton_18.pack()

checked_state_19 = tk.IntVar()
checkbutton_19 = tk.Checkbutton(text="陪伴服務", variable=checked_state_19, command=checkbutton_used_19)
checked_state_19.get()
checkbutton_19.pack()

checked_state_20 = tk.IntVar()
checkbutton_20 = tk.Checkbutton(text="巡視服務", variable=checked_state_20, command=checkbutton_used_20)
checked_state_20.get()
checkbutton_20.pack()

checked_state_21 = tk.IntVar()
checkbutton_21 = tk.Checkbutton(text="居家喘息服務", variable=checked_state_21, command=checkbutton_used_21)
checked_state_21.get()
checkbutton_21.pack()

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
        print(choose_contracts)
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

# def checkbutton_used(x, checked_state):
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

# checked_state = tk.IntVar()
# checkbutton_8 = tk.Checkbutton(text="足部照護", variable=checked_state, command=checkbutton_used_8(8, checked_state))
# checked_state.get()
# checkbutton_8.pack()

