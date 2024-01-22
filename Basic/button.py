import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.title("Button practice")
root.iconbitmap('icon.ico')
root.geometry('550×550')
root.resizable(0, 0) #サイズの変更禁止
root.config(bg='red') #背景色

# ボタンの作成
button_1 = tkinter.Button(root, text='ボタン1')
button_1.grid(row=0, column=0)

button_2 = tkinter.Button(root, text='ボタン2')
button_2.grid(row=0, column=1)

button_3 = tkinter.Button(root, text='ボタン3', bg='pink', activebackground='yellow')
button_3.grid(row=0, column=2, padx=10, pady=10, ipadx=10, ipady=10)

button_4 = tkinter.Button(root, text='ボタン4', borderwidth=5)
button_4.grid(row=1, column=0, columnspan=0, sticky='WE')

button_5 = tkinter.Button(root, text='テスト')
button_6 = tkinter.Button(root, text='テスト')
button_7 = tkinter.Button(root, text='テスト')
button_8 = tkinter.Button(root, text='テスト')
button_9 = tkinter.Button(root, text='テスト')
button_10 = tkinter.Button(root, text='テスト')

button_5.grid(row=2, column=0, padx=5, pady=5)
button_6.grid(row=2, column=1, padx=5, pady=5)
button_7.grid(row=2, column=2, padx=5, pady=5)
button_8.grid(row=3, column=0, padx=5, pady=5)
button_9.grid(row=3, column=1, padx=5, pady=5)
button_10.grid(row=3, column=2, padx=5, pady=5)



# ウィンドウのループ処理
root.mainloop()