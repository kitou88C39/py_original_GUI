import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.title("Label practice!")
root.iconbitmap('icon.ico')
root.geometry('550×550')
root.resizable(0, 0) #サイズの変更禁止
root.config(bg='red') #背景色



# ウィンドウのループ処理
root.mainloop()