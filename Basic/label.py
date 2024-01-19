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



# ウィンドウのループ処理
root.mainloop()