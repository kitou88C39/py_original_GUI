import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.title('Window practice')
root.iconbitmap('icon.ico')
root.geometry('300×800')
root.resizable(0, 0) #サイズの変更禁止
root.config(bg='red') #背景色

# サブウィンドウの作成
sub_window = tkinter.Toplevel()
sub_window.title('Second Window')


# ウィンドウのループ処理
root.mainloop()