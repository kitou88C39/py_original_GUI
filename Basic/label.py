import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.title("Label practice!")
root.iconbitmap('icon.ico')
root.geometry('550×550')
root.resizable(0, 0) #サイズの変更禁止
root.config(bg='red') #背景色

# ラベルの作成
label_1 = tkinter.Label(root, text='宜しくお願いします')
label_1.pack()

label_2 = tkinter.Label(root, text='宜しくお願いします', font=('Arial',10,'bold'))
label_2.pack()

label_3 = tkinter.Label(root, text='宜しくお願いします', font=('Arial',10,'bold'), bg='gray')
label_3.pack(padx=10, pady=10)

label_4 = tkinter.Label(root)
label_4.config(text='宜しくお願いします')
label_4.config(bg='gray')
label_4.pack(padx=10, pady=10)

label_5 = tkinter.Label(root, text='宜しくお願いします', font=('Arial',10,'bold'), bg='gray', fg='green')
label_5.pack(padx=10, pady=(0, 10), ipadx=10, ipady=10, anchor='w')

# ウィンドウのループ処理
root.mainloop()