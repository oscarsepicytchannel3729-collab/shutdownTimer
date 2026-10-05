import tkinter as tk
import subprocess
from tkinter import LEFT

#Declare initial variables
root = tk.Tk()

#Window properties
root.title("Tk Example")
root.configure(background="sky blue")
root.geometry("400x200")

#Functions

def cancelCountdown():
    subprocess.run("shutdown /a")
    root.destroy()

def startCountdown(hh,mm,ss, sButton):

    try:
        hh = int(hh)
        mm = int(mm)
        ss = int(ss)
    except:
        return 422

    timeUntil = hh*3600+mm*60+ss
    subprocess.run(f"shutdown /s /t {timeUntil}")
    sButton.destroy()

    cancelButton = tk.Button(root,
                             text="Cancel shutdown",
                             font=("Trebuchet MS", 12, "bold"),
                             bg="lime green",
                             fg="white",
                             command=cancelCountdown)
    cancelButton.pack()
    print(f"Shutting down in {timeUntil}")
    return None


def main():
    tk.Label(root,
             text="Timed Shutdown",
             font=("Trebuchet MS", 16, "bold"),
             bg="sky blue",
             fg="darkblue",
             relief="raised",
             anchor="n").pack(pady=10)
    tk.Label(root,
             text="Desired Time to Shutdown",
             font=("Trebuchet MS", 12, "bold"),
             bg="sky blue",
             anchor="n").pack()

    timeFrame = tk.Frame(root, bg="sky blue")
    timeFrame.pack()


    hoursText = tk.StringVar()
    hoursText.set("hh")

    hoursInput = tk.Entry(timeFrame,
                          textvariable=hoursText,
                          width=2,
                          font=("Trebuchet MS", 10))
    hoursInput.pack(side=LEFT)

    minutesText = tk.StringVar()
    minutesText.set("mm")

    minutesInput = tk.Entry(timeFrame,
                            textvariable=minutesText,
                            width=3,
                            font=("Trebuchet MS", 10))
    minutesInput.pack(side=LEFT)

    secondsText = tk.StringVar()
    secondsText.set("ss")
    secondsInput = tk.Entry(timeFrame,
                            textvariable=secondsText,
                            width=2,
                            font=("Trebuchet MS", 10))

    secondsInput.pack(side=LEFT)

    startButton = tk.Button(root,
                            text="Start Countdown",
                            bg="crimson",
                            fg="white",
                            font=("Trebuchet MS", 12, "bold",),
                            command=lambda: startCountdown(hoursInput.get(),minutesInput.get(),secondsText.get(),startButton))
    startButton.pack(pady=10)
    #Mainloop *NECESSARY*
    root.mainloop()

if __name__ == "__main__":
    main()