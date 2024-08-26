import tkinter as tk
from PIL import Image , ImageTk
from res.lib.hamsterclick import hamsterclick

global energy
energy = 1000
with open("yk874bt968ew7t96857i98.exe","r") as save:
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
root.title("isme")
root.minsize(300,400) 
info = tk.Tk()
info.title("isme-info")
upgrades = tk.Tk()
upgrades.title("isme-upgrades")



def loop_1sec():
    global energy
    global maxenergy
    global mony
    global profitph
    if energy < maxenergy:
        energy += 1

    mony += round(profitph/64,0)
    info.after(1000,loop_1sec)
loop_1sec()

def setinfo(mony,profitph):
    
    global energy
    global maxenergy
    global profitpc

    for widget in info.winfo_children():
        widget.destroy()
    profitpcl = tk.Label(info,text=f"isme per tap \n{profitpc}")
    profitpcl.pack()
    #profitpcl.place_configure(x=10)
    profitphl = tk.Label(info,text=f"isme per min: \n{profitph}")
    profitphl.pack()
    #profitphl.place_configure(x=160.5)
    monyl = tk.Label(info,text=f"isme: {round(mony)}$")
    monyl.pack()
    #monyl.place_configure(x=160.5,y=50)
    energyl =tk.Label(info,text=f"energy: {energy}/{maxenergy}")
    energyl.pack()
    #energyl.place_configure(x=10,y=410)
    
def buyup():
    global mony
    global profitph
    selected = str(listup.get(tk.ACTIVE)).split(",")
    if int(selected[1].replace("$","")) <= mony:
        profitph = profitph + int((selected[2].replace("isme per sec + ","")))
        mony = mony - int(selected[1].replace("$",""))


def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    info.geometry('%dx%d+%d+%d' % (width, height, x, y-200))

    upgrades.geometry('%dx%d+%d+%d' % (width, height, x+300, y))

def hamsterdrop():
    global energy
    if hamsterclick(energy):
        global mony
        global profitpc

        energy = energy - 10
        mony = mony + profitpc

def loadup():
    with open("res/list/upgrades.list","r")as upglist:
        upgrades = upglist.readlines()
        for upgrades in upgrades:
            ups = upgrades.split(",")
            listup.insert(tk.END,f"{ups[0]},{ups[1]}$,isme per sec + {ups[2]}".strip())

listup = tk.Listbox(upgrades,width=100)
listup.pack()
upbuy = tk.Button(upgrades,text="buy",command=lambda:buyup()).pack()

loadup()

def updater():
    setinfo(mony,profitph)
    info.after(10, updater)

updater()

hamsterimg = Image.open("C:\\Users\\eateb\\Desktop\\hamster\\res\\img\\hamster.png")
hamsterui = ImageTk.PhotoImage(hamsterimg.resize((300,300)))
hamster = tk.Button(root,image=hamsterui,command=lambda:hamsterdrop(), borderwidth=0, relief="sunken")
hamster.pack()
#hamster.place_configure(y=100,x=60)
def quit():
    root.destroy()
    info.destroy()
    upgrades.destroy()
tk.Button(root,text="quit",command=lambda:quit()).pack()

center_window()
tk.mainloop()

with open("yk874bt968ew7t96857i98.exe","w") as file:
    file.write(f"""maxenergy =
{maxenergy}
mony =
{int(round(mony))}
profutph = 
{profitph}
profitpc = 
{profitpc}""")