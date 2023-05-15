from tkinter import *


# ----------------------------------------------TIMER LOGIC------------------------------------------------#
def Start():
    timerLogic(Spinmin_used(), Spinsec_used())


def timerLogic(minutes, seconds):
    label_m.config(text=minutes)
    label_s.config(text=seconds)
    if seconds > 0:
        window.after(1000, timerLogic, minutes, seconds - 1)
    elif minutes != 0 and seconds == 0:
        window.after(0, timerLogic, minutes - 1, seconds + 59)


# ---------------------------------------------UI SETUP---------------------------------------------------#
window = Tk()
window.title("TeaTimer")
window.minsize(width=500, height=400)
window.config(padx=1, pady=1)
window.wm_maxsize(width=500, height=400)

# Timer Label
label_timer = Label(text="Timer", font=("arial", 30, "bold"))
label_timer.place(x=180, y=30)

# Create label for changeable min
label_m = Label(text="0", font=("arial", 30, "bold"))
label_m.place(x=150, y=100)

# Create label for separator
label_sep = Label(text=":", font=("arial", 30, "bold"))
label_sep.place(x=215, y=100)

# Create label for changeable sec
label_s = Label(text="0", font=("arial", 30, "bold"))
label_s.place(x=250, y=100)


# Create 2 spin boxes and 2 labels
# Get methode
def Spinmin_used():
    m_min = spin_min.get()
    return int(m_min)


# Spin box min
spin_min = Spinbox(from_=0, to=59, font=("arial", 20, "bold"), width=2, command=Spinmin_used)
spin_min.place(x=150, y=200)
label_min = Label(text="Min", font=("arial", 20, "bold"))
label_min.place(x=150, y=250)


def Spinsec_used():
    m_sec = spin_sec.get()
    return int(m_sec)


# Spin box sec
spin_sec = Spinbox(from_=0, to=59, font=("arial", 20, "bold"), width=2, command=Spinsec_used)
spin_sec.place(x=250, y=200)
label_sec = Label(text="Sec", font=("arial", 20, "bold"))
label_sec.place(x=250, y=250)

# Create a start button
b_start = Button(text="START", foreground="blue", background="azure", font=("arial", 20, "bold"),
                 command=Start)
b_start.place(x=170, y=300)



window.mainloop()
