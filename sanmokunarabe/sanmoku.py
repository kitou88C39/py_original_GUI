import tkinter

def masume():
   cvs.create_line(200,0,200,600,fill="gray", width=8) # 左の縦線
   cvs.create_line(400,0,400,600,fill="gray", width=8) # 右の縦線
   cvs.create_line(0,200,600,200,fill="gray", width=8) # 上の横線
   cvs.create_line(0,400,600,400,fill="gray", width=8) # 下の横線