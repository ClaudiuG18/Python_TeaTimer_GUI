from tkinter import *
from types import NoneType

m_min = 0
s_sec = 0
running = False
# ----------------------------------------------TIMER LOGIC------------------------------------------------#
def Reset():
    global running
    running = False
    label_m.config(text="0")
    label_s.config(text="0")
    spin_min.configure(textvariable ="0")
    spin_sec.configure(textvariable ="" )

def Start():
    global running 
    running = True
    timerLogic(int(m_min), int (s_sec))
    

def timerLogic(minutes, seconds):
    global running
    label_m.config(text=minutes)
    label_s.config(text=seconds)
    if running:
        if seconds > 0:
            window.after(1000, timerLogic, minutes, seconds - 1)
        elif minutes != 0 and seconds == 0:
            window.after(0, timerLogic, minutes - 1, seconds + 59)
    else:
        window.after_cancel(timerLogic)



    


    
# ---------------------------------------------UI SETUP---------------------------------------------------#
window = Tk()
window.title("TeaTimer")
window.minsize(width=300, height=250)



# Timer Label
label_timer = Label(text="Timer", font=("arial", 20, "bold"))
label_timer.place(x=100, y=20)

# Create label for changeable min
label_m = Label(text="0", font=("arial", 30, "bold"))
label_m.place(x=100, y=70)

# Create label for separator
label_sep = Label(text=":", font=("arial", 30, "bold"))
label_sep.place(x=140, y=70)

# Create label for changeable sec
label_s = Label(text="0", font=("arial", 30, "bold"))
label_s.place(x=170, y=70)


# Create 2 spin boxes and 2 labels
# Get methode
def Spinmin_used():
   global m_min 
   m_min = spin_min.get()
   return int(m_min)


# Spin box min
spin_min = Spinbox(from_=0, to=59, font=("arial", 16), width=2,command=Spinmin_used)
spin_min.place(x=90, y=120)
label_min = Label(text="Min", font=("arial", 20))
label_min.place(x=90, y=150)


def Spinsec_used():
   global s_sec 
   s_sec = spin_sec.get()
   return int(s_sec)


# Spin box sec
spin_sec = Spinbox(from_=0, to=59, font=("arial", 16), width=2, command=Spinsec_used)
spin_sec.place(x=160, y=120)
label_sec = Label(text="Sec", font=("arial", 20))
label_sec.place(x=160, y=150)

# Create a start button
b_start = Button(text="START", foreground="blue", background="azure", font=("arial", 12, "bold"),
                 command=Start)
b_start.place(x=70, y=200)

def reset_used():
    global m_min
    global s_sec
    m_min = 0
    m_sec = 0

#Create a reset button
b_reset = Button(text="RESET", foreground="red",background="orange",font=("arial", 12, "bold"), command=Reset)
b_reset.place(x=160,y=200) 

window.mainloop()
