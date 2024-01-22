import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.title("Frame practice")
root.iconbitmap('icon.ico')
root.geometry('550×550')
root.resizable(0, 0) #サイズの変更禁止

# なぜframeを使うのか？
tkinter.Label(root, text='test').pack()


# ウィンドウのループ処理
root.mainloop()