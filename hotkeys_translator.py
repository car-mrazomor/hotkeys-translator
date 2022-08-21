import os
#   python3 -m pip install requests keyboard pyperclip

import keyboard as k
import pyperclip
import sys

def copy_paste():
    k.press("command"); k.press(0)
    k.release(0); k.press(8)
    k.release(8); k.release("command")
    return pyperclip.paste()

import requests
import json

def translate(string):
    url = "https://google-translate20.p.rapidapi.com/translate"
    headers = {
        "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
        "X-RapidAPI-Host": "google-translate20.p.rapidapi.com"
    }
    params = {"text": string, "tl": "en", "sl": "auto"}
    res = requests.get(url, headers=headers, params=params)
    try:
        return json.loads(res.text)["data"]["translation"]
    except:
        print(json.loads(res.text))
        return None

def main():
    k.record(until=50)
    string = copy_paste()
    string = string[0:len(string)-1].strip()
    k.write(translate(string))


if __name__ == "__main__":
    while True:
        try:
            k.add_hotkey("command+space", main())
            k.clear_all_hotkeys()
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            print(e)
            pass