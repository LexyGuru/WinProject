import requests
import json
import os
import webbrowser

from pywinauto import Application

url_current = "https://raw.githubusercontent.com/LexyGuru/WinProject/main/SVG_DIR/verzion.json"
file_exists = os.path.exists('ver.json')
ROOT_DIR = os.path.abspath(os.curdir)

startcfg = ROOT_DIR + "\\lang\\language.json"


def configurator():

    '''webbrowser.open('https://steamcommunity.com/dev/apikey')
    webbrowser.open('https://steamcommunity.com/search/users/#text=')
    config_steam = ROOT_DIR + "\\config\\SteamDB_key.json"
    app = Application().start("notepad.exe " + config_steam)'''

    app = Application().start("notepad.exe " + startcfg)


def start():
    if not file_exists:
        configurator()
        url = url_current
        x = requests.get(url)
        current = x.json()

        json_object = json.dumps(current)

        with open("ver.json", "w") as outfile:
            outfile.write(json_object)

        print("Restart Apps")

    if file_exists:
        from main import menu
        menu.menulista()


start()

