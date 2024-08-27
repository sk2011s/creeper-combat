import tkinter as tk
from PIL import Image, ImageTk
from res.lib.hamsterclick import hamsterclick

global energy
energy = 1000
with open("yk874bt968ew7t96857i98.exe", "r") as save:
    savel = save.readlines()
    global maxenergy
    maxenergy = int(savel[1])
    global mony
    mony = int(savel[3])
    global profitph
    profitph = int(savel[5])
    global profitpc
    profitpc = int(savel[7])

root = tk.Tk()
root.title("friend")
root.minsize(300, 400)
info = tk.Tk()
info.title("friend-info")
ppmup = tk.Tk()
ppmup.title("friend-ppmup")
ppcup = tk.Tk()
ppcup.title("friend-ppcup")
meup = tk.Tk()
meup.title("friend-ppcup")


def loop_1sec():
    global energy
    global maxenergy
    global mony
    global profitph
    if energy < maxenergy:
        energy += 1

    mony += round(profitph / 64, 0)
    info.after(1000, loop_1sec)


loop_1sec()


def setinfo(mony, profitph):

    global energy
    global maxenergy
    global profitpc

    for widget in info.winfo_children():
        widget.destroy()
    profitpcl = tk.Label(info, text=f"friend per tap \n{profitpc}")
    profitpcl.pack()
    # profitpcl.place_configure(x=10)
    profitphl = tk.Label(info, text=f"friend per min: \n{profitph}")
    profitphl.pack()
    # profitphl.place_configure(x=160.5)
    monyl = tk.Label(info, text=f"friend: {round(mony)}$")
    monyl.pack()
    # monyl.place_configure(x=160.5,y=50)
    energyl = tk.Label(info, text=f"energy: {energy}/{maxenergy}")
    energyl.pack()
    # energyl.place_configure(x=10,y=410)


def buyppmup():
    global mony
    global profitph
    selected = str(listppmup.get(tk.ACTIVE)).split(",")
    if int(selected[1].replace("$", "")) <= mony:
        profitph = profitph + int((selected[2].replace("friend per min + ", "")))
        mony = mony - int(selected[1].replace("$", ""))


def buyppcup():
    global mony
    global profitpc
    selected = str(listppcup.get(tk.ACTIVE)).split(",")
    if int(selected[1].replace("$", "")) <= mony:
        profitpc = profitpc + int((selected[2].replace("friend per click + ", "")))
        mony = mony - int(selected[1].replace("$", ""))


def buymeup():
    global mony
    global maxenergy
    selected = str(listmeup.get(tk.ACTIVE)).split(",")
    if int(selected[1].replace("$", "")) <= mony:
        maxenergy = maxenergy + int((selected[2].replace("max energy + ", "")))


def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

    info.geometry("%dx%d+%d+%d" % (width, height, x, y - 200))

    ppmup.geometry("%dx%d+%d+%d" % (width, height, x + 300, y))
    ppcup.geometry("%dx%d+%d+%d" % (width, height, x - 300, y))

    meup.geometry("%dx%d+%d+%d" % (width, height, x, y - 430))


def hamsterdrop():
    global energy
    if hamsterclick(energy):
        global mony
        global profitpc

        energy = energy - 10
        mony = mony + profitpc


def loadppcup():
    with open("res/list/ppcup.list", "r") as upglist:
        upgrades = upglist.readlines()
        for upgrades in upgrades:
            ups = upgrades.split(",")
            listppcup.insert(
                tk.END, f"{ups[0]},{ups[1]}$,friend per click + {ups[2]}".strip()
            )


def loadppmup():
    with open("res/list/ppmup.list", "r") as upglist:
        upgrades = upglist.readlines()
        for upgrades in upgrades:
            ups = upgrades.split(",")
            listppmup.insert(
                tk.END, f"{ups[0]},{ups[1]}$,friend per min + {ups[2]}".strip()
            )


def loadmeup():
    with open("res/list/meup.list", "r") as upglist:
        upgrades = upglist.readlines()
        for upgrades in upgrades:
            ups = upgrades.split(",")
            listmeup.insert(tk.END, f"{ups[0]},{ups[1]}$,max energy + {ups[2]}".strip())


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
    info.after(10, updater)


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
    info.destroy()
    ppmup.destroy()
    ppcup.destroy()
    meup.destroy()


tk.Button(root, text="quit", command=lambda: quit()).pack()

center_window()
tk.mainloop()

with open("yk874bt968ew7t96857i98.exe", "w") as file:
    file.write(
        f"""maxenergy =
{maxenergy}
mony =
{int(round(mony))}
profutph = 
{profitph}
profitpc = 
{profitpc}"""
    )
