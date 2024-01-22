import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.title("Frame practice")
root.iconbitmap('icon.ico')
root.geometry('550×550')
root.resizable(0, 0) #サイズの変更禁止

# なぜframeを使うのか？
# tkinter.Label(root, text='test').pack()
# tkinter.Button(root, text='test').grid(row=0, column=0)

# frameの作成
frame_1 = tkinter.Frame(root, bg='yellow')


# ウィンドウのループ処理
root.mainloop()