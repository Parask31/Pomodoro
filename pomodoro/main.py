from tkinter import *
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


def reset():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    label1.config(text="Timer")
    label2.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0:
        count_down(WORK_MIN*60)
        label1.config(text="Work", fg=GREEN)
        reps += 1
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        label1.config(text="Short break", fg=PINK)
        reps += 1
    elif reps == 8:
        count_down(LONG_BREAK_MIN*60)
        label1.config(text="Long break", fg=RED)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "🗸"
        label2.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label1 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label1.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_txt = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="reset", highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

label2 = Label(font=("Courier", 20, "bold"),fg=GREEN, bg=YELLOW)
label2.grid(row=3, column=1)

window.mainloop()
