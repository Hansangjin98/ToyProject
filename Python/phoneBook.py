from tkinter import *
from tkinter import messagebox

Names = []
Number = []
Names_new = []
Number_new = []

def isEmpty():
    n = len(Names)
    if n==0:
        return False
    else:
        return True

def isFull():
    n = len(Names)
    if n==10:
        return False
    else:
        return True

def search():
    if isEmpty()==True:
        ser = Tk()
        ser.title('찾기')
        ser.geometry('280x150')
        ser.configure(background = "#eee4da")
        ser.resizable(False, False)
        find_label = Label(ser, text="찾을 이름", background = "#eee4da")
        find_label.place(x=110, y=10)
        find_entry = Entry(ser, width=20)
        find_entry.place(x=70, y=30)
        button = Button(ser,text="찾기", font=('Helvetica', 13, "bold"), overrelief="solid", command=lambda: [find()], background = "#eee4da")
        button.place(x=110, y=90)
        
        def find():
            if Entry.get(find_entry) in Names:
                idx=Names.index((Entry.get(find_entry)))
                messagebox.showinfo(title='결과', message='이름: ' + Names[idx] + '\n전화번호: ' + Number[idx])
                ser.destroy()
            else:
                messagebox.showerror(title='오류', message='전화번호부에 없습니다.')
                ser.destroy()

    else:
        messagebox.showerror(title='오류', message='전화번호부가 비었습니다.')
    
def insert():
    if isFull()==True:
        ins = Tk()
        ins.title('전화번호부 추가')
        ins.geometry('280x150')
        ins.configure(background = "#eee4da")
        ins.resizable(False, False)
        name_label = Label(ins, text="이름 ", background = "#eee4da")
        name_label.place(x=20, y=30)
        insertName = Entry(ins, width=15)
        insertName.place(x=65, y=30)
        num_label = Label(ins, text="전화번호 ", background = "#eee4da")
        num_label.place(x=10, y=80)
        insertNum = Entry(ins, width=15)
        insertNum.place(x=65, y=80)
        button = Button(ins,text="완료", font=('Helvetica', 14, "bold"), overrelief="solid", command=lambda: [insertSave(), ins.destroy()], background = "#eee4da")
        button.place(x=200, y=50)

        def insertSave():
            if Entry.get(insertName) == '' and Entry.get(insertNum) == '':
                messagebox.showerror(title='오류', message='이름과 전화번호를 입력하세요.')
            elif Entry.get(insertName) == '':
                messagebox.showerror(title='오류', message='이름을 입력하세요.')
            elif Entry.get(insertNum) == '':
                messagebox.showerror(title='오류', message='전화번호를 입력하세요.')
            elif Entry.get(insertName) in Names:
                messagebox.showerror(title='오류', message='이미 존재하는 이름입니다.')
            elif Entry.get(insertNum) in Number:
                messagebox.showerror(title='오류', message='이미 존재하는 전화번호입니다.')
            else:
                Names.append(Entry.get(insertName))
                Number.append(Entry.get(insertNum))
                messagebox.showinfo(title='결과', message='추가되었습니다.')

    else:
        messagebox.showerror(title='오류', message='전화번호부가 꽉찼습니다.')
        
def remove():
    if isEmpty()==True:
        re = Tk()
        re.title('삭제')
        re.geometry('280x150')
        re.configure(background = "#eee4da")
        re.resizable(False, False)
        delLabel = Label(re, text="삭제할 이름", background = "#eee4da")
        delLabel.place(x=110, y=10)
        delEntry = Entry(re, width=20)
        delEntry.place(x=70, y=30)
        button = Button(re,text="삭제", font=('Helvetica', 13, "bold"), overrelief="solid", command=lambda: [delete(),re.destroy()], background = "#eee4da")
        button.place(x=120, y=90)

        def delete():
            if Entry.get(delEntry) in Names:
                idx=Names.index((Entry.get(delEntry)))
                del Names[idx]
                del Number[idx]
                messagebox.showinfo(title='결과', message='삭제되었습니다.')

            else:
                messagebox.showerror(title='오류', message='전화번호부에 없습니다.')

    else:
        messagebox.showerror(title='오류', message='전화번호부가 비었습니다.')

def printAll():
    if isEmpty()==True:
        prt = Tk()
        prt.title('목록')
        prt.geometry('400x400')
        prt.configure(background = "#eee4da")
        prt.resizable(False, False)
        titlelabel = Label(prt, text="저장된 목록", font=('Helvetica', 18, "bold"), background = "#eee4da")
        titlelabel.pack(side="top")
        titlelabel = Label(prt, text="", font=('Helvetica', 10, "bold"), background = "#eee4da")
        titlelabel.pack(side="top")
        idx = 0
        for i in range(len(Names)):
            idx+=1
            prtlabel = Label(prt, text=str(idx) + ". 이름: " + str(Names[i]) + "   /   전화번호: " + str(Number[i]),font=('Helvetica', 12, "bold"), background = "#eee4da")
            prtlabel.pack()
        button = Button(prt,text="닫기", font=('Helvetica', 14, "bold"), overrelief="solid", command=lambda: [prt.destroy()], background = "#eee4da")
        button.pack(side='bottom')
        button = Button(prt,text="정렬해서 보기", font=('Helvetica', 14, "bold"), overrelief="solid", command=lambda: [nameSort(), prt.destroy()], background = "#eee4da")
        button.pack(side='bottom')
    
    else:
        messagebox.showerror(title='오류', message='전화번호부가 비었습니다.')
    
def getData(list, i):
    if i >= 0 and i < len(list):
        return list[i]
    else:
        return None

def nameSort():
    temp = []
    for i in range(len(Names)):
        var1 = Names[i]
        var2 = Number[i]
        if var1 != None and var2 != None:
            temp.append([var1, var2])
    namesorted = sorted(temp, key=lambda nm: nm[0])
    Names_new = []
    for item in namesorted:
        Names_new.append(item[0])
    Number_new = []
    for item in namesorted:
        Number_new.append(item[1])

    ren = Tk()
    ren.title('목록')
    ren.geometry('400x400')
    ren.configure(background = "#eee4da")
    ren.resizable(False, False)
    titlelabel = Label(ren, text="저장된 목록", font=('Helvetica', 18, "bold"), background = "#eee4da")
    titlelabel.pack(side="top")
    titlelabel = Label(ren, text="", font=('Helvetica', 10, "bold"), background = "#eee4da")
    titlelabel.pack(side="top")
    idx = 0
    for i in range(len(Names)):
        label = Label(ren, text=str(idx+1) + ". 이름: " + str(Names_new[idx]) + "   /   전화번호: " + str(Number_new[idx]),font=('Helvetica', 12, "bold"), background = "#eee4da")
        label.pack()
        idx+=1
    button = Button(ren,text="닫기", font=('Helvetica', 14, "bold"), overrelief="solid", command=lambda: [ren.destroy()], background = "#eee4da")
    button.pack(side='bottom')


class mainUI():
    def __init__(self):
        mainUI = Tk()
        mainUI.title('전화번호부')
        mainUI.geometry('500x400')
        mainUI.configure(background = "#eee4da")
        mainUI.resizable(False, False)
        label = Label(mainUI, text="\n전화번호부", font=('Helvetica', 18, "bold"), background = "#eee4da")
        label.pack(side="top")
        label = Label(mainUI, text="한상진 토이프로젝트" + "\n   (2020.12)", font=('Helvetica', 9, "bold"), background = "#eee4da")
        label.place(x=185, y=365)
        button = Button(mainUI,text="검색", font=('Helvetica', 18, "bold"), overrelief="solid", command=search, background = "#eee4da")
        button.place(x=210, y=70)
        button = Button(mainUI,text="추가", font=('Helvetica', 18, "bold"), overrelief="solid", command=insert, background = "#eee4da")
        button.place(x=210, y=130)
        button = Button(mainUI,text="삭제", font=('Helvetica', 18, "bold"), overrelief="solid", command=remove, background = "#eee4da")
        button.place(x=210, y=190)
        button = Button(mainUI,text="목록", font=('Helvetica', 18, "bold"), overrelief="solid", command=printAll, background = "#eee4da")
        button.place(x=210, y=250)
        button = Button(mainUI,text="종료", font=('Helvetica', 18, "bold"), overrelief="solid", command=mainUI.quit, background = "#eee4da")
        button.place(x=210, y=310)
        mainUI.mainloop()

mainui = mainUI()