from datetime import datetime
from tkinter import messagebox


def sleep_mony(close_time: str, pph: int):
    now = datetime.now()
    closed = datetime.fromisoformat(close_time.replace("\n", ""))

    sleep_time = now - closed
    sleep_secend = int(round(sleep_time.total_seconds(), 0))
    if sleep_secend < 3600 * 3:
        mony = int(sleep_secend * (round(pph / 60, 0)))
        # if False:
        messagebox.showinfo('friend combat', f'you reched {mony}')
        return mony
    else:
        mony = int(round(pph / 60, 0)) * (3600 * 3)
        messagebox.showinfo('friend combat', f'you reched {mony}')
        return mony
