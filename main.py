from tkinter import *
import time

import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def Reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(Timer_text,text = "00:00")
    check_mark.config(text ="")
    global reps
    reps = 0
    #timer-text =00:00
    #time text
    #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        # if its the 1st/3rd/5th/7th reps
        label.config(text="WORK TIMER")
        count_down(work_sec)
        print(work_sec)
    elif reps == 8:
        # if its the 8 th reps:
        label.config(text="LONG BREAK")
        count_down(long_break_sec)
        window.config(text = "LONG BREAK")
    elif reps == 2 or reps == 4 or reps == 6:
        # if its 2nd /4th/6th:
        count_down(short_break_sec)
        label.config(text="SHORT BREAK")
        window.config(text = "SHORT BREAK")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min<10:
        count_min = f"0{count_min}"
    canvas.itemconfig(Timer_text,text =f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="0"
        check_mark.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100,pady = 50,bg =YELLOW)


canvas = Canvas(width = 200,height= 223,bg = YELLOW,highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
label= Label(text = "Timer",fg = GREEN,bg = YELLOW,font = (FONT_NAME,50,))
label.grid(row =0 ,column = 1)
start = Button(text ="start",highlightthickness = 0,command = start_timer)
start.grid(row = 2,column = 0)
Reset = Button(text ="Reset",highlightthickness = 0,command = Reset_timer)
Reset.grid(row = 2,column = 2)
# after method


check_mark =Label(text = "")
canvas.create_image(100,111,image = tomato_img)
Timer_text = canvas.create_text(102,125,text = "00:00",fill = "white",font = (FONT_NAME, 35,"bold"))
canvas.grid(row = 1,column = 1)
check_mark = Label(text = "O",fg =GREEN,bg =YELLOW)
check_mark.grid(column =1 ,row =3 )
window.mainloop()