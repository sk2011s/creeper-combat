import json
from base64 import b64decode, b64encode
from tkinter import messagebox

def encode_data(data):
    json_data = json.dumps(data).encode("utf-8")
    encoded_data = b64encode(json_data).decode("utf-8")
    return encoded_data

def decode_data(encoded_data):
    decoded_data = b64decode(encoded_data.encode("utf-8"))
    data = json.loads(decoded_data.decode("utf-8"))
    return data

def load():
    try:
        with open("yk874bt968ew7t96857i98.exe", "r") as file:
            encoded_data = file.read()
        data = decode_data(encoded_data)
        return data
    except FileNotFoundError:
        save(1000, 0, 0, 1, "")
        return {}
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error decoding JSON.")
        return {}

def save(maxenergy: int, mony: int, pph: int, ppc: int, close_time):
    if close_time == "":
        data = {
        "maxenergy": maxenergy,
        "mony": int(round(mony)),
        "profitph": pph,
        "profitpc": ppc,
        }
    else:
        data = {
        "maxenergy": maxenergy,
        "mony": int(round(mony)),
        "profitph": pph,
        "profitpc": ppc,
        "close_time": close_time
        }
    encoded_data = encode_data(data)
    with open("yk874bt968ew7t96857i98.exe", "w") as file:
        file.write(encoded_data)


if __name__ == "__main__":
    save(1000, 0, 0, 1, "")
    print("ok")
    s = load()
    print(s)
