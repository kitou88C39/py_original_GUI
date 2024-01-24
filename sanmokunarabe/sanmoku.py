import tkinter
import random
import time
# masu[0][0]の値が1、masuが[1][2]の値が２
masu=[
    [0,0,0],
    [0,0,2],
    [0,0,0]
]

shirushi=0
def masume():
#    cvs.create_line(200,0,200,600,fill="gray", width=8) # 左の縦線
#    cvs.create_line(400,0,400,600,fill="gray", width=8) # 右の縦線
#    cvs.create_line(0,200,600,200,fill="gray", width=8) # 上の横線
#    cvs.create_line(0,400,600,400,fill="gray", width=8) # 下の横線

    cvs.delete("all")
# for文でマスを作成する
    for i in range(1,3):
        cvs.create_line(200*i,0,200*i,600,fill="gray",width=8)
        cvs.create_line(0,i*200,600,i*200,fill="gray",width=8)
    for y in range(3):
        for x in range(3):
            X=x*200
            Y=y*200
            if masu[y][x]==1:
                cvs.create_oval(X+20,Y+20,X+180,Y+180,outline="blue",
                width=12)
            if masu[y][x]==2:
                cvs.create_line(X+20,Y+20,X+180,Y+180,fill="red",width=12)
                cvs.create_line(X+180,Y+20,X+20,Y+180,fill="red",width=12)
    cvs.update()

def click(e):
    mx=int(e.x/200)
    my=int(e.y/200)
    if mx>2:mx=2
    if my>2:my=2
    if masu[my][mx]==0:
       masu[my][mx]=1
    else:
       masu[my][mx]=0
    masume()

root=tkinter.Tk()
root.title("三目並べ")
root.resizable(False, False) #サイズの変更禁止
root.bind("<Button>",click)
cvs=tkinter.Canvas(width=600,height=600,bg="white")
cvs.pack()
masume()
root.mainloop()