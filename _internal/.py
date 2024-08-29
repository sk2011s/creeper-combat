import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from res.lib import (
    hamsterclick,
    save,
    sleep_mony,
)

from datetime import datetime

savel = save.load()

if len(savel) >= 5:
    global mony
    close_time = savel["close_time"]
    mony = int(
        int(savel["mony"]) + sleep_mony.sleep_mony(close_time, int(savel["profitph"]))
    )
    del close_time
else:
    mony = int(savel.get("mony", 0))



global maxenergy
maxenergy = int(savel.get("maxenergy", 1000))
global energy
energy = maxenergy
global profitph
profitph = int(savel.get("profitph", 0))
global profitpc
profitpc = int(savel.get("profitpc", 1))

root = tk.Tk()
root.title("creeper combat")
root.minsize(300, 450)
ppmup = tk.Tk()
ppmup.title("creeper-ppmup")
ppcup = tk.Tk()
ppcup.title("creeper-meup")
meup = tk.Tk()
meup.title("creeper-ppcup")


def loop_1sec():
    global energy
    global maxenergy
    global mony
    global profitph
    if energy < maxenergy:
        energy += 1

    mony += round(profitph / 60, 0)
    root.after(1000, loop_1sec)


loop_1sec()


def setinfo(mony, profitph):
    global energy
    global maxenergy
    global profitpc

    if not hasattr(setinfo, "initialized"):
        setinfo.profitpcl = tk.Label(root, text="")
        setinfo.profitpcl.pack()
        setinfo.profitphl = tk.Label(root, text="")
        setinfo.profitphl.pack()
        setinfo.monyl = tk.Label(root, text="")
        setinfo.monyl.pack()
        setinfo.energyl = tk.Label(root, text="")
        setinfo.energyl.pack()
        setinfo.initialized = True

    setinfo.profitpcl.config(text=f"creeper per tap \n{profitpc}")
    setinfo.profitphl.config(text=f"creeper per min: \n{profitph}")
    setinfo.monyl.config(text=f"creeper: {round(mony)}$")
    setinfo.energyl.config(text=f"energy: {energy}/{maxenergy}")


def buy_upgrade(listbox, attribute, label):
    global mony
    selected = str(listbox.get(tk.ACTIVE)).split(",")
    cost = int(selected[1].replace("$", ""))
    if cost <= mony:
        increment = int(selected[2].replace(label, ""))
        globals()[attribute] += increment
        mony -= cost


def buyppmup():
    buy_upgrade(listppmup, "profitph", "creeper per min + ")


def buyppcup():
    buy_upgrade(listppcup, "profitpc", "creeper per click + ")


def buymeup():
    buy_upgrade(listmeup, "maxenergy", "max energy + ")


def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

    ppmup.geometry("%dx%d+%d+%d" % (width, height, x + 300, y))
    ppcup.geometry("%dx%d+%d+%d" % (width, height, x - 300, y))

    meup.geometry("%dx%d+%d+%d" % (width, height, x, y - 280))

    del x, y

def link_page():
    print(root.geometry)
    link_page()

def hamsterdrop():
    global energy
    if hamsterclick.hamstercanclick(energy):
        global mony
        global profitpc

        energy = energy - 10
        mony = mony + profitpc


def loadppcup():
    try:
        with open("res/list/ppcup.list", "r") as upglist:
            upgrades = upglist.readlines()
            for upgrades in upgrades:
                ups = upgrades.split(",")
                listppcup.insert(
                    tk.END, f"{ups[0]},{ups[1]}$,creeper per click + {ups[2]}".strip()
                )
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found: res/list/ppcup.list")
        quit()


def loadppmup():
    try:
        with open("res/list/ppmup.list", "r") as upglist:
            upgrades = upglist.readlines()
            for upgrades in upgrades:
                ups = upgrades.split(",")
                listppmup.insert(
                    tk.END, f"{ups[0]},{ups[1]}$,creeper per min + {ups[2]}".strip()
                )
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found: res/list/ppmup.list")
        quit()


def loadmeup():
    try:
        with open("res/list/meup.list", "r") as upglist:
            upgrades = upglist.readlines()
            for upgrades in upgrades:
                ups = upgrades.split(",")
                listmeup.insert(
                    tk.END, f"{ups[0]},{ups[1]}$,max energy + {ups[2]}".strip()
                )
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found: res/list/meup.list")
        quit()


listppmup = tk.Listbox(ppmup, width=100)
listppmup.pack()
ppmupbuy = tk.Button(ppmup, text="buy", command=lambda: buyppmup()).pack()

listppcup = tk.Listbox(ppcup, width=100)
listppcup.pack()
ppcupbuy = tk.Button(ppcup, text="buy", command=lambda: buyppcup()).pack()

listmeup = tk.Listbox(meup, width=100)
listmeup.pack()
meupbuy = tk.Button(meup, text="buy", command=lambda: buymeup()).pack()

loadppmup()
loadppcup()
loadmeup()


def updater():
    setinfo(mony, profitph)
    root.after(10, updater)


updater()

hamsterimg = Image.open("res\\img\\hamster.png")
hamsterui = ImageTk.PhotoImage(hamsterimg.resize((300, 300)))
hamster = tk.Button(
    root, image=hamsterui, command=lambda: hamsterdrop(), borderwidth=0, relief="sunken"
)
hamster.pack()


# hamster.place_configure(y=100,x=60)
def quit():
    root.destroy()
    ppmup.destroy()
    ppcup.destroy()
    meup.destroy()


tk.Button(root, text="quit", command=lambda: quit()).pack()

center_window()
tk.mainloop()

save.save(maxenergy, mony, profitph, profitpc, datetime.now().isoformat())
