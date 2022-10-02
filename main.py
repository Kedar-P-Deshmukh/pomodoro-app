from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0
total_tik=""
tik_sym="✔"
counter=None
# ---------------------------- TIMER RESET ------------------------------- # 

def timmer_reset():
    global counter
    global rep
    global total_tik
    window.after_cancel(counter)
    mycan.itemconfig(cantext,text="00:00")
    timer_lable.config(text="Timmer",fg=GREEN)
    rep=0
    total_tik=""
    tik.config(text=f"{total_tik}")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timmer():
        global rep
        global total_tik
        global tik_sym
        rep+=1
        print(rep)
        if rep in [1,3,5]:
            count_down(WORK_MIN*60)
            timer_lable.config(text="Work!",fg=RED)
        elif rep in [2,4]:
            total_tik
            tik_sym
            total_tik+=tik_sym
            tik.config(text=f"{total_tik}")
            count_down(SHORT_BREAK_MIN *60)
            timer_lable.config(text="Break!", fg=PINK)
        elif rep in [6]:
            total_tik
            tik_sym
            total_tik += tik_sym
            tik.config(text=f"{total_tik}")
            count_down(LONG_BREAK_MIN* 60)
            timer_lable.config(text="Break!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if count>=0:
        global counter
        min=count//60
        sec=count%60
        mycan.itemconfig(cantext,text=f"{str(min).zfill(2)}:{str(sec).zfill(2)}")
        counter=window.after(1000,count_down,count-1)
    else:
        start_timmer()


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro Clock")
window.config(padx=20,pady=30,bg=YELLOW)

timer_lable=Label(text="Timmer", fg=GREEN, font=(FONT_NAME,28,"bold"),bg=YELLOW)
timer_lable.grid(column=1,row=0)

mycan=Canvas(width=220,height=224,bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
mycan.create_image(110,112,image=tomato_img)
cantext=mycan.create_text(110,135, fill="white",  text="00:00",font=(FONT_NAME,28,"bold"))
mycan.grid(column=1,row=1)

start_button=Button(text="Start",font=(FONT_NAME,12,"bold"),command=start_timmer)
start_button.grid(column=0,row=2)
reset_button=Button(text="Reset",font=(FONT_NAME,12,"bold"),command=timmer_reset)
reset_button.grid(column=2,row=2)

tik=Label(text="",fg=GREEN,font=(FONT_NAME,15,"bold"),bg=YELLOW)
tik.grid(column=1,row=3)


window.mainloop()