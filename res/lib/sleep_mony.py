from datetime import datetime
from tkinter import messagebox
import tkinter as tk

def sleep_mony(close_time: str, pph: int):
    root = tk.Tk()
    root.title("info")
    
    now = datetime.now()
    closed = datetime.fromisoformat(close_time.replace("\n", ""))
    sleep_time = now - closed
    sleep_secend = int(round(sleep_time.total_seconds(), 0))
    if sleep_secend < 3600 * 3:
        mony = int(sleep_secend * (round(pph / 60, 0)))
        tk.Label(root, text=f"you reached {mony}").pack()

    else:
        mony = int(round(pph / 60, 0)) * (3600 * 3)
        tk.Label(root, text=f"you reached {mony}").pack()
    claim = tk.Button(root, text="Claim", command=lambda:root.destroy()).pack()
    root.mainloop()
    if sleep_secend < 3600 * 3:
        mony = int(sleep_secend * (round(pph / 60, 0)))
        # if False:
        return mony
    else:
        mony = int(round(pph / 60, 0)) * (3600 * 3)
        return mony
    