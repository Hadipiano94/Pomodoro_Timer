from tkinter import *
import winsound

"""Constants"""

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "🗸"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer_on = False
reps = 0


"""Functions"""


def sec_to_clock(time_left):
    min_left = time_left // 60
    sec_left = time_left % 60
    if min_left < 10:
        min_left = f"0{min_left}"
    if sec_left < 10:
        sec_left = f"0{sec_left}"
    return f"{min_left}:{sec_left}"


def start():
    global reps
    if reps == 0:
        start_timer()


def start_timer():
    global timer_on
    global reps
    timer_on = True
    reps += 1
    if reps > 8:
        winsound.Beep(580, 500)
        timer_on = False
        return
    elif reps == 8:
        winsound.Beep(440, 200)
        winsound.Beep(440, 200)
        winsound.Beep(440, 200)
        label_1.config(text="Breeeak", fg=RED)
        timer(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        winsound.Beep(440, 200)
        winsound.Beep(440, 200)
        label_1.config(text="Break", fg=PINK)
        timer(SHORT_BREAK_MIN * 60)
    elif reps % 2 == 1:
        winsound.Beep(440, 200)
        label_1.config(text="Work", fg=GREEN)
        timer(WORK_MIN * 60)
    checkmark_label.config(text=str((reps // 2) * CHECKMARK))


def timer(time_left):
    global timer_on
    if time_left >= 0:
        if timer_on:
            clock_text = sec_to_clock(time_left)
            canvas_1.itemconfig(timer_text, text=clock_text)
            canvas_1.after(1000, timer, time_left - 1)
        else:
            return
    else:
        start_timer()


def reset_timer():
    global timer_on
    global reps
    timer_on = False
    reps = 0
    canvas_1.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    label_1.config(text="Timer", fg=GREEN)


"""UI setup"""

win = Tk()
win.title("Pomodoro")
win.config(bg=YELLOW, padx=70, pady=70)

label_1 = Label(win, text="Timer", font=(FONT_NAME, 35, "normal"), bg=YELLOW, fg=GREEN)
label_1.grid(column=1, row=0)

canvas_1 = Canvas(win, width=210, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas_1.create_image(110, 115, image=tomato_img)
timer_text = canvas_1.create_text(110, 137, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"), tags="text")
canvas_1.grid(column=1, row=1)

button_1 = Button(win, text="Start", font=(FONT_NAME, 10, "normal"), highlightthickness=0, command=start)
button_1.grid(column=0, row=2)
button_2 = Button(win, text="Reset", font=(FONT_NAME, 10, "normal"), highlightthickness=0, command=reset_timer)
button_2.grid(column=2, row=2)

checkmark_label = Label(win, text="", bg=YELLOW, fg="green", font=(FONT_NAME, 25, "bold"))
checkmark_label.grid(column=1, row=2)

win.mainloop()
