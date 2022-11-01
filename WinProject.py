import requests
import json
import os
from main import menu

url_current = "https://raw.githubusercontent.com/LexyGuru/WinProject/main/SVG_DIR/verzion.json"
file_exists = os.path.exists('ver.json')


def start():
    if not file_exists:
        url = url_current
        x = requests.get(url)
        current = x.json()

        json_object = json.dumps(current)

        with open("ver.json", "w") as outfile:
            outfile.write(json_object)

    if file_exists:
        from main import menu
        menu.menulista()


start()
menu.menulista()
