import webbrowser
import codecs
import requests
import os
import json
import pandas as pd
import lang.language
import psutil
import platform
import GPUtil
import subprocess
import speedtest
import PySimpleGUI as sg
import time
import sys
import datetime
print(datetime.datetime.now())


import threading

from colorama import Fore, Style
from pywinauto import Application
from datetime import datetime
from sty import fg
from subprocess import Popen, CREATE_NEW_CONSOLE

test = speedtest.Speedtest(secure=True)

ROOT_DIR = os.path.abspath(os.curdir)
file_exists = os.path.exists('ver.json')

start = ROOT_DIR + "\\winscript\\godm.ps1"
ms_list = ROOT_DIR + "\\winscript\\ms_list.ps1"
win_install = ROOT_DIR + "\\winscript\\win_inst_list.ps1"
win_search = ROOT_DIR + "\\winscript\\win_sear_que_inst.ps1"
win_upgrade = ROOT_DIR + "\\winscript\\win_upg_all.ps1"
power_set = ROOT_DIR + "\\winscript\\power_set.ps1"

update_powershell = ROOT_DIR + "\\winscript\\windows_runas_update.ps1"
update_powershell_fixer = ROOT_DIR + "\\winscript\\windows_runas_update_fixer.ps1"

restart_vga_driver = ROOT_DIR + "\\winscript\\windows_runas_vga_driver_restart.ps1"
restart_vga_driver_start = ROOT_DIR + "\\winscript\\windows_runas_vga_restart_start.ps1"
restart_vga_id = "pnputil /restart-device "
vga_list = '"'

steam_fix = ROOT_DIR + "\\winscript\\steam_fix_service.ps1"

C_DIR_VGA_IN = "C:\\TEMP\\"
C_DIR_IN = "C:\\TEMP\\IMPORT.json"
C_DIR_EX = "C:\\TEMP\\EXPORT.json"
steamjson = "c:\\temp\\steamdb.json"

w_scan_updates = "Update-MpSignature"
w_scan_Quick = "Start-MpScan -ScanType QuickScan"
w_scan_Full = "Start-MpScan -ScanType FullScan"

net_disabled = ROOT_DIR + "\\beta\\net_disabled.ps1"
net_enabled = ROOT_DIR + "\\beta\\net_enabled.ps1"
host_edit = ROOT_DIR + "\\beta\\hosts_edit.ps1"

url_beta = "https://raw.githubusercontent.com/LexyGuru/WinProject/beta/SVG_DIR/verzion.json"
url_current = "https://raw.githubusercontent.com/LexyGuru/WinProject/main/SVG_DIR/verzion.json"


def getListOfProcessSortedByMemory():
    listOfProcObjects = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            listOfProcObjects.append(pinfo)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    return listOfProcObjects


def adjust_size(size):
    factor = 1024
    for i in ["B", "KiB", "MiB", "GiB", "TiB"]:
        if size > factor:
            size = size / factor
        else:
            return f"{size:.3f}{i}"


def code(text, delay=.001):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# ****************************************************************************
# logo
# ****************************************************************************
class logos:
    @staticmethod
    def main_logo():
        code(fg(255, 80, 250) + "  _      ___         __                 __  _____  ____            " + fg.rs)
        code(fg(255, 80, 200) + " | | /| / (_)__  ___/ /__ _    _____   / / / / _ \/  _/ ___  __ __ " + fg.rs)
        code(fg(255, 80, 150) + " | |/ |/ / / _ \/ _  / _ \ |/|/ (_-<  / /_/ / , _// /  / _ \/ // / " + fg.rs)
        code(fg(255, 80, 100) + " |__/|__/_/_//_/\_,_/\___/__,__/___/  \____/_/|_/___/ / .__/\_, /  " + fg.rs)
        code(fg(255, 80, 50) + "                Create by LexyGuru                   /_/   /___/   " + fg.rs)
        print("")

    @staticmethod
    def beta_logo():
        print("   ___      __         ___             _         __  ")
        print("  / _ )___ / /____ _  / _ \_______    (_)__ ____/ /_ ")
        print(" / _  / -_) __/ _ `/ / ___/ __/ _ \  / / -_) __/ __/ ")
        print("/____/\__/\__/\_,_/ /_/  /_/  \___/_/ /\__/\__/\__/  ")
        print("         Create by LexyGuru      |___/               ")
        print("")

    @staticmethod
    def beta_logo_v2():
        code(fg(255, 80, 250) + "   ___      __         ___             _         __  " + fg.rs)
        code(fg(255, 80, 200) + "  / _ )___ / /____ _  / _ \_______    (_)__ ____/ /_ " + fg.rs)
        code(fg(255, 80, 150) + " / _  / -_) __/ _ `/ / ___/ __/ _ \  / / -_) __/ __/ " + fg.rs)
        code(fg(255, 80, 100) + "/____/\__/\__/\_,_/ /_/  /_/  \___/_/ /\__/\__/\__/  " + fg.rs)
        code(fg(255, 80, 950) + "         Create by LexyGuru" + fg(255, 80, 50) + "      |___/               " + fg.rs)
        print("")

    @staticmethod
    def main_logo_v2():
        code(fg(255, 80, 250) + "  _      ___         __                 __  _____  ____            " + fg.rs)
        code(fg(255, 80, 200) + " | | /| / (_)__  ___/ /__ _    _____   / / / / _ \/  _/ ___  __ __ " + fg.rs)
        code(fg(255, 80, 150) + " | |/ |/ / / _ \/ _  / _ \ |/|/ (_-<  / /_/ / , _// /  / _ \/ // / " + fg.rs)
        code(fg(255, 80, 100) + " |__/|__/_/_//_/\_,_/\___/__,__/___/  \____/_/|_/___/ / .__/\_, /  " + fg.rs)
        code(fg(20, 180, 90) + "                Create by LexyGuru" +
              fg(255, 80, 50) + "                   /_/   /___/   " + fg.rs)
        print("")

    @staticmethod
    def SteamDB_logo():
        print("   ______                 ___  ___    ___        _ ")
        print("  / __/ /____ ___ ___ _  / _ \/ _ )  / _ | ___  (_)")
        print(" _\ \/ __/ -_) _ `/  ' \/ // / _  | / __ |/ _ \/ / ")
        print("/___/\__/\__/\_,_/_/_/_/____/____/ /_/ |_/ .__/_/  ")
        print("            Create by LexyGuru          /_/        ")
        print("")

    @staticmethod
    def SteramDB_logo_v2():
        code(fg(255, 80, 250) + "   ______                 ___  ___    ___        _ " + fg.rs)
        code(fg(255, 80, 200) + "  / __/ /____ ___ ___ _  / _ \/ _ )  / _ | ___  (_)" + fg.rs)
        code(fg(255, 80, 150) + " _\ \/ __/ -_) _ `/  ' \/ // / _  | / __ |/ _ \/ / " + fg.rs)
        code(fg(255, 80, 100) + "/___/\__/\__/\_,_/_/_/_/____/____/ /_/ |_/ .__/_/  " + fg.rs)
        code(fg(20, 180, 90) + "            Create by LexyGuru" + fg(255, 80, 50) + "          /_/        " + fg.rs)
        print("")

    @staticmethod
    def BattleNet():
        code(fg(255, 80, 250) + "________       ________________ " +
              fg(20, 180, 90) + "Create by LexyGuru" +
              fg(255, 80, 250) + "_____ " + fg.rs)
        code(fg(255, 80, 200) + "___  __ )_____ __  /__  /___  /____   ______________  /_" + fg.rs)
        code(fg(255, 80, 150) + "__  __  |  __ `/  __/  __/_  /_  _ \  __  __ \  _ \  __/" + fg.rs)
        code(fg(255, 80, 100) + "_  /_/ // /_/ // /_ / /_ _  / /  __/___  / / /  __/ /_  " + fg.rs)
        code(fg(255, 80, 50) + "/_____/ \__,_/ \__/ \__/ /_/  \___/_(_)_/ /_/\___/\__/  " + fg.rs)
        print("")


# ****************************************************************************
# ver_ch
# ****************************************************************************
class verch:

    @staticmethod
    def ver_ch():
        url = url_current
        x = requests.get(url)
        new_ver = x.json()['next_current'][0]

        with open(ROOT_DIR + '\\ver.json', "r") as file:
            jsonData = json.load(file)
            current = jsonData['current'][0]

            a = current
            b = new_ver

            if b > a:
                print(fg(255, 64, 64) + lang.language.langs["verch_lang"][1] + b + fg.rs)

            elif a == b:
                print(fg(127, 255, 0) + lang.language.langs["verch_lang"][0] + a + fg.rs)

    @staticmethod
    def ver_ch_beta():

        url = url_beta
        x = requests.get(url)
        beta_ver = x.json()['next_beta'][0]

        x = requests.get(url)
        current = x.json()['current_beta'][0]

        a = current
        b = beta_ver

        if b > a:
            print(fg(255, 64, 64) + lang.language.langs["verch_lang"][1] + b + " " +
                  lang.language.langs["verch_lang"][2] + fg.rs)

        elif a == b:
            print(fg(127, 255, 0) + lang.language.langs["verch_lang"][3] + a + fg.rs)

    @staticmethod
    def ver_ch_start():

        if not file_exists:
            url = url_current
            x = requests.get(url)
            current = x.json()

            json_object = json.dumps(current)

            with open("ver.json", "w") as outfile:
                outfile.write(json_object)

        if file_exists:
            def Sysinfomenu():
                uname = platform.uname()
                print(
                    fg(130, 255, 0) + "S" +
                    fg(150, 245, 10) + "y" +
                    fg(170, 235, 20) + "s" +
                    fg(190, 225, 30) + "t" +
                    fg(210, 215, 40) + "e" +
                    fg(230, 205, 50) + "m" +
                    fg(250, 195, 60) + ": " + fg.rs +

                    fg(250, 195, 255) + f"{uname.system} {uname.version}" + fg.rs)

            Sysinfomenu()
            verch.ver_ch()
            verch.ver_ch_beta()
            print('\n')


# ****************************************************************************
# language_def_list
# ****************************************************************************
class menu_list_def:

    class menu_def:
        @staticmethod
        def clear():
            os.system("cls")

        @staticmethod
        def next_text():
            print("")
            print(lang.language.langs['main'][2])
            print("")

        @staticmethod
        def back_to_menu_text():
            print("")
            print(lang.language.langs['main'][3])
            print("")

        @staticmethod
        def back_text():
            print("")
            print(lang.language.langs['main'][1])
            print("")

        @staticmethod
        def extra_back_text():
            print("")
            print(lang.language.langs['main'][8])
            print("")

        @staticmethod
        def exits_text():
            print("")
            print(lang.language.langs['main'][5])
            print("")

        @staticmethod
        def menu_A():
            lista = lang.language.langs['menu_a']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_listaA():
            lista = lang.language.langs['menu_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_B():
            lista = lang.language.langs['menu_b']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_C():
            lista = lang.language.langs['menu_c']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class system_lista:
        @staticmethod
        def system_listaA():
            lista = lang.language.langs['menu_system']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_system_display_list():
            lista = lang.language.langs['menu_system_display_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_system_audio_list():
            lista = lang.language.langs['menu_system_audio_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_system_focus_list():
            lista = lang.language.langs['menu_system_focus_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_system_battery_list():
            lista = lang.language.langs['menu_system_battery_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_system_storage_list():
            lista = lang.language.langs['menu_system_storage_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class devices_list:

        @staticmethod
        def devices_listA():
            lista = lang.language.langs['devices_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_devices_typing_list():
            lista = lang.language.langs['devices_menu_typing_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class phone_list:

        @staticmethod
        def phone_listA():
            lista = lang.language.langs['phone_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class network_list:

        @staticmethod
        def network_listA():
            lista = lang.language.langs['network_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_network_status_list():
            lista = lang.language.langs['network_menu_status_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_network_wifi_list():
            lista = lang.language.langs['network_menu_wifi_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class personalization_list:

        @staticmethod
        def personalization_listA():
            lista = lang.language.langs['personalization_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_start_personalization_list():
            lista = lang.language.langs['personalization_menu_start_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class apps_list:

        @staticmethod
        def apps_listA():
            lista = lang.language.langs['apps_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_apps_list():
            lista = lang.language.langs['apps_menu_apps_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_apps_ofline_maps_list():
            lista = lang.language.langs['offline_maps_menu_apps_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class accounts_list:

        @staticmethod
        def accounts_listA():
            lista = lang.language.langs['accounts_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_accounts_sigin_list():
            lista = lang.language.langs['accounts_menu_sigin_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_accounts_family_list():
            lista = lang.language.langs['accounts_menu_family_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class time_language_list:

        @staticmethod
        def time_language_listA():
            lista = lang.language.langs['time_language_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_time_language_language_list():
            lista = lang.language.langs['time_language_menu_language_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class gaming_list:

        @staticmethod
        def gaming_listA():
            lista = lang.language.langs['gaming_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class extra_list:

        @staticmethod
        def extra_listA():
            lista = lang.language.langs['extras_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def menu_weather_list():
            lista = lang.language.langs['extras_menu_weather_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class ease_of_access:

        @staticmethod
        def eace_of_access_listA():
            lista = lang.language.langs['ease_of_access_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def ease_of_access_narrator_list():
            lista = lang.language.langs['ease_of_access_menu_narrator_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class search:

        @staticmethod
        def search_listA():
            lista = lang.language.langs['search_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class privacy:

        @staticmethod
        def privacy_listA():
            lista = lang.language.langs['privacy_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def privacy_diagnostics_list():
            lista = lang.language.langs['privacy_menu_diagnostics_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class update:

        @staticmethod
        def update_listA():
            lista = lang.language.langs['update_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def windows_menu_update_list():
            lista = lang.language.langs['windows_menu_update_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def windows_menu_security_list():
            lista = lang.language.langs['windows_menu_security_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class mixed_reality:

        @staticmethod
        def mixed_reality_listA():
            lista = lang.language.langs['mixed_reality_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class surface_hub:

        @staticmethod
        def surface_hub_listA():
            lista = lang.language.langs['surface_hub_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class shell:

        @staticmethod
        def shell_commands_list_0():
            lista = lang.language.langs['shell_commads']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def shell_commands_list_1():
            lista = lang.language.langs['shell_commads_1']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def shell_commands_list_2():
            lista = lang.language.langs['shell_commads_2']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def shell_commands_list_3():
            lista = lang.language.langs['shell_commads_3']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def shell_commands_list_4():
            lista = lang.language.langs['shell_commads_4']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def shell_commands_list_5():
            lista = lang.language.langs['shell_commads_5']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def shell_commands_list_6():
            lista = lang.language.langs['shell_commads_6']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def shell_commands_list_7():
            lista = lang.language.langs['shell_commads_7']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def shell_commands_list_8():
            lista = lang.language.langs['shell_commads_8']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def shell_commands_list_9():
            lista = lang.language.langs['shell_commads_9']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def shell_commands_list_10():
            lista = lang.language.langs['shell_commads_10']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class goodm:

        @staticmethod
        def goodmod_listA():
            lista = lang.language.langs['goodmod']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def power_listA():
            lista = lang.language.langs['power_goodmod']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def power_menu_listA():
            lista = lang.language.langs['manual_power']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def Update_Fixer():
            lista = lang.language.langs['Update_Fixer']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def Windows_Defender():
            lista = lang.language.langs['Windows_Defender']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class microsoft:

        @staticmethod
        def microsoft_listA():
            lista = lang.language.langs['Microsoft_Store']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def microsoft_install():
            lista = lang.language.langs['Microsoft_Store_install_fixer']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def microsoft_uninstall():
            lista = lang.language.langs['Microsoft_Store_uninstall_fixer']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class beta:

        @staticmethod
        def beta_project_lang():
            lista = lang.language.langs['beta_project']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class SteamDB_lang:
        @staticmethod
        def SteamDB_Summaries():
            lista = lang.language.langdb['SteamDB_Summaries']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def GetGameServersStatus():
            lista = lang.language.langdb['GetGameServersStatus']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def GetGameServersStatus_list():
            lista = lang.language.langdb['GetGameServersStatus_list']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def steam_menu():
            lista = lang.language.langdb['steam_menu']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def steamdb_selected_lang():
            lista = lang.language.langdb['language_selected']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class verch:

        @staticmethod
        def verch_lang():
            lista = lang.language.langdb['verch_lang']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

    class systeminfo:
        @staticmethod
        def systeminfo():
            lista = lang.language.langs['systeminfo']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])

        @staticmethod
        def sysinfo():
            lista = lang.language.langs['sysinfo']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])


# ****************************************************************************
# modul
# ****************************************************************************
class modul:
    class SteamDB:
        class game:
            @staticmethod
            def CSGOServer_730():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.SteramDB_logo_v2()
                    verch.ver_ch_start()
                    menu_list_def.SteamDB_lang.GetGameServersStatus()
                    menu_list_def.menu_def.back_text()
                    keyload = int(input("" + lang.language.langs["main"][6]))

                    if keyload == 0:
                        webbrowser.open('https://steamcommunity.com/dev/apikey')
                        webbrowser.open('https://steamcommunity.com/search/users/#text=')
                        config_steam = ROOT_DIR + "\\config\\SteamDB_key.json"
                        app = Application().start("notepad.exe " + config_steam)

                    if keyload == 1:
                        while True:
                            menu_list_def.menu_def.clear()
                            logos.SteramDB_logo_v2()
                            verch.ver_ch_start()
                            menu_list_def.SteamDB_lang.GetGameServersStatus_list()
                            menu_list_def.menu_def.back_text()

                            with open(ROOT_DIR + '\\config\\SteamDB_key.json', "r") as file:
                                jsonData = json.load(file)

                            keyin = jsonData['steam_key'][0]

                            keyloadd = int(input("" + lang.language.langs["main"][6]))
                            if keyloadd == 0:
                                url = (
                                        "https://api.steampowered.com/ICSGOServers_730/"
                                        "GetGameServersStatus/v1/?key=" + keyin)
                                x = requests.get(url)
                                h = x.json()['result']['services']

                                print(fg(255, 80, 250) + "SessionsLogon: " + fg(255, 180, 70) + h.get(
                                    'SessionsLogon') + fg.rs)
                                print(fg(255, 80, 240) + "SteamCommunity: " + fg(255, 180, 60) + h.get(
                                    'SteamCommunity') + fg.rs)
                                print(
                                    fg(255, 80, 230) + "IEconItems: " + fg(255, 180, 50) + h.get('IEconItems') + fg.rs)
                                print(fg(255, 80, 220) + "Leaderboards: " + fg(255, 180, 40) + h.get(
                                    'Leaderboards') + fg.rs)

                                menu_list_def.menu_def.back_text()
                                keyloadd = int(input("" + lang.language.langs["main"][6]))

                                if keyloadd == 20:
                                    break
                            if keyloadd == 1:
                                while True:
                                    menu_list_def.menu_def.clear()
                                    logos.SteramDB_logo_v2()
                                    verch.ver_ch_start()

                                    url = ("https://api.steampowered.com/ICSGOServers_730/"
                                           "GetGameServersStatus/v1/?key=" + keyin)
                                    x = requests.get(url)
                                    h = x.json()['result']['datacenters']

                                    dict_list_Peru = (h['Peru'])
                                    dict_list_EU_West = (h['EU West'])
                                    dict_list_EU_East = (h['EU East'])
                                    dict_list_Poland = (h['Poland'])
                                    dict_list_India_East = (h['India East'])
                                    dict_list_Hong_Kong = (h['Hong Kong'])
                                    dict_list_Spain = (h['Spain'])
                                    dict_list_Chile = (h['Chile'])
                                    dict_list_US_Southwest = (h['US Southwest'])
                                    dict_list_US_Southeast = (h['US Southeast'])
                                    dict_list_India = (h['India'])
                                    dict_list_EU_North = (h['EU North'])
                                    dict_list_Emirates = (h['Emirates'])
                                    dict_list_US_Northwest = (h['US Northwest'])
                                    dict_list_South_Africa = (h['South Africa'])
                                    dict_list_Brazil = (h['Brazil'])
                                    dict_list_US_Northeast = (h['US Northeast'])
                                    dict_list_US_Northcentral = (h['US Northcentral'])
                                    dict_list_Japan = (h['Japan'])
                                    dict_list_Argentina = (h['Argentina'])
                                    dict_list_South_Korea = (h['South Korea'])
                                    dict_list_Singapore = (h['Singapore'])
                                    dict_list_Australia = (h['Australia'])
                                    dict_list_China_Shanghai = (h['China Shanghai'])
                                    dict_list_China_Tianjin = (h['China Tianjin'])
                                    dict_list_China_Guangzhou = (h['China Guangzhou'])

                                    print(fg(255, 80, 250) +

                                          "Peru: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_Peru.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_Peru.get('load') + fg.rs)

                                    print(fg(255, 80, 245) +

                                          "EU West: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_EU_West.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_EU_West.get('load') + fg.rs)

                                    print(fg(255, 80, 240) +

                                          "EU East: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_EU_East.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_EU_East.get('load') + fg.rs)

                                    print(fg(255, 80, 235) +

                                          "Poland: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_Poland.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_Poland.get('load') + fg.rs)

                                    print(fg(255, 80, 230) +

                                          "India East: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_India_East.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_India_East.get('load') + fg.rs)

                                    print(fg(255, 80, 225) +

                                          "Hong Kong: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_Hong_Kong.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_Hong_Kong.get('load') + fg.rs)

                                    print(fg(255, 80, 220) +

                                          "Spain: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_Spain.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_Spain.get('load') + fg.rs)

                                    print(fg(255, 80, 215) +

                                          "Chile: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_Chile.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_Chile.get('load') + fg.rs)

                                    print(fg(255, 80, 210) +

                                          "US Southwest: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_US_Southwest.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_US_Southwest.get('load') + fg.rs)

                                    print(fg(255, 80, 205) +

                                          "US Southeast: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_US_Southeast.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_US_Southeast.get('load') + fg.rs)

                                    print(fg(255, 80, 200) +

                                          "India: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_India.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_India.get('load') + fg.rs)

                                    print(fg(255, 80, 195) +

                                          "EU North: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_EU_North.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_EU_North.get('load') + fg.rs)

                                    print(fg(255, 80, 190) +

                                          "Emirates: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_Emirates.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_Emirates.get('load') + fg.rs)

                                    print(fg(255, 80, 185) +

                                          "US Northwest: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_US_Northwest.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_US_Northwest.get('load') + fg.rs)

                                    print(fg(255, 80, 180) +

                                          "South Africa: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_South_Africa.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_South_Africa.get('load') + fg.rs)

                                    print(fg(255, 80, 175) +

                                          "Brazil: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_Brazil.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_Brazil.get('load') + fg.rs)

                                    print(fg(255, 80, 170) +

                                          "US Northeast: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_US_Northeast.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_US_Northeast.get('load') + fg.rs)

                                    print(fg(255, 80, 165) +

                                          "US Northcentral: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_US_Northcentral.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_US_Northcentral.get('load') + fg.rs)

                                    print(fg(255, 80, 160) +

                                          "Japan: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_Japan.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_Japan.get('load') + fg.rs)

                                    print(fg(255, 80, 155) +

                                          "Argentina: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_Argentina.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_Argentina.get('load') + fg.rs)

                                    print(fg(255, 80, 150) +

                                          "South Korea: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_South_Korea.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_South_Korea.get('load') + fg.rs)

                                    print(fg(255, 80, 145) +

                                          "Singapore: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_Singapore.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_Singapore.get('load') + fg.rs)

                                    print(fg(255, 80, 140) +

                                          "Australia: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_Australia.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_Australia.get('load') + fg.rs)

                                    print(fg(255, 80, 135) +

                                          "China Shanghai: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_China_Shanghai.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_China_Shanghai.get('load') + fg.rs)

                                    print(fg(255, 80, 130) +

                                          "China Tianjin: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_China_Tianjin.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_China_Tianjin.get('load') + fg.rs)

                                    print(fg(255, 80, 125) +

                                          "China Guangzhou: " + fg(255, 180, 70) +
                                          "capacity: " + fg(255, 180, 70) + dict_list_China_Guangzhou.get('capacity') +
                                          " Load: " + fg(255, 180, 70) + dict_list_China_Guangzhou.get('load') + fg.rs)

                                    menu_list_def.menu_def.back_text()
                                    keyloadd = int(input("" + lang.language.langs["main"][6]))

                                    if keyloadd == 20:
                                        break

                            if keyloadd == 2:
                                while True:
                                    menu_list_def.menu_def.clear()
                                    logos.SteramDB_logo_v2()
                                    verch.ver_ch_start()
                                    url = ("https://api.steampowered.com/ICSGOServers_730/"
                                           "GetGameServersStatus/v1/?key=" + keyin)
                                    x = requests.get(url)
                                    h = x.json()['result']
                                    dict_list_matchmaking = (h['matchmaking'])
                                    print(fg(255, 80, 250) +
                                          "Matchmaking: " + fg(255, 180, 70) + '\n'
                                          "      scheduler: " + fg(255, 180, 70) +
                                          dict_list_matchmaking.get('scheduler') + '\n'
                                          "      online_servers: " + fg(255, 180, 70) +
                                          str(dict_list_matchmaking.get('online_servers')) + '\n'
                                          "      online_players: " + fg(255, 180, 70) +
                                          str(dict_list_matchmaking.get('online_players')) + '\n'
                                          "      searching_players: " + fg(255, 180, 70) +
                                          str(dict_list_matchmaking.get('searching_players')) + '\n'
                                          "      search_seconds_avg: " + fg(255, 180, 70) +
                                          str(dict_list_matchmaking.get('search_seconds_avg')) + fg.rs)

                                    menu_list_def.menu_def.back_text()
                                    keyloadd = int(input("" + lang.language.langs["main"][6]))

                                    if keyloadd == 20:
                                        break

                            if keyloadd == 3:
                                while True:
                                    menu_list_def.menu_def.clear()
                                    logos.SteramDB_logo_v2()
                                    verch.ver_ch_start()
                                    url = ("https://api.steampowered.com/ICSGOServers_730/"
                                           "GetGameServersStatus/v1/?key=" + keyin)
                                    x = requests.get(url)
                                    h = x.json()['result']['perfectworld']
                                    dict_list_perfectworld = (h['logon'])
                                    dict_list_purchase = (h['purchase'])

                                    print(fg(255, 80, 250) +
                                          "Perfectworld: " + fg(255, 10, 70) + '\n'
                                          "   Logon: " + fg(255, 180, 70) + '\n'
                                          "      availability: " + fg(255, 180, 70) +
                                          dict_list_perfectworld.get('availability') + '\n'
                                          "      latency: " + fg(255, 180, 70) +
                                          dict_list_perfectworld.get('latency') + fg.rs)

                                    print(fg(255, 10, 70) +
                                          "   Purchase: " + fg(255, 180, 70) + '\n'
                                                                               "      availability: " + fg(255, 180,
                                                                                                           70) +
                                          dict_list_purchase.get('availability') + '\n'
                                                                                   "      purchase: " + fg(255, 180,
                                                                                                           70) +
                                          dict_list_purchase.get('latency') + fg.rs)

                                    menu_list_def.menu_def.back_text()
                                    keyloadd = int(input("" + lang.language.langs["main"][6]))

                                    if keyloadd == 20:
                                        break

                            if keyloadd == 20:
                                break

                    if keyload == 20:
                        break

        class userinfo:
            @staticmethod
            def my_userid_info():
                while True:
                    logos.SteramDB_logo_v2()
                    verch.ver_ch_start()

                    with open(ROOT_DIR + '\\config\\SteamDB_key.json', "r") as file:
                        jsonData = json.load(file)
                        keyin = jsonData['steam_key'][0]
                        steamid = jsonData['steamid'][0]

                        url = ("https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key="
                               + keyin + "&steamid=" + steamid)
                        x = requests.get(url)
                        h = x.json()['response']['game_count']
                        print("All Games in steam: " + str(h) + "\n")

                        hh = x.json()['response']['games']
                        for item in hh:
                            # write each item on a new line
                            print("%s" % item)

                        system_lista = int(input("[20]: Back: "))

                    if system_lista == 20:
                        break

            @staticmethod
            def userid_info():
                while True:
                    logos.SteramDB_logo_v2()
                    verch.ver_ch_start()

                    with open(ROOT_DIR + '\\config\\SteamDB_key.json', "r") as file:
                        jsonData = json.load(file)
                        keyin = jsonData['steam_key'][0]
                        webbrowser.open('https://steamcommunity.com/search/users/#text=')
                        steamid = input("steamID64 (Dec): ")
                        url = (
                                "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key=" +
                                keyin + "&steamid=" + steamid)
                        x = requests.get(url)
                        h = x.json()['response']['game_count']
                        print("All Games in steam: " + str(h) + "\n")

                        hh = x.json()['response']['games']
                        for item in hh:
                            # write each item on a new line
                            print("%s" % item)

                        system_lista = int(input("[20]: Back: "))

                    if system_lista == 20:
                        break

        class playerbans:
            @staticmethod
            def bann_user():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.SteramDB_logo_v2()
                    verch.ver_ch_start()

                    with open(ROOT_DIR + '\\config\\SteamDB_key.json', "r") as file:
                        jsonData = json.load(file)
                        keyin = jsonData['steam_key'][0]
                        steamid = jsonData['steamid'][0]
                        url = (
                                "https://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=" + keyin +
                                "&steamids=" + steamid)
                        x = requests.get(url)
                        h = x.json()['players'][0]
                        print(fg(255, 80, 250) +
                              "Players: " + fg(255, 10, 70) + '\n'
                                                              "   SteamId: " + fg(255, 180, 70) + str(
                            h.get('SteamId')) + '\n' + fg(255, 10, 70) +
                              "   CommunityBanned: " + fg(255, 180, 70) +
                              str(h.get('CommunityBanned')) + '\n' + fg(255, 10, 70) +
                              "   VACBanned: " + fg(255, 180, 70) +
                              str(h.get('VACBanned')) + '\n' + fg(255, 10, 70) +
                              "   NumberOfVACBans: " + fg(255, 180, 70) +
                              str(h.get('NumberOfVACBans')) + '\n' + fg(255, 10, 70) +
                              "   DaysSinceLastBan: " + fg(255, 180, 70) +
                              str(h.get('DaysSinceLastBan')) + '\n' + fg(255, 10, 70) +
                              "   NumberOfGameBans: " + fg(255, 180, 70) +
                              str(h.get('NumberOfGameBans')) + '\n' + fg(255, 10, 70) +
                              "   EconomyBan: " + fg(255, 180, 70) +
                              str(h.get('EconomyBan')) + '\n' + fg.rs)

                        system_lista = int(input("[20]: Back: "))

                    if system_lista == 20:
                        break

        class playersummaries:
            @staticmethod
            def GetPlayerSummaries():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.SteramDB_logo_v2()
                    verch.ver_ch_start()

                    with open(ROOT_DIR + '\\config\\SteamDB_key.json', "r") as file:
                        jsonData = json.load(file)
                        keyin = jsonData['steam_key'][0]
                        steamid = jsonData['steamid'][0]
                        url = (
                                "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=" + keyin +
                                "&steamids=" + steamid)
                        x = requests.get(url)
                        h = x.json()['response']['players'][0]

                        print(fg(255, 80, 250) + "steamid: " + fg(255, 180, 70) + h.get('steamid') + fg.rs)
                        print(fg(255, 80, 240) + "personaname: " + fg(255, 180, 60) + h.get('personaname') + fg.rs)
                        print(fg(255, 80, 230) + "realname: " + fg(255, 180, 50) + str(h.get('realname')) + fg.rs)
                        print(fg(255, 80, 220) + "profileurl: " + fg(255, 180, 40) + h.get('profileurl') + fg.rs)
                        print(fg(255, 80, 210) + "avatar: " + fg(255, 180, 30) + h.get('avatar') + fg.rs)
                        print(fg(255, 80, 200) + "avatarfull: " + fg(255, 180, 20) + h.get('avatarfull') + fg.rs)
                        print(fg(255, 80, 190) + "lastlogoff: " + fg(255, 180, 10) + str(h.get('lastlogoff')) + fg.rs)
                        print(fg(255, 80, 180) + "loccountrycode: " + fg(255, 180, 0) + h.get('loccountrycode') + fg.rs)

                        print("")
                        system_lista = int(input("" + lang.language.langs["main"][1]))

                    if system_lista == 20:
                        break

            @staticmethod
            def GetPlayerSummaries_player():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.SteramDB_logo_v2()
                    verch.ver_ch_start()

                    menu_list_def.SteamDB_lang.SteamDB_Summaries()
                    menu_list_def.menu_def.back_text()

                    with open(ROOT_DIR + '\\config\\SteamDB_key.json', "r") as file:
                        jsonData = json.load(file)
                        keyin = jsonData['steam_key'][0]
                        system_lista = int(input("" + lang.language.langs["main"][6]))

                        if system_lista == 0:
                            webbrowser.open('https://steamcommunity.com/search/users/#text=')

                        if system_lista == 1:
                            menu_list_def.menu_def.clear()
                            logos.SteramDB_logo_v2()
                            verch.ver_ch_start()

                            print(50 * "-")
                            print(Fore.RED + 'steamcommunity.com/profiles/', (Fore.GREEN + 'xxxxxxxxxxxxxxxxx'))
                            print(Style.RESET_ALL)
                            print(50 * "-")

                            steamids = input("steamID64 (Dec): ")

                            url = (
                                    "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=" + keyin +
                                    "&steamids=" + steamids)
                            x = requests.get(url)
                            h = x.json()['response']['players'][0]

                            menu_list_def.menu_def.clear()
                            logos.SteramDB_logo_v2()
                            verch.ver_ch_start()

                            print(fg(255, 80, 250) + "steamid: " + fg(255, 180, 70) + h.get('steamid') + fg.rs)
                            print(fg(255, 80, 240) + "personaname: " + fg(255, 180, 60) + h.get('personaname') + fg.rs)
                            print(fg(255, 80, 230) + "realname: " + fg(255, 180, 50) + str(h.get('realname')) + fg.rs)
                            print(fg(255, 80, 220) + "profileurl: " + fg(255, 180, 40) + h.get('profileurl') + fg.rs)
                            print(fg(255, 80, 210) + "avatar: " + fg(255, 180, 30) + h.get('avatar') + fg.rs)
                            print(fg(255, 80, 200) + "avatarfull: " + fg(255, 180, 20) + h.get('avatarfull') + fg.rs)
                            print(
                                fg(255, 80, 190) + "lastlogoff: " + fg(255, 180, 10) + str(h.get('lastlogoff')) + fg.rs)
                            print(fg(255, 80, 180) + "loccountrycode: " + fg(255, 180, 0) + h.get(
                                'loccountrycode') + fg.rs)

                            print("")
                            system_lista = int(input("" + lang.language.langs["main"][1]))

                            if system_lista == 20:
                                break

                        if system_lista == 20:
                            break

    class BattleNET:
        @staticmethod
        def acess_token():
            config = ROOT_DIR + "\\config\\battenet.json"

            json.load(codecs.open(config, 'r', 'utf-8-sig'))
            with open(config, encoding='utf-8-sig') as f:
                configs = json.load(f)

            Client_ID = str(configs['Client_ID'][0])
            Client_Sicret = str(configs['Client_Sicret'][0])

            command = "curl -u " + Client_ID + ":" + Client_Sicret + " -d grant_type=client_credentials https://oauth.battle.net/token"
            save = command + " > c:\\temp\\battle_acess.json"
            os.system("" + save)

            config_save = "c:\\temp\\battle_acess.json"
            json.load(codecs.open(config_save, 'r', 'utf-8-sig'))
            with open(config_save, encoding='utf-8-sig') as f:
                command = json.load(f)
            keyword = "access_token: {access_token}".format(**command)

            print(keyword)

        @staticmethod
        def D3():

            file_exists = os.path.exists('c:\\temp\\battle_acess.json')
            if not file_exists:
                modul.BattleNET.acess_token()
                menu.menulista()

            if file_exists:
                config = ROOT_DIR + "\\config\\battenet.json"

                json.load(codecs.open(config, 'r', 'utf-8-sig'))
                with open(config, encoding='utf-8-sig') as f:
                    configs = json.load(f)

                account = str(configs['account'][0])
                account_id = str(configs['account_num'][0])
                locate = str(configs['locale'][0])
                region = str(configs['region'][0])

                config_save = "c:\\temp\\battle_acess.json"
                json.load(codecs.open(config_save, 'r', 'utf-8-sig'))
                with open(config_save, encoding='utf-8-sig') as f:
                    command = json.load(f)
                keyword = "{access_token}".format(**command)
                access_token = keyword
                hashtag = "%23"

                url = "https://" + region + ".api.blizzard.com/d3/profile/" + \
                      account + hashtag + account_id + "/?locale=" + locate + \
                      "&access_token=" + access_token

                print(url)
                x = requests.get(url)
                h = x.json()

                '''
                Black: \u001b[30m
                Red: \u001b[31m
                Green: \u001b[32m
                Yellow: \u001b[33m
                Blue: \u001b[34m
                Magenta: \u001b[35m
                Cyan: \u001b[36m
                White: \u001b[37m
                Reset: \u001b[0m
                '''

                a1 = "\u001b[32m battleTag: \u001b[31m{battleTag} \n" \
                     "\u001b[32m paragonLevel: \u001b[31m{paragonLevel} \n" \
                     "\u001b[32m paragonLevelHardcore: \u001b[31m{paragonLevelHardcore} \n" \
                     "\u001b[32m paragonLevelSeason: \u001b[31m{paragonLevelSeason} \n" \
                     "\u001b[32m paragonLevelSeasonHardcore: \u001b[31m{paragonLevelSeasonHardcore} \n" \
                     "\u001b[32m guildName: \u001b[31m{guildName} \n" \
                     "\u001b[32m heroes: \n" \
                     "     \u001b[31m {heroes}\n \u001b[0m".format(**h)

                a2 = "\u001b[32m lastHeroPlayed: \u001b[31m{lastHeroPlayed}\n" \
                     "\u001b[32m lastUpdated: \u001b[31m{lastUpdated}\n" \
                     "\u001b[32m kills: \n" \
                     "     \u001b[31m{kills}\n" \
                     "\u001b[32m highestHardcoreLevel: \u001b[31m{highestHardcoreLevel}\n" \
                     "\u001b[32m timePlayed: \u001b[31m{timePlayed}\n \u001b[0m".format(**h)

                a3 = "\u001b[32m progression: \n" \
                     "     \u001b[31m {progression}\n \u001b[0m".format(**h)

                a4 = "\u001b[32m seasonalProfiles: \n" \
                     "     \u001b[31m {seasonalProfiles}\n \u001b[0m".format(**h)

                a5 = "\u001b[32m timePlayed: \n" \
                     "     \u001b[31m {timePlayed}\n \u001b[0m".format(**h)

                a6 = "\u001b[32m highestHardcoreLevel: \u001b[31m{highestHardcoreLevel}\n \u001b[0m".format(**h)

                b1 = "\u001b[32m blacksmith: \n" \
                     "     \u001b[31m {blacksmith}\n" \
                     "\u001b[32m jeweler \n" \
                     "     \u001b[31m {jeweler}\n" \
                     "\u001b[32m mystic \n" \
                     "     \u001b[31m {mystic}\n" \
                     "\u001b[32m blacksmithSeason \n" \
                     "     \u001b[31m {blacksmithSeason}\n" \
                     "\u001b[32m jewelerSeason \n" \
                     "     \u001b[31m {jewelerSeason}\n" \
                     "\u001b[32m mysticSeason \n" \
                     "     \u001b[31m {mysticSeason}\n" \
                     "\u001b[32m blacksmithHardcore \n" \
                     "     \u001b[31m {blacksmithHardcore}\n" \
                     "\u001b[32m jewelerHardcore \n" \
                     "     \u001b[31m {jewelerHardcore}\n" \
                     "\u001b[32m mysticHardcore \n" \
                     "     \u001b[31m {mysticHardcore}\n" \
                     "\u001b[32m blacksmithSeasonHardcore \n" \
                     "     \u001b[31m {blacksmithSeasonHardcore}\n" \
                     "\u001b[32m jewelerSeasonHardcore \n" \
                     "     \u001b[31m {jewelerSeasonHardcore}\n" \
                     "\u001b[32m mysticSeasonHardcore \n" \
                     "     \u001b[31m {mysticSeasonHardcore}\n \u001b[0m".format(**h)

                #: {}
                print(a1 + a2 + a3 + a4 + a5 + a6 + b1)
                print("")

        @staticmethod
        def D3_hero():
            file_exists = os.path.exists('c:\\temp\\battle_acess.json')
            if not file_exists:
                modul.BattleNET.acess_token()
                menu.menulista()

            if file_exists:
                config = ROOT_DIR + "\\config\\battenet.json"

                json.load(codecs.open(config, 'r', 'utf-8-sig'))
                with open(config, encoding='utf-8-sig') as f:
                    configs = json.load(f)

                account = str(configs['account'][0])
                account_id = str(configs['account_num'][0])
                locate = str(configs['locale'][0])
                region = str(configs['region'][0])

                config_save = "c:\\temp\\battle_acess.json"
                json.load(codecs.open(config_save, 'r', 'utf-8-sig'))
                with open(config_save, encoding='utf-8-sig') as f:
                    command = json.load(f)
                keyword = "{access_token}".format(**command)
                access_token = keyword
                hashtag = "%23"

                url = "https://" + region + ".api.blizzard.com/d3/profile/" + \
                      account + hashtag + account_id + "/?locale=" + locate + \
                      "&access_token=" + access_token
                x = requests.get(url)
                h = x.json()['heroes']

                '''
                Black: \u001b[30m
                Red: \u001b[31m
                Green: \u001b[32m
                Yellow: \u001b[33m
                Blue: \u001b[34m
                Magenta: \u001b[35m
                Cyan: \u001b[36m
                White: \u001b[37m
                Reset: \u001b[0m
                '''

                '''print("Printing lists Heroes")
                print(*h, sep="\n")'''


                data = h
                s = pd.DataFrame(data[0:20], columns=data[0])
                print("-" * 122)
                print(s.to_string(index=False))
                print("-" * 122)

                print("\n")
                heroid = str(input(" " + lang.language.langs["main"][6]))

                url = "https://" + region + ".api.blizzard.com/d3/profile/" + account + hashtag + account_id + \
                      "/hero/" + heroid + "?locale=" + locate + "&access_token=" + access_token

                x = requests.get(url)
                d = x.json()
                d1 = x.json()['kills']

                s0 = x.json()['skills']['active'][0]['skill']
                s1 = x.json()['skills']['active'][1]['skill']
                s2 = x.json()['skills']['active'][2]['skill']
                s3 = x.json()['skills']['active'][3]['skill']
                s4 = x.json()['skills']['active'][4]['skill']
                s5 = x.json()['skills']['active'][5]['skill']

                i0 = x.json()['items']['head']
                i1 = x.json()['items']['neck']
                i2 = x.json()['items']['torso']
                i2_0 = x.json()['items']['torso']['dyeColor']
                i3 = x.json()['items']['shoulders']
                i3_0 = x.json()['items']['shoulders']['dyeColor']
                i4 = x.json()['items']['legs']
                i5 = x.json()['items']['waist']
                i6 = x.json()['items']['hands']
                i6_0 = x.json()['items']['hands']['dyeColor']
                i7 = x.json()['items']['bracers']
                i8 = x.json()['items']['feet']
                i9 = x.json()['items']['leftFinger']
                i10 = x.json()['items']['rightFinger']
                i11 = x.json()['items']['mainHand']

                print("\n")
                print("\u001b[31m id: \u001b[36m {id}".format(**d))
                print("\u001b[31m name: \u001b[36m {name}".format(**d))
                print("\u001b[31m gender: \u001b[36m {gender}".format(**d))
                print("\u001b[31m level: \u001b[36m {level}".format(**d))
                print("\u001b[31m paragonLevel: \u001b[36m {paragonLevel}".format(**d))
                print("\u001b[31m kills elites: \u001b[36m {elites} ".format(**d1))
                print("\u001b[31m hardcore: \u001b[36m {hardcore}".format(**d))
                print("\u001b[31m seasonal: \u001b[36m {seasonal}".format(**d))
                print("\u001b[31m seasonCreated: \u001b[36m {seasonCreated}".format(**d))

                print("\u001b[31m skills:\u001b[0m")

                print("\u001b[0m*" * 40 + "\u001b[31m skills 0 " + "\u001b[0m*" * 40)
                print("\u001b[31m       slug: \u001b[36m {slug}".format(**s0))
                print("\u001b[31m       name: \u001b[36m {name}".format(**s0))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**s0))
                print("\u001b[31m       level: \u001b[36m {level}".format(**s0))
                print("\u001b[31m       tooltipUrl: \u001b[36m {tooltipUrl}".format(**s0))
                print("\u001b[31m       description: \u001b[36m {description}".format(**s0))

                print("\u001b[0m*" * 40 + "\u001b[31m skills 1 " + "\u001b[0m*" * 40)
                print("\u001b[31m       slug: \u001b[36m {slug}".format(**s1))
                print("\u001b[31m       name: \u001b[36m {name}".format(**s1))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**s1))
                print("\u001b[31m       level: \u001b[36m {level}".format(**s1))
                print("\u001b[31m       tooltipUrl: \u001b[36m {tooltipUrl}".format(**s1))
                print("\u001b[31m       description: \u001b[36m {description}".format(**s1))

                print("\u001b[0m*" * 40 + "\u001b[31m skills 2 " + "\u001b[0m*" * 40)
                print("\u001b[31m       slug: \u001b[36m {slug}".format(**s2))
                print("\u001b[31m       name: \u001b[36m {name}".format(**s2))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**s2))
                print("\u001b[31m       level: \u001b[36m {level}".format(**s2))
                print("\u001b[31m       tooltipUrl: \u001b[36m {tooltipUrl}".format(**s2))
                print("\u001b[31m       description: \u001b[36m {description}".format(**s2))

                print("\u001b[0m*" * 40 + "\u001b[31m skills 3 " + "\u001b[0m*" * 40)
                print("\u001b[31m       slug: \u001b[36m {slug}".format(**s3))
                print("\u001b[31m       name: \u001b[36m {name}".format(**s3))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**s3))
                print("\u001b[31m       level: \u001b[36m {level}".format(**s3))
                print("\u001b[31m       tooltipUrl: \u001b[36m {tooltipUrl}".format(**s3))
                print("\u001b[31m       description: \u001b[36m {description}".format(**s3))

                print("\u001b[0m*" * 40 + "\u001b[31m skills 4 " + "\u001b[0m*" * 40)
                print("\u001b[31m       slug: \u001b[36m {slug}".format(**s4))
                print("\u001b[31m       name: \u001b[36m {name}".format(**s4))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**s4))
                print("\u001b[31m       level: \u001b[36m {level}".format(**s4))
                print("\u001b[31m       tooltipUrl: \u001b[36m {tooltipUrl}".format(**s4))
                print("\u001b[31m       description: \u001b[36m {description}".format(**s4))

                print("\u001b[0m*" * 40 + "\u001b[31m skills 5 " + "\u001b[0m*" * 40)
                print("\u001b[31m       slug: \u001b[36m {slug}".format(**s5))
                print("\u001b[31m       name: \u001b[36m {name}".format(**s5))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**s5))
                print("\u001b[31m       level: \u001b[36m {level}".format(**s5))
                print("\u001b[31m       tooltipUrl: \u001b[36m {tooltipUrl}".format(**s5))
                print("\u001b[31m       description: \u001b[36m {description}".format(**s5))

                print("\u001b[0m*" * 45 + "" + "\u001b[0m*" * 45)

                print("\u001b[31m items:".format(**d))
                print("\u001b[0m*" * 42 + "\u001b[31m head " + "\u001b[0m*" * 42)

                print("\u001b[31m   head: \u001b[36m")
                print("\u001b[31m       id: \u001b[36m {id}".format(**i0))
                print("\u001b[31m       name: \u001b[36m {name}".format(**i0))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**i0))
                print("\u001b[31m       displayColor: \u001b[36m {displayColor}".format(**i0))
                print("\u001b[31m       tooltipParams: \u001b[36m {tooltipParams}".format(**i0))

                print("\u001b[0m*" * 42 + "\u001b[31m neck " + "\u001b[0m*" * 42)
                print("\u001b[31m   neck: \u001b[36m")

                print("\u001b[31m       id: \u001b[36m {id}".format(**i1))
                print("\u001b[31m       name: \u001b[36m {name}".format(**i1))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**i1))
                print("\u001b[31m       displayColor: \u001b[36m {displayColor}".format(**i1))
                print("\u001b[31m       tooltipParams: \u001b[36m {tooltipParams}".format(**i1))

                print("\u001b[0m*" * 41 + "\u001b[31m torso " + "\u001b[0m*" * 42)
                print("\u001b[31m   torso: \u001b[36m")

                print("\u001b[31m       id: \u001b[36m {id}".format(**i2))
                print("\u001b[31m       name: \u001b[36m {name}".format(**i2))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**i2))
                print("\u001b[31m       displayColor: \u001b[36m {displayColor}".format(**i2))
                print("\u001b[31m       tooltipParams: \u001b[36m {tooltipParams}".format(**i2))
                print("\u001b[31m       dyeColor: ")
                print("\u001b[31m           id: \u001b[36m {id}".format(**i2_0))
                print("\u001b[31m           name: \u001b[36m {name}".format(**i2_0))
                print("\u001b[31m           icon: \u001b[36m {icon}".format(**i2_0))
                print("\u001b[31m           tooltipParams: \u001b[36m {tooltipParams}".format(**i2_0))

                print("\u001b[0m*" * 39 + "\u001b[31m shoulders " + "\u001b[0m*" * 40)
                print("\u001b[31m   shoulders: \u001b[36m")

                print("\u001b[31m       id: \u001b[36m {id}".format(**i3))
                print("\u001b[31m       name: \u001b[36m {name}".format(**i3))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**i3))
                print("\u001b[31m       displayColor: \u001b[36m {displayColor}".format(**i3))
                print("\u001b[31m       tooltipParams: \u001b[36m {tooltipParams}".format(**i3))
                print("\u001b[31m       dyeColor: ")
                print("\u001b[31m           id: \u001b[36m {id}".format(**i3_0))
                print("\u001b[31m           name: \u001b[36m {name}".format(**i3_0))
                print("\u001b[31m           icon: \u001b[36m {icon}".format(**i3_0))
                print("\u001b[31m           tooltipParams: \u001b[36m {tooltipParams}".format(**i3_0))

                print("\u001b[0m*" * 42 + "\u001b[31m legs " + "\u001b[0m*" * 42)
                print("\u001b[31m   legs: \u001b[36m")

                print("\u001b[31m       id: \u001b[36m {id}".format(**i4))
                print("\u001b[31m       name: \u001b[36m {name}".format(**i4))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**i4))
                print("\u001b[31m       displayColor: \u001b[36m {displayColor}".format(**i4))
                print("\u001b[31m       tooltipParams: \u001b[36m {tooltipParams}".format(**i4))

                print("\u001b[0m*" * 41 + "\u001b[31m waist " + "\u001b[0m*" * 42)
                print("\u001b[31m   waist: \u001b[36m")

                print("\u001b[31m       id: \u001b[36m {id}".format(**i5))
                print("\u001b[31m       name: \u001b[36m {name}".format(**i5))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**i5))
                print("\u001b[31m       displayColor: \u001b[36m {displayColor}".format(**i5))
                print("\u001b[31m       tooltipParams: \u001b[36m {tooltipParams}".format(**i5))

                print("\u001b[0m*" * 41 + "\u001b[31m hands " + "\u001b[0m*" * 42)
                print("\u001b[31m   hands: \u001b[36m")

                print("\u001b[31m       id: \u001b[36m {id}".format(**i6))
                print("\u001b[31m       name: \u001b[36m {name}".format(**i6))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**i6))
                print("\u001b[31m       displayColor: \u001b[36m {displayColor}".format(**i6))
                print("\u001b[31m       tooltipParams: \u001b[36m {tooltipParams}".format(**i6))
                print("\u001b[31m       dyeColor: ")
                print("\u001b[31m           id: \u001b[36m {id}".format(**i6_0))
                print("\u001b[31m           name: \u001b[36m {name}".format(**i6_0))
                print("\u001b[31m           icon: \u001b[36m {icon}".format(**i6_0))
                print("\u001b[31m           tooltipParams: \u001b[36m {tooltipParams}".format(**i6_0))

                print("\u001b[0m*" * 40 + "\u001b[31m bracers " + "\u001b[0m*" * 41)
                print("\u001b[31m   bracers: \u001b[36m")

                print("\u001b[31m       id: \u001b[36m {id}".format(**i7))
                print("\u001b[31m       name: \u001b[36m {name}".format(**i7))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**i7))
                print("\u001b[31m       displayColor: \u001b[36m {displayColor}".format(**i7))
                print("\u001b[31m       tooltipParams: \u001b[36m {tooltipParams}".format(**i7))

                print("\u001b[0m*" * 42 + "\u001b[31m feet " + "\u001b[0m*" * 42)
                print("\u001b[31m   feet: \u001b[36m")

                print("\u001b[31m       id: \u001b[36m {id}".format(**i8))
                print("\u001b[31m       name: \u001b[36m {name}".format(**i8))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**i8))
                print("\u001b[31m       displayColor: \u001b[36m {displayColor}".format(**i8))
                print("\u001b[31m       tooltipParams: \u001b[36m {tooltipParams}".format(**i8))

                print("\u001b[0m*" * 38 + "\u001b[31m leftFinger " + "\u001b[0m*" * 38)
                print("\u001b[31m   leftFinger: \u001b[36m")

                print("\u001b[31m       id: \u001b[36m {id}".format(**i9))
                print("\u001b[31m       name: \u001b[36m {name}".format(**i9))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**i9))
                print("\u001b[31m       displayColor: \u001b[36m {displayColor}".format(**i9))
                print("\u001b[31m       tooltipParams: \u001b[36m {tooltipParams}".format(**i9))

                print("\u001b[0m*" * 39 + "\u001b[31m rightFinger " + "\u001b[0m*" * 39)
                print("\u001b[31m   rightFinger: \u001b[36m")

                print("\u001b[31m       id: \u001b[36m {id}".format(**i10))
                print("\u001b[31m       name: \u001b[36m {name}".format(**i10))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**i10))
                print("\u001b[31m       displayColor: \u001b[36m {displayColor}".format(**i10))
                print("\u001b[31m       tooltipParams: \u001b[36m {tooltipParams}".format(**i10))

                print("\u001b[0m*" * 40 + "\u001b[31m mainHand " + "\u001b[0m*" * 41)
                print("\u001b[31m   mainHand: \u001b[36m")

                print("\u001b[31m       id: \u001b[36m {id}".format(**i11))
                print("\u001b[31m       name: \u001b[36m {name}".format(**i11))
                print("\u001b[31m       icon: \u001b[36m {icon}".format(**i11))
                print("\u001b[31m       displayColor: \u001b[36m {displayColor}".format(**i11))
                print("\u001b[31m       tooltipParams: \u001b[36m {tooltipParams}".format(**i11))

                print("\u001b[0m*" * 45 + "" + "\u001b[0m*" * 45)

                print("\u001b[31m followers: \u001b[36m {followers}".format(**d))

                print("\u001b[31m legendaryPowers: \u001b[36m {legendaryPowers}".format(**d))
                print("\u001b[31m progression: \u001b[36m {progression}".format(**d))
                print("\u001b[31m alive: \u001b[36m {alive}".format(**d))
                print("\u001b[31m lastUpdated: \u001b[36m {lastUpdated}".format(**d))
                print("\u001b[31m highestSoloRiftCompleted: \u001b[36m {highestSoloRiftCompleted}".format(**d))
                print("\u001b[31m stats: \u001b[36m {stats} \u001b[0m".format(**d))

    class SteamDB_finder:

        @staticmethod
        def steamdb_generate():
            menu_list_def.menu_def.clear()
            logos.SteramDB_logo_v2()
            verch.ver_ch_start()
            url = 'http://api.steampowered.com/ISteamApps/GetAppList/v2'
            x = requests.get(url)
            h = x.json()['applist']['apps']
            os.system("mkdir c:\\temp\\")
            with open(r'c:\\temp\\steamdb.txt', 'w', encoding="utf8") as fp:
                for item in h:
                    # write each item on a new line
                    fp.read("%s\n" % item)
                    print('Done' + str(item))

            menu_list_def.menu_def.clear()

            text_main = lang.language.langdb['steam_menu'][0]
            text_inf = lang.language.langdb['steam_menu'][1]

            sg.theme('DarkAmber')  # Add a little color to your windows
            # All the stuff inside your window. This is the PSG magic code compactor...
            layout = [[sg.Text(text_main)],
                      [sg.Text(text_inf)],
                      [sg.OK()]]

            # Create the Window
            window = sg.Window('Window Title', layout)
            # Event Loop to process "events"
            while True:
                event, values = window.read()
                if event in (sg.WIN_CLOSED, 'OK'):
                    break

            window.close()

        @staticmethod
        def steamdb_finder_a():
            while True:
                menu_list_def.menu_def.clear()
                logos.SteramDB_logo_v2()
                verch.ver_ch_start()
                # string to search in file
                '''word = 'Global Offensive'''
                word = input("" + lang.language.langs["main"][6])
                with open(r'c:\\temp\\steamdb.txt', 'r', encoding="utf8") as fp:
                    # read all lines in a list
                    lines = fp.readlines()
                    for line in lines:
                        # check if string present on a current line
                        if line.find(word) != -1:
                            print(word, 'string exists in file')
                            print('Line Number:', lines.index(line))
                            print('Line:', line)

                system_lista = int(input("" + lang.language.langs["main"][1]))

                if system_lista == 20:
                    break

        @staticmethod
        def steamdb_finder_b():
            menu_list_def.menu_def.clear()
            logos.SteramDB_logo_v2()
            verch.ver_ch_start()

            notepad = ROOT_DIR + "\\lang\\language.json"
            notepad_lang = ROOT_DIR + "\\lang\\notepad_lang.json"
            json.load(codecs.open(notepad, 'r', 'utf-8-sig'))
            with open(notepad, encoding='utf-8-sig') as f:
                datadb = json.load(f)

            langnote = datadb['notepad_langs']

            json.load(codecs.open(notepad_lang, 'r', 'utf-8-sig'))
            with open(notepad_lang, encoding='utf-8-sig') as f:
                notepad_lang = json.load(f)

            if langnote == ['eng']:
                app = Application().start("notepad.exe c:\\temp\\steamdb.txt")
                app.UntitledNotepad.menu_select("Edit->Find")

            if langnote == ['hun']:
                app = Application().start("notepad.exe c:\\temp\\steamdb.txt")
                app.UntitledNotepad.menu_select("S&zerkesztés->Keresés")

            if langnote == ['de']:
                app = Application().start("notepad.exe c:\\temp\\steamdb.txt")
                app.UntitledNotepad.menu_select("Bearbeiten->Suchen")

        @staticmethod
        def steam_run_game():
            appid = input("Added Appidd: ")
            prgm_path = ""
            if os.environ.get("PROGRAMFILES(X86)") is None:  # this case is 32bit
                prgm_path = os.environ.get("PROGRAMFILES")
            else:
                prgm_path = os.environ.get("PROGRAMFILES(X86)")

            print(prgm_path + "\\Steam\\steam.exe -applaunch " + appid)

            startgame = prgm_path + "\\Steam\\steam.exe -applaunch " + appid
            subprocess.Popen(startgame)

    class Accounts:
        @staticmethod
        def accounts():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.accounts_list.accounts_listA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))
                if system_lista == 0:
                    os.system("start ms-settings:yourinfo")
                if system_lista == 1:
                    os.system("start ms-settings:emailandaccounts")
                if system_lista == 2:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()

                        menu_list_def.accounts_list.menu_accounts_sigin_list()
                        menu_list_def.menu_def.back_text()
                        account_lista = int(input("" + lang.language.langs["main"][6]))

                        if account_lista == 0:
                            os.system("start ms-settings:signinoptions")
                        if account_lista == 1:
                            os.system("start ms-settings:signinoptions-launchfaceenrollment")
                        if account_lista == 2:
                            os.system("start ms-settings:signinoptions-launchfingerprintenrollment")
                        if account_lista == 3:
                            os.system("start ms-settings:signinoptions-launchsecuritykeyenrollment")
                        if account_lista == 4:
                            os.system("start ms-settings:signinoptions-dynamiclock")
                        if account_lista == 20:
                            break
                if system_lista == 3:
                    os.system("start ms-settings:workplace")
                if system_lista == 4:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()

                        menu_list_def.accounts_list.menu_accounts_family_list()
                        menu_list_def.menu_def.back_text()
                        account_lista = int(input("" + lang.language.langs["main"][6]))

                        if account_lista == 0:
                            os.system("start ms-settings:otherusers")
                        if account_lista == 1:
                            os.system("start ms-settings:assignedaccess")
                        if account_lista == 20:
                            break
                if system_lista == 5:
                    os.system("start ms-settings:sync")
                if system_lista == 20:
                    break

    class Apps:
        @staticmethod
        def apps():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.apps_list.apps_listA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()

                        menu_list_def.apps_list.menu_apps_list()
                        menu_list_def.menu_def.back_text()
                        apps_lista = int(input("" + lang.language.langs["main"][6]))

                        if apps_lista == 0:
                            os.system("start ms-settings:appsfeatures")
                        if apps_lista == 1:
                            os.system("start ms-settings:optionalfeatures")

                        if apps_lista == 20:
                            break

                if system_lista == 1:
                    os.system("start ms-settings:defaultapps")

                if system_lista == 2:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()

                        menu_list_def.apps_list.menu_apps_ofline_maps_list()
                        menu_list_def.menu_def.back_text()
                        ofline_lista = int(input("" + lang.language.langs["main"][6]))

                        if ofline_lista == 0:
                            os.system("start ms-settings:maps")
                        if ofline_lista == 1:
                            os.system("start ms-settings:maps-downloadmaps")
                        if ofline_lista == 20:
                            break

                if system_lista == 3:
                    os.system("start ms-settings:appsforwebsites")
                if system_lista == 4:
                    os.system("start ms-settings:videoplayback")
                if system_lista == 5:
                    os.system("start ms-settings:startupapps")

                if system_lista == 20:
                    break

    class Devices:
        @staticmethod
        def devices():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.devices_list.devices_listA()
                menu_list_def.menu_def.back_text()

                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    os.system("start ms-settings:bluetooth")

                if system_lista == 1:
                    os.system("start ms-settings:printers")
                if system_lista == 2:
                    os.system("start ms-settings:mousetouchpad")

                if system_lista == 3:
                    os.system("start ms-settings:devices-touchpad")

                if system_lista == 4:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.devices_list.menu_devices_typing_list()
                        menu_list_def.menu_def.back_text()
                        typing_lista = int(input("" + lang.language.langs["main"][6]))

                        if typing_lista == 0:
                            os.system("start ms-settings:typing")

                        if typing_lista == 1:
                            os.system("start ms - settings:devicestyping-hwkbtextsuggestions")

                        if typing_lista == 20:
                            break

                if system_lista == 5:
                    os.system("start ms-settings:wheel")

                if system_lista == 6:
                    os.system("start ms-settings:pen")

                if system_lista == 7:
                    os.system("start ms-settings:autoplay")

                if system_lista == 8:
                    os.system("start ms-settings:usb")

                if system_lista == 20:
                    break

    class Ease_of_Access:
        @staticmethod
        def ease_of_Access():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.ease_of_access.eace_of_access_listA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    os.system("start ms-settings:easeofaccess-display")
                if system_lista == 1:
                    os.system("start ms-settings:easeofaccess-cursorandpointersize")
                if system_lista == 2:
                    os.system("start ms-settings:easeofaccess-cursor")
                if system_lista == 3:
                    os.system("start ms-settings:easeofaccess-magnifier")
                if system_lista == 4:
                    os.system("start ms-settings:easeofaccess-colorfilter")
                if system_lista == 5:
                    os.system("start ms-settings:easeofaccess-highcontrast")
                if system_lista == 6:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.ease_of_access.ease_of_access_narrator_list()
                        menu_list_def.menu_def.back_text()
                        ease_lista = int(input("" + lang.language.langs["main"][6]))

                        if ease_lista == 0:
                            os.system("start ms-settings:easeofaccess-narrator")
                        if ease_lista == 0:
                            os.system("start ms-settings:easeofaccess-narrator-isautostartenabled")
                        if ease_lista == 20:
                            break

                if system_lista == 7:
                    os.system("start ms-settings:easeofaccess-audio")
                if system_lista == 8:
                    os.system("start ms-settings:easeofaccess-closedcaptioning")
                if system_lista == 9:
                    os.system("start ms-settings:easeofaccess-speechrecognition")
                if system_lista == 10:
                    os.system("start ms-settings:easeofaccess-keyboard")
                if system_lista == 11:
                    os.system("start ms-settings:easeofaccess-mouse")
                if system_lista == 12:
                    os.system("start ms-settings:easeofaccess-eyecontrol")

                if system_lista == 20:
                    break

    class Extras:
        @staticmethod
        def Extra():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.extra_list.extra_listA()
                menu_list_def.menu_def.extra_back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    os.system("start ms-settings:extras")
                if system_lista == 1:
                    os.system("start ms-availablenetworks:")
                if system_lista == 2:
                    os.system("start calculator:")
                if system_lista == 3:
                    os.system("start outlookcal:")
                if system_lista == 4:
                    os.system("start microsoft.windows.camera:")
                if system_lista == 5:
                    os.system("start ms-settings-connectabledevices:devicediscovery")
                if system_lista == 6:
                    os.system("start ms-clock:")
                if system_lista == 7:
                    os.system("start feedback-hub:")
                if system_lista == 8:
                    os.system("start mswindowsmusic:")
                if system_lista == 9:
                    os.system("start outlookmail:")
                if system_lista == 10:
                    os.system("start 	bingmaps:")
                if system_lista == 11:
                    os.system("start 	microsoft-edge:")
                if system_lista == 12:
                    os.system("start 	bingnews:")
                if system_lista == 13:
                    os.system("start xboxliveapp-1297287741:")
                if system_lista == 14:
                    os.system("start 	ms-windows-store:")
                if system_lista == 15:
                    os.system("start mswindowsvideo:")
                if system_lista == 16:
                    os.system("start 	ms-actioncenter:")
                if system_lista == 17:
                    os.system("start 	ms-people:")
                if system_lista == 18:
                    os.system("start 	ms-people:settings")
                if system_lista == 19:
                    os.system("start 	ms-photos:")
                if system_lista == 20:
                    os.system("start 	ms-settings-displays-topology:projection")
                if system_lista == 21:
                    os.system("start 	ms-settings:")
                if system_lista == 22:
                    os.system("start 	ms-ScreenSketch:")
                if system_lista == 23:
                    os.system("start 	ms-screenclip:")
                if system_lista == 24:
                    os.system("start ms-get-started:")
                if system_lista == 25:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.extra_list.menu_weather_list()
                        menu_list_def.menu_def.back_text()
                        weather_lista = int(input("" + lang.language.langs["main"][6]))

                        if weather_lista == 0:
                            os.system("start bingweather:")
                        if weather_lista == 1:
                            os.system("start msnweather:")
                        if weather_lista == 20:
                            break

                if system_lista == 26:
                    os.system("start windowsdefender:")
                if system_lista == 30:
                    break

    class Gaming:
        @staticmethod
        def gaming():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.gaming_list.gaming_listA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    os.system("start ms-settings:gaming-gamebar")
                if system_lista == 1:
                    os.system("start ms-settings:gaming-gamedvr")
                if system_lista == 2:
                    os.system("start ms-settings:gaming-gamemode")
                if system_lista == 3:
                    os.system("start ms-settings:gaming-xboxnetworking")
                if system_lista == 20:
                    break

    class GoodMod:
        @staticmethod
        def good():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.goodm.goodmod_listA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    result = subprocess.run([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe',
                                             r'' + start], stdout=subprocess.PIPE,
                                            stderr=subprocess.STDOUT, shell=True)
                    print(result)

                if system_lista == 1:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.goodm.power_listA()
                        menu_list_def.menu_def.back_text()
                        system_lista = int(input("" + lang.language.langs["main"][6]))

                        if system_lista == 0:
                            os.system("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")

                        if system_lista == 1:
                            os.system("start powercfg.cpl")

                        if system_lista == 2:
                            menu_list_def.menu_def.clear()
                            logos.main_logo()
                            verch.ver_ch_start()
                            menu_list_def.goodm.power_menu_listA()
                            menu_list_def.menu_def.back_text()

                            Popen('powershell ' + power_set, creationflags=CREATE_NEW_CONSOLE)
                            system_lista = input("" + lang.language.langs["main"][9])
                            os.system("powercfg /setactive " + system_lista)

                            if system_lista == 20:
                                break

                        if system_lista == 20:
                            break

                if system_lista == 2:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.microsoft.microsoft_listA()
                        menu_list_def.menu_def.back_text()
                        system_lista = int(input("" + lang.language.langs["main"][6]))

                        if system_lista == 0:
                            Popen('powershell ' + ms_list, creationflags=CREATE_NEW_CONSOLE)

                        if system_lista == 1:
                            Popen('powershell ' + win_install, creationflags=CREATE_NEW_CONSOLE)

                        if system_lista == 2:
                            Popen('powershell ' + win_upgrade, creationflags=CREATE_NEW_CONSOLE)

                        if system_lista == 3:
                            os.system("winget import " + C_DIR_IN)

                        if system_lista == 4:
                            os.system("winget export " + C_DIR_EX)

                        if system_lista == 5:
                            while True:
                                menu_list_def.menu_def.clear()
                                logos.main_logo()
                                verch.ver_ch_start()
                                menu_list_def.microsoft.microsoft_install()
                                menu_list_def.menu_def.back_text()

                                if system_lista == 0:
                                    Popen('powershell ' + win_search, creationflags=CREATE_NEW_CONSOLE)

                                if system_lista == 1:
                                    system_lista = input("" + lang.language.langs["main"][9])
                                    os.system("winget install " + system_lista)

                                if system_lista == 20:
                                    break

                        if system_lista == 6:
                            while True:
                                menu_list_def.menu_def.clear()
                                logos.main_logo()
                                verch.ver_ch_start()
                                menu_list_def.microsoft.microsoft_uninstall()
                                menu_list_def.menu_def.back_text()
                                system_lista = int(input("" + lang.language.langs["main"][6]))

                                if system_lista == 0:
                                    Popen('powershell ' + win_install, creationflags=CREATE_NEW_CONSOLE)

                                if system_lista == 1:
                                    system_lista = input("" + lang.language.langs["main"][9])
                                    os.system("winget uninstall " + system_lista)

                                if system_lista == 20:
                                    break

                        if system_lista == 20:
                            break

                if system_lista == 3:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.goodm.Update_Fixer()
                        menu_list_def.menu_def.back_text()
                        system_lista = int(input("" + lang.language.langs["main"][6]))

                        if system_lista == 0:
                            Popen('powershell ' + update_powershell, creationflags=CREATE_NEW_CONSOLE)

                        if system_lista == 1:
                            Popen('powershell ' + update_powershell_fixer, creationflags=CREATE_NEW_CONSOLE)

                        if system_lista == 2:
                            Popen('powershell ' + steam_fix, creationflags=CREATE_NEW_CONSOLE)

                        if system_lista == 3:
                            Popen('powershell ' + restart_vga_driver, creationflags=CREATE_NEW_CONSOLE)
                            system_lista = input("" + lang.language.langs["main"][10])

                            ''' 
                            "x" - Create - will create a file, returns an error if the file exist 
                            "a" - Append - will create a file if the specified file does not exist
                            "w" - Write - will create a file if the specified file does not exist
                            '''

                            f = open(C_DIR_VGA_IN + "ScriptVGARestart.ps1", "w")
                            f.write(restart_vga_id + vga_list + system_lista + vga_list)
                            f.close()

                            file = restart_vga_driver_start
                            Popen('powershell ' + file)

                        if system_lista == 20:
                            break

                if system_lista == 4:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.goodm.Windows_Defender()
                        menu_list_def.menu_def.back_text()
                        system_lista = int(input("" + lang.language.langs["main"][6]))

                        if system_lista == 0:
                            Popen('powershell ' + w_scan_updates, creationflags=CREATE_NEW_CONSOLE)

                        if system_lista == 1:
                            Popen('powershell ' + w_scan_Quick, creationflags=CREATE_NEW_CONSOLE)

                        if system_lista == 2:
                            Popen('powershell ' + w_scan_Full, creationflags=CREATE_NEW_CONSOLE)

                        if system_lista == 20:
                            break

                if system_lista == 20:
                    break

    class Mixed_reality:
        @staticmethod
        def mixed_reality():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.mixed_reality.mixed_reality_listA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    os.system("start ms-settings:holographic-audio")
                if system_lista == 1:
                    os.system("start ms-settings:privacy-holographic-environment")
                if system_lista == 2:
                    os.system("start ms-settings:holographic-headset")
                if system_lista == 3:
                    os.system("start ms-settings:holographic-management")
                if system_lista == 20:
                    break

    class my_script:
        @staticmethod
        def beta_my_script():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.beta.beta_project_lang()
                menu_list_def.menu_def.exits_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    Popen('powershell ' + net_disabled, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 1:
                    Popen('powershell ' + net_enabled, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 2:
                    Popen('powershell ' + host_edit, creationflags=CREATE_NEW_CONSOLE)

                if system_lista == 20:
                    break

    class Network_Internet:
        @staticmethod
        def networks():
            while True:
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.network_list.network_listA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    while True:
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.network_list.menu_network_status_list()
                        menu_list_def.menu_def.back_text()

                        net_list = int(input("" + lang.language.langs["main"][6]))

                        if net_list == 0:
                            os.system("start ms-settings:network-status")
                        if net_list == 1:
                            os.system("start ms-settings:datausage")
                        if net_list == 2:
                            os.system("start ms-availablenetworks:")

                        if net_list == 20:
                            break

                if system_lista == 1:
                    os.system("start ms-settings:network-cellular")

                if system_lista == 2:
                    while True:
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.network_list.menu_network_wifi_list()
                        menu_list_def.menu_def.back_text()

                        wifi_list = int(input("" + lang.language.langs["main"][6]))

                        if wifi_list == 0:
                            os.system("start ms-settings:network-wifi")

                        if wifi_list == 1:
                            os.system("start ms-availablenetworks:")

                        if wifi_list == 2:
                            os.system("start ms-settings:network-wifisettings")

                        if wifi_list == 20:
                            break

                if system_lista == 3:
                    os.system("start ms-settings:network-wificalling")

                if system_lista == 4:
                    os.system("start ms-settings:network-ethernet")

                if system_lista == 5:
                    os.system("start ms-settings:network-dialup")

                if system_lista == 6:
                    os.system("start ms-settings:network-directaccess")

                if system_lista == 7:
                    os.system("start ms-settings:network-vpn")

                if system_lista == 8:
                    os.system("start ms-settings:network-airplanemode")

                if system_lista == 9:
                    os.system("start ms-settings:network-mobilehotspot")

                if system_lista == 10:
                    os.system("start ms-settings:nfctransactions")

                if system_lista == 11:
                    os.system("start ms-settings:network-proxy")

                if system_lista == 20:
                    break

    class Personalization:
        @staticmethod
        def personalization():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.personalization_list.personalization_listA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    os.system("start ms-settings:personalization-background")
                if system_lista == 1:
                    os.system("start ms-settings:colors")
                if system_lista == 2:
                    os.system("start ms-settings:lockscreen")
                if system_lista == 3:
                    os.system("start ms-settings:themes")
                if system_lista == 4:
                    os.system("start ms-settings:fonts")
                if system_lista == 5:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.personalization_list.menu_start_personalization_list()
                        menu_list_def.menu_def.back_text()
                        start_lista = int(input("" + lang.language.langs["main"][6]))

                        if start_lista == 0:
                            os.system("start ms-settings:personalization-start")
                        if start_lista == 1:
                            os.system("start ms-settings:personalization-start-places")

                        if start_lista == 20:
                            break

                if system_lista == 6:
                    os.system("start ms-settings:taskbar")

                if system_lista == 20:
                    break

    class Phone:
        @staticmethod
        def phone():
            while True:
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.phone_list.phone_listA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    os.system("start ms-settings:mobile-devices")

                if system_lista == 1:
                    os.system("start ms-settings:mobile-devices-addphone")

                if system_lista == 2:
                    os.system("start ms-settings:mobile-devices-addphone-direct")

                if system_lista == 20:
                    break

    class Privacy:
        @staticmethod
        def privacy():
            while True:
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.privacy.privacy_listA()
                menu_list_def.menu_def.extra_back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    os.system("start ms-settings:privacy")
                if system_lista == 1:
                    os.system("start ms-settings:privacy-speech")
                if system_lista == 2:
                    os.system("start ms-settings:privacy-speechtyping")
                if system_lista == 3:
                    while True:
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.privacy.privacy_diagnostics_list()
                        menu_list_def.menu_def.back_text()
                        diagnostics_lista = int(input("" + lang.language.langs["main"][6]))

                        if diagnostics_lista == 0:
                            os.system("start ms-settings:privacy-feedback")
                        if diagnostics_lista == 1:
                            os.system("start ms-settings:privacy-feedback")
                        if diagnostics_lista == 20:
                            break
                if system_lista == 4:
                    os.system("start ms-settings:privacy-activityhistory")
                if system_lista == 5:
                    os.system("start ms-settings:privacy-location")
                if system_lista == 6:
                    os.system("start ms-settings:privacy-webcam")
                if system_lista == 7:
                    os.system("start ms-settings:privacy-microphone")
                if system_lista == 8:
                    os.system("start ms-settings:privacy-voiceactivation")
                if system_lista == 9:
                    os.system("start ms-settings:privacy-notifications")
                if system_lista == 10:
                    os.system("start ms-settings:privacy-accountinfo")
                if system_lista == 11:
                    os.system("start ms-settings:privacy-contacts")
                if system_lista == 12:
                    os.system("start ms-settings:privacy-calendar")
                if system_lista == 13:
                    os.system("start ms-settings:privacy-phonecalls")
                if system_lista == 14:
                    os.system("start ms-settings:privacy-callhistory")
                if system_lista == 15:
                    os.system("start ms-settings:privacy-email")
                if system_lista == 16:
                    os.system("start ms-settings:privacy-eyetracker")
                if system_lista == 17:
                    os.system("start ms-settings:privacy-tasks")
                if system_lista == 18:
                    os.system("start ms-settings:privacy-messaging")
                if system_lista == 19:
                    os.system("start ms-settings:privacy-radios")
                if system_lista == 20:
                    os.system("start ms-settings:privacy-customdevices")
                if system_lista == 21:
                    os.system("start ms-settings:privacy-backgroundapps")
                if system_lista == 22:
                    os.system("start ms-settings:privacy-appdiagnostics")
                if system_lista == 23:
                    os.system("start ms-settings:privacy-automaticfiledownloads")
                if system_lista == 24:
                    os.system("start ms-settings:privacy-documents")
                if system_lista == 25:
                    os.system("start ms-settings:privacy-downloadsfolder")
                if system_lista == 26:
                    os.system("start ms-settings:privacy-pictures")
                if system_lista == 27:
                    os.system("start ms-settings:privacy-documents")
                if system_lista == 28:
                    os.system("start ms-settings:privacy-broadfilesystemaccess")

                if system_lista == 30:
                    break

    class Search:
        @staticmethod
        def search():
            while True:
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.search.search_listA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    os.system("start ms-settings:search-permissions")
                if system_lista == 1:
                    os.system("start ms-settings:cortana-windowssearch")
                if system_lista == 20:
                    break

    class Shell_Command:
        @staticmethod
        def menu():
            modul.Shell_Command.shell_command.shell_cmd_list_0()

        class shell_command:
            @staticmethod
            def shell_cmd_list_0():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.shell.shell_commands_list_0()
                    menu_list_def.menu_def.next_text()
                    menu_list_def.menu_def.back_text()
                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        os.system('explorer "shell:3D Objects"')
                    if system_lista == 1:
                        os.system('explorer "shell:AccountPictures"')
                    if system_lista == 2:
                        os.system('explorer "shell:AddNewProgramsFolder"')
                    if system_lista == 3:
                        os.system('explorer "shell:Administrative Tools"')
                    if system_lista == 4:
                        os.system('explorer "shell:AppData"')
                    if system_lista == 5:
                        os.system('explorer "shell:Application Shortcuts"')
                    if system_lista == 6:
                        os.system('explorer "shell:AppsFolder"')
                    if system_lista == 7:
                        os.system('explorer "shell:AppUpdatesFolder"')
                    if system_lista == 8:
                        os.system('explorer "shell:Cache"')
                    if system_lista == 9:
                        os.system('explorer "shell:Camera Roll"')
                    if system_lista == 10:
                        os.system('explorer "shell:CD Burning"')
                    if system_lista == 11:
                        modul.Shell_Command.shell_command.shell_cmd_list_1()

                    if system_lista == 20:
                        break

            @staticmethod
            def shell_cmd_list_1():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.shell.shell_commands_list_1()
                    menu_list_def.menu_def.next_text()
                    menu_list_def.menu_def.back_text()
                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        os.system('explorer "shell:ChangeRemoveProgramsFolder"')
                    if system_lista == 1:
                        os.system('explorer "shell:Common Administrative Tools"')
                    if system_lista == 2:
                        os.system('explorer "shell:Common AppData"')
                    if system_lista == 3:
                        os.system('explorer "shell:Common Desktop"')
                    if system_lista == 4:
                        os.system('explorer "shell:Common Documents"')
                    if system_lista == 5:
                        os.system('explorer "shell:CommonDownloads"')
                    if system_lista == 6:
                        os.system('explorer "shell:CommonMusic"')
                    if system_lista == 7:
                        os.system('explorer "shell:CommonPictures"')
                    if system_lista == 8:
                        os.system('explorer "shell:Common Programs"')
                    if system_lista == 9:
                        os.system('explorer "shell:CommonRingtones"')
                    if system_lista == 10:
                        os.system('explorer "shell:Common Start Menu"')

                    if system_lista == 11:
                        modul.Shell_Command.shell_command.shell_cmd_list_2()

                    if system_lista == 20:
                        break

            @staticmethod
            def shell_cmd_list_2():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.shell.shell_commands_list_2()
                    menu_list_def.menu_def.next_text()
                    menu_list_def.menu_def.back_text()
                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        os.system('explorer "shell:Common Startup"')
                    if system_lista == 1:
                        os.system('explorer "shell:Common Templates"')
                    if system_lista == 2:
                        os.system('explorer "shell:CommonVideo"')
                    if system_lista == 3:
                        os.system('explorer "shell:ConflictFolder"')
                    if system_lista == 4:
                        os.system('explorer "shell:ConnectionsFolder"')
                    if system_lista == 5:
                        os.system('explorer "shell:Contacts"')
                    if system_lista == 6:
                        os.system('explorer "shell:ControlPanelFolder"')
                    if system_lista == 7:
                        os.system('explorer "shell:Cookies"')
                    if system_lista == 8:
                        os.system('explorer "shell:Cookies\\Low"')
                    if system_lista == 9:
                        os.system('explorer "shell:CredentialManager"')
                    if system_lista == 10:
                        os.system('explorer "shell:CryptoKeys"')

                    if system_lista == 11:
                        modul.Shell_Command.shell_command.shell_cmd_list_3()

                    if system_lista == 20:
                        break

            @staticmethod
            def shell_cmd_list_3():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.shell.shell_commands_list_3()
                    menu_list_def.menu_def.next_text()
                    menu_list_def.menu_def.back_text()
                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        os.system('explorer "shell:desktop"')
                    if system_lista == 1:
                        os.system('explorer "shell:device Metadata Store"')
                    if system_lista == 2:
                        os.system('explorer "shell:documentsLibrary"')
                    if system_lista == 3:
                        os.system('explorer "shell:downloads"')
                    if system_lista == 4:
                        os.system('explorer "shell:dpapiKeys"')
                    if system_lista == 5:
                        os.system('explorer "shell:Favorites"')
                    if system_lista == 6:
                        os.system('explorer "shell:Fonts"')
                    if system_lista == 7:
                        os.system('explorer "shell:Games"')
                    if system_lista == 8:
                        os.system('explorer "shell:GameTasks"')
                    if system_lista == 9:
                        os.system('explorer "shell:History"')
                    if system_lista == 10:
                        os.system('explorer "shell:HomeGroupCurrentUserFolder"')

                    if system_lista == 11:
                        modul.Shell_Command.shell_command.shell_cmd_list_4()

                    if system_lista == 20:
                        break

            @staticmethod
            def shell_cmd_list_4():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.shell.shell_commands_list_4()
                    menu_list_def.menu_def.next_text()
                    menu_list_def.menu_def.back_text()
                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        os.system('explorer "shell:HomeGroupFolder"')
                    if system_lista == 1:
                        os.system('explorer "shell:ImplicitAppShortcuts	"')
                    if system_lista == 2:
                        os.system('explorer "shell:InternetFolder"')
                    if system_lista == 3:
                        os.system('explorer "shell:Libraries"')
                    if system_lista == 4:
                        os.system('explorer "shell:Links"')
                    if system_lista == 5:
                        os.system('explorer "shell:Local AppData"')
                    if system_lista == 6:
                        os.system('explorer "shell:LocalAppDataLow"')
                    if system_lista == 7:
                        os.system('explorer "shell:LocalAppDataLow"')
                    if system_lista == 8:
                        os.system('explorer "shell:MyComputerFolder"')
                    if system_lista == 9:
                        os.system('explorer "shell:My Music"')
                    if system_lista == 10:
                        os.system('explorer "shell:My Pictures"')

                    if system_lista == 11:
                        modul.Shell_Command.shell_command.shell_cmd_list_5()

                    if system_lista == 20:
                        break

            @staticmethod
            def shell_cmd_list_5():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.shell.shell_commands_list_5()
                    menu_list_def.menu_def.next_text()
                    menu_list_def.menu_def.back_text()
                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        os.system('explorer "shell:My Video"')
                    if system_lista == 1:
                        os.system('explorer "shell:NetHood"')
                    if system_lista == 2:
                        os.system('explorer "shell:NetworkPlacesFolder"')
                    if system_lista == 3:
                        os.system('explorer "shell:OneDrive	"')
                    if system_lista == 4:
                        os.system('explorer "shell:OneDriveCameraRoll"')
                    if system_lista == 5:
                        os.system('explorer "shell:OneDriveDocuments"')
                    if system_lista == 6:
                        os.system('explorer "shell:OneDriveMusic"')
                    if system_lista == 7:
                        os.system('explorer "shell:OneDrivePictures"')
                    if system_lista == 8:
                        os.system('explorer "shell:Personal"')
                    if system_lista == 9:
                        os.system('explorer "shell:PicturesLibrary"')
                    if system_lista == 10:
                        os.system('explorer "shell:PrintersFolder"')

                    if system_lista == 11:
                        modul.Shell_Command.shell_command.shell_cmd_list_6()

                    if system_lista == 20:
                        break

            @staticmethod
            def shell_cmd_list_6():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.shell.shell_commands_list_6()
                    menu_list_def.menu_def.next_text()
                    menu_list_def.menu_def.back_text()
                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        os.system('explorer "shell:PrintHood"')
                    if system_lista == 1:
                        os.system('explorer "shell:Profile"')
                    if system_lista == 2:
                        os.system('explorer "shell:ProgramFiles"')
                    if system_lista == 3:
                        os.system('explorer "shell:ProgramFilesCommon"')
                    if system_lista == 4:
                        os.system('explorer "shell:ProgramFilesCommonX64"')
                    if system_lista == 5:
                        os.system('explorer "shell:ProgramFilesCommonX86"')
                    if system_lista == 6:
                        os.system('explorer "shell:ProgramFilesX64"')
                    if system_lista == 7:
                        os.system('explorer "shell:ProgramFilesX86"')
                    if system_lista == 8:
                        os.system('explorer "shell:Programs"')
                    if system_lista == 9:
                        os.system('explorer "shell:Public"')
                    if system_lista == 10:
                        os.system('explorer "shell:PublicAccountPictures"')

                    if system_lista == 11:
                        modul.Shell_Command.shell_command.shell_cmd_list_7()

                    if system_lista == 20:
                        break

            @staticmethod
            def shell_cmd_list_7():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.shell.shell_commands_list_7()
                    menu_list_def.menu_def.next_text()
                    menu_list_def.menu_def.back_text()
                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        os.system('explorer "shell:PublicGameTasks"')
                    if system_lista == 1:
                        os.system('explorer "shell:PublicLibraries"')
                    if system_lista == 2:
                        os.system('explorer "shell:Quick Launch"')
                    if system_lista == 3:
                        os.system('explorer "shell:Recent"')
                    if system_lista == 4:
                        os.system('explorer "shell:RecordedTVLibrary"')
                    if system_lista == 5:
                        os.system('explorer "shell:RecycleBinFolder"')
                    if system_lista == 6:
                        os.system('explorer "shell:ResourceDir"')
                    if system_lista == 7:
                        os.system('explorer "shell:Ringtones"')
                    if system_lista == 8:
                        os.system('explorer "shell:Roamed Tile Images"')
                    if system_lista == 9:
                        os.system('explorer "shell:Roaming Tiles"')
                    if system_lista == 10:
                        os.system('explorer "shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}"')

                    if system_lista == 11:
                        modul.Shell_Command.shell_command.shell_cmd_list_8()

                    if system_lista == 20:
                        break

            @staticmethod
            def shell_cmd_list_8():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.shell.shell_commands_list_8()
                    menu_list_def.menu_def.next_text()
                    menu_list_def.menu_def.back_text()
                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        os.system('explorer "shell:SavedGames"')
                    if system_lista == 1:
                        os.system('explorer "shell:Screenshots"')
                    if system_lista == 2:
                        os.system('explorer "shell:Searches"')
                    if system_lista == 3:
                        os.system('explorer "shell:SearchHistoryFolder"')
                    if system_lista == 4:
                        os.system('explorer "shell:SearchHomeFolder"')
                    if system_lista == 5:
                        os.system('explorer "shell:SearchTemplatesFolder"')
                    if system_lista == 6:
                        os.system('explorer "shell:SendTo"')
                    if system_lista == 7:
                        os.system('explorer "shell:Start Menu"')
                    if system_lista == 8:
                        os.system('explorer "shell:StartMenuAllPrograms"')
                    if system_lista == 9:
                        os.system('explorer "shell:Startup"')
                    if system_lista == 10:
                        os.system('explorer "shell:SyncCenterFolder"')

                    if system_lista == 11:
                        modul.Shell_Command.shell_command.shell_cmd_list_9()

                    if system_lista == 20:
                        break

            @staticmethod
            def shell_cmd_list_9():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.shell.shell_commands_list_9()
                    menu_list_def.menu_def.next_text()
                    menu_list_def.menu_def.back_text()
                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        os.system('explorer "shell:SyncResultsFolder"')
                    if system_lista == 1:
                        os.system('explorer "shell:SyncSetupFolder"')
                    if system_lista == 2:
                        os.system('explorer "shell:System"')
                    if system_lista == 3:
                        os.system('explorer "shell:SystemCertificates"')
                    if system_lista == 4:
                        os.system('explorer "shell:SystemX86"')
                    if system_lista == 5:
                        os.system('explorer "shell:Templates"')
                    if system_lista == 6:
                        os.system('explorer "shell:ThisPCDesktopFolder"')
                    if system_lista == 7:
                        os.system('explorer "shell:UsersFilesFolder"')
                    if system_lista == 8:
                        os.system('explorer "shell:UsersFilesFolder"')
                    if system_lista == 9:
                        os.system('explorer "shell:UserProfiles"')
                    if system_lista == 10:
                        os.system('explorer "shell:UserProgramFiles"')

                    if system_lista == 11:
                        modul.Shell_Command.shell_command.shell_cmd_list_10()

                    if system_lista == 20:
                        break

            @staticmethod
            def shell_cmd_list_10():
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.shell.shell_commands_list_10()
                    menu_list_def.menu_def.back_to_menu_text()
                    menu_list_def.menu_def.back_text()
                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        os.system('explorer "shell:UserProgramFilesCommon"')
                    if system_lista == 1:
                        os.system('explorer "shell:UsersLibrariesFolder"')
                    if system_lista == 2:
                        os.system('explorer "shell:VideosLibrary"')
                    if system_lista == 3:
                        os.system('explorer "shell:Windows"')

                    if system_lista == 11:
                        menu.menulista()

                    if system_lista == 20:
                        break

    class Surface_Hub:
        @staticmethod
        def surface_hub():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.surface_hub.surface_hub_listA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    os.system("start ms-settings:surfacehub-accounts")
                if system_lista == 1:
                    os.system("start ms-settings:surfacehub-calling")
                if system_lista == 2:
                    os.system("start ms-settings:surfacehub-devicemanagenent")
                if system_lista == 3:
                    os.system("start ms-settings:surfacehub-sessioncleanup")
                if system_lista == 4:
                    os.system("start ms-settings:surfacehub-welcome")
                if system_lista == 20:
                    break

    class System:
        @staticmethod
        def systems():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.system_lista.system_listaA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                """Display SYSTEM LIST"""
                if system_lista == 0:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.system_lista.menu_system_display_list()
                        menu_list_def.menu_def.back_text()
                        display_lista = int(input("" + lang.language.langs["main"][6]))

                        if display_lista == 0:
                            os.system("start ms-settings:display")
                        if display_lista == 1:
                            os.system("start ms-settings:nightlight")
                        if display_lista == 2:
                            os.system("start ms-settings:display-advanced")
                        if display_lista == 3:
                            os.system("start ms-settings-connectabledevices:devicediscovery")
                        if display_lista == 4:
                            os.system("start ms-settings:display-advancedgraphics")

                        if display_lista == 20:
                            break

                """Sound (build 17063) SYSTEM LIST"""
                if system_lista == 1:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.system_lista.menu_system_audio_list()
                        menu_list_def.menu_def.back_text()
                        display_lista = int(input("" + lang.language.langs["main"][6]))

                        if display_lista == 0:
                            os.system("start ms-settings:sound")

                        if display_lista == 1:
                            os.system("start ms-settings:sound-devices")

                        if display_lista == 2:
                            os.system("start ms-settings:apps-volume")

                        if display_lista == 20:
                            break

                """	Notifications & actions  SYSTEM LIST"""
                if system_lista == 2:
                    os.system("start ms-settings:notifications")

                """Focus assist (build 17074) SYSTEM LIST"""
                if system_lista == 3:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.system_lista.menu_system_focus_list()
                        menu_list_def.menu_def.back_text()
                        display_lista = int(input("" + lang.language.langs["main"][6]))

                        if display_lista == 0:
                            os.system("start ms-settings:quiethours")

                        if display_lista == 1:
                            os.system("start ms-settings:quietmomentsscheduled")

                        if display_lista == 2:
                            os.system("start ms-settings:quietmomentspresentation")

                        if display_lista == 3:
                            os.system("start ms-settings:quietmomentsgame")

                        if display_lista == 20:
                            break

                """Power & sleep SYSTEM LIST"""
                if system_lista == 4:
                    os.system("start ms-settings:powersleep")

                """	Battery SYSTEM LIST"""
                if system_lista == 5:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.system_lista.menu_system_battery_list()
                        menu_list_def.menu_def.back_text()
                        display_lista = int(input("" + lang.language.langs["main"][6]))

                        if display_lista == 0:
                            os.system("start ms-settings:batterysaver")

                        if display_lista == 1:
                            os.system("start ms-settings:batterysaver-usagedetails")

                        if display_lista == 2:
                            os.system("start ms-settings:batterysaver-settings")

                        if display_lista == 20:
                            break

                """Storage SYSTEM LIST"""
                if system_lista == 6:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.system_lista.menu_system_storage_list()
                        menu_list_def.menu_def.back_text()
                        display_lista = int(input("" + lang.language.langs["main"][6]))

                        if display_lista == 0:
                            os.system("start ms-settings:storagesense")

                        if display_lista == 1:
                            os.system("start ms-settings:storagepolicies")

                        if display_lista == 2:
                            os.system("start ms-settings:savelocations")

                        if display_lista == 20:
                            break

                """Tablet SYSTEM LIST"""
                if system_lista == 7:
                    os.system("start ms-settings:tabletmode")

                """Multitasking SYSTEM LIST"""
                if system_lista == 8:
                    os.system("start ms-settings:multitasking")

                """	Projecting to this PC SYSTEM LIST"""
                if system_lista == 9:
                    os.system("start ms-settings:project")

                """Shared experiences SYSTEM LIST"""
                if system_lista == 10:
                    os.system("start ms-settings:crossdevice")

                """Clipboard (build 17666) SYSTEM LIST"""
                if system_lista == 11:
                    os.system("start ms-settings:clipboard")

                """Remote Desktop SYSTEM LIST"""
                if system_lista == 12:
                    os.system("start ms-settings:remotedesktop")

                """Device Encryption (if available) SYSTEM LIST"""
                if system_lista == 13:
                    os.system("start ms-settings:deviceencryption")

                """About SYSTEM LIST"""
                if system_lista == 14:
                    os.system("start ms-settings:about")

                if system_lista == 20:
                    break

    class Time_Language:
        @staticmethod
        def time_language():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.time_language_list.time_language_listA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    os.system('start ms-settings:dateandtime')
                if system_lista == 1:
                    os.system('start ms-settings:regionlanguage-jpnime')
                if system_lista == 2:
                    os.system('start ms-settings:regionlanguage-chsime-pinyin')
                if system_lista == 5:
                    os.system('start ms-settings:regionlanguage-chsime-wubi')
                if system_lista == 4:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.time_language_list.menu_time_language_language_list()
                        menu_list_def.menu_def.back_text()
                        language_lista = int(input("" + lang.language.langs["main"][6]))

                        if language_lista == 0:
                            os.system('start ms-settings:regionlanguage')
                        if language_lista == 1:
                            os.system('start ms-settings:regionlanguage-setdisplaylanguage')
                        if language_lista == 2:
                            os.system('start ms-settings:regionlanguage-adddisplaylanguage')
                        if language_lista == 20:
                            break
                if system_lista == 5:
                    os.system('start ms-settings:speech')
                if system_lista == 20:
                    break

    class Update_Security:
        @staticmethod
        def update():
            while True:
                menu_list_def.menu_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.update.update_listA()
                menu_list_def.menu_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.update.windows_menu_update_list()
                        menu_list_def.menu_def.back_text()
                        update_lista = int(input("" + lang.language.langs["main"][6]))

                        if update_lista == 0:
                            os.system("start ms-settings:windowsupdate")
                        if update_lista == 1:
                            os.system("start ms-settings:windowsupdate-action")
                        if update_lista == 2:
                            os.system("start ms-settings:windowsupdate-optionalupdates")
                        if update_lista == 3:
                            os.system("start ms-settings:windowsupdate-activehours")
                        if update_lista == 4:
                            os.system("start ms-settings:windowsupdate-history")
                        if update_lista == 5:
                            os.system("start ms-settings:windowsupdate-restartoptions")
                        if update_lista == 6:
                            os.system("start ms-settings:windowsupdate-options")

                        if update_lista == 20:
                            break

                if system_lista == 1:
                    os.system("start ms-settings:delivery-optimization")
                if system_lista == 2:
                    while True:
                        menu_list_def.menu_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.update.windows_menu_security_list()
                        menu_list_def.menu_def.back_text()
                        security_lista = int(input("" + lang.language.langs["main"][6]))

                        if security_lista == 0:
                            os.system("start ms-settings:windowsdefender")
                        if security_lista == 1:
                            os.system("start windowsdefender:")
                        if security_lista == 20:
                            break

                if system_lista == 3:
                    os.system("start ms-settings:backup")
                if system_lista == 4:
                    os.system("start ms-settings:troubleshoot")
                if system_lista == 5:
                    os.system("start ms-settings:recovery")
                if system_lista == 6:
                    os.system("start ms-settings:activation")
                if system_lista == 7:
                    os.system("start ms-settings:findmydevice")
                if system_lista == 8:
                    os.system("start ms-settings:developers")
                if system_lista == 9:
                    os.system("start ms-settings:windowsinsider")

                if system_lista == 20:
                    break

    class Sysinfo_all:
        @staticmethod
        def Sysinfo_win():
            print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "Sys Info", fg(250, 195, 60), "-" * 40, fg.rs + "\n")
            uname = platform.uname()
            print(
                fg(250, 200, 0) + "S" +
                fg(250, 190, 0) + "y" +
                fg(250, 180, 0) + "s" +
                fg(250, 170, 0) + "t" +
                fg(250, 160, 0) + "e" +
                fg(250, 150, 0) + "m" +
                fg(250, 140, 0) + ": " +
                fg(250, 105, 60) + f"{uname.system}" + fg.rs)
            print(
                fg(250, 200, 0) + "N" +
                fg(250, 190, 0) + "o" +
                fg(250, 180, 0) + "d" +
                fg(250, 170, 0) + "e " +
                fg(250, 160, 0) + "N" +
                fg(250, 150, 0) + "a" +
                fg(250, 140, 0) + "m" +
                fg(250, 130, 0) + "e" +
                fg(250, 120, 0) + ": " +
                fg(250, 105, 60) + f"{uname.node}" + fg.rs)
            print(
                fg(250, 200, 0) + "R" +
                fg(250, 190, 0) + "e" +
                fg(250, 180, 0) + "l" +
                fg(250, 170, 0) + "e" +
                fg(250, 160, 0) + "a" +
                fg(250, 150, 0) + "s" +
                fg(250, 140, 0) + "e" +
                fg(250, 130, 0) + ": " +
                fg(250, 105, 60) + f"{uname.release}" + fg.rs)
            print(
                fg(250, 200, 0) + "V" +
                fg(250, 190, 0) + "e" +
                fg(250, 180, 0) + "r" +
                fg(250, 170, 0) + "s" +
                fg(250, 160, 0) + "i" +
                fg(250, 150, 0) + "o" +
                fg(250, 140, 0) + "n" +
                fg(250, 130, 0) + ": " +
                fg(250, 105, 60) + f"{uname.version}" + fg.rs)
            print(
                fg(250, 200, 0) + "M" +
                fg(250, 190, 0) + "a" +
                fg(250, 180, 0) + "c" +
                fg(250, 170, 0) + "h" +
                fg(250, 160, 0) + "i" +
                fg(250, 150, 0) + "n" +
                fg(250, 140, 0) + "e" +
                fg(250, 130, 0) + ": " +
                fg(250, 105, 60) + f"{uname.machine}" + fg.rs)
            print(
                fg(250, 200, 0) + "P" +
                fg(250, 190, 0) + "r" +
                fg(250, 180, 0) + "o" +
                fg(250, 170, 0) + "c" +
                fg(250, 160, 0) + "e" +
                fg(250, 150, 0) + "s" +
                fg(250, 140, 0) + "s" +
                fg(250, 130, 0) + "o" +
                fg(250, 120, 0) + "r" +
                fg(250, 110, 0) + ": " +
                fg(250, 105, 60) + f"{uname.processor}" + fg.rs + "\n")

        @staticmethod
        def Sysinfo_boot():
            print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "Boot Time", fg(250, 195, 60), "-" * 40, fg.rs + "\n")
            boot_time_timestamp = psutil.boot_time()
            bt = datetime.fromtimestamp(boot_time_timestamp)
            print(
                fg(250, 200, 0) + "B" +
                fg(250, 190, 0) + "o" +
                fg(250, 180, 0) + "o" +
                fg(250, 170, 0) + "t " +
                fg(250, 160, 0) + "T" +
                fg(250, 150, 0) + "i" +
                fg(250, 140, 0) + "m" +
                fg(250, 130, 0) + "e" +
                fg(250, 120, 0) + ": " +
                fg(250, 105, 60) + f"{bt.day}.{bt.month}.{bt.year} {bt.hour}:{bt.minute}:{bt.second}" + fg.rs + "\n")

        @staticmethod
        def Sysinfo_CPU():
            print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "CPU Info", fg(250, 195, 60), "-" * 40, fg.rs + "\n")
            print(
                fg(250, 200, 0) + "A" +
                fg(250, 190, 0) + "c" +
                fg(250, 180, 0) + "t" +
                fg(250, 170, 0) + "u" +
                fg(250, 160, 0) + "a" +
                fg(250, 150, 0) + "l " +
                fg(250, 140, 0) + "C" +
                fg(250, 130, 0) + "o" +
                fg(250, 120, 0) + "r" +
                fg(250, 110, 0) + "e" +
                fg(250, 100, 0) + "s" +
                fg(250, 90, 0) + ":",
                fg(250, 105, 60) + str(psutil.cpu_count(logical=False)))
            print(
                fg(250, 200, 0) + "L" +
                fg(250, 190, 0) + "o" +
                fg(250, 180, 0) + "g" +
                fg(250, 170, 0) + "i" +
                fg(250, 160, 0) + "c" +
                fg(250, 150, 0) + "a" +
                fg(250, 140, 0) + "l " +
                fg(250, 130, 0) + "C" +
                fg(250, 120, 0) + "o" +
                fg(250, 110, 0) + "r" +
                fg(250, 100, 0) + "e" +
                fg(250, 90, 0) + "s" +
                fg(250, 80, 0) + ":",
                fg(250, 105, 60) + str(psutil.cpu_count(logical=True)))
            print(
                fg(250, 200, 0) + "M" +
                fg(250, 190, 0) + "a" +
                fg(250, 180, 0) + "x " +
                fg(250, 170, 0) + "F" +
                fg(250, 160, 0) + "r" +
                fg(250, 150, 0) + "e" +
                fg(250, 140, 0) + "q" +
                fg(250, 130, 0) + "u" +
                fg(250, 120, 0) + "e" +
                fg(250, 110, 0) + "n" +
                fg(250, 100, 0) + "c" +
                fg(250, 90, 0) + "y" +
                fg(250, 80, 0) + ": " +
                fg(250, 105, 60) + f"{psutil.cpu_freq().max:.1f}Mhz")
            print(
                fg(250, 200, 0) + "C" +
                fg(250, 190, 0) + "u" +
                fg(250, 180, 0) + "r" +
                fg(250, 170, 0) + "r" +
                fg(250, 160, 0) + "e" +
                fg(250, 150, 0) + "n" +
                fg(250, 140, 0) + "t " +
                fg(250, 130, 0) + "F" +
                fg(250, 120, 0) + "r" +
                fg(250, 110, 0) + "e" +
                fg(250, 100, 0) + "q" +
                fg(250, 90, 0) + "u" +
                fg(250, 80, 0) + "e" +
                fg(250, 70, 0) + "n" +
                fg(250, 60, 0) + "c" +
                fg(250, 50, 0) + "y" +
                fg(250, 40, 0) + ": " +
                fg(250, 105, 60) + f"{psutil.cpu_freq().current:.1f}Mhz")
            print(
                fg(250, 200, 0) + "C" +
                fg(250, 190, 0) + "P" +
                fg(250, 180, 0) + "U " +
                fg(250, 170, 0) + "U" +
                fg(250, 160, 0) + "s" +
                fg(250, 150, 0) + "a" +
                fg(250, 140, 0) + "g" +
                fg(250, 130, 0) + "e" +
                fg(250, 120, 0) + ": " +
                fg(250, 105, 60) + f"{psutil.cpu_percent()}%" + fg.rs + "\n")

            '''print("CPU Usage/Core:")
            for i, perc in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                print(f"Core {i}: {perc}%")'''

        @staticmethod
        def Sysinfo_ram():
            print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "RAM Info", fg(250, 195, 60), "-" * 40, fg.rs + "\n")
            virtual_mem = psutil.virtual_memory()
            print(
                fg(250, 200, 0) + "T" +
                fg(250, 190, 0) + "o" +
                fg(250, 180, 0) + "t" +
                fg(250, 170, 0) + "a" +
                fg(250, 160, 0) + "l" +
                fg(250, 150, 0) + ": " +
                fg(250, 105, 60) + f"{adjust_size(virtual_mem.total)}" + fg.rs)
            print(
                fg(250, 200, 0) + "A" +
                fg(250, 190, 0) + "v" +
                fg(250, 180, 0) + "a" +
                fg(250, 170, 0) + "i" +
                fg(250, 160, 0) + "l" +
                fg(250, 150, 0) + "a" +
                fg(250, 140, 0) + "b" +
                fg(250, 130, 0) + "l" +
                fg(250, 120, 0) + "e" +
                fg(250, 110, 0) + ": " +
                fg(250, 105, 60) + f"{adjust_size(virtual_mem.available)}" + fg.rs)
            print(
                fg(250, 200, 0) + "U" +
                fg(250, 190, 0) + "s" +
                fg(250, 180, 0) + "e" +
                fg(250, 170, 0) + "d" +
                fg(250, 160, 0) + ": " +
                fg(250, 105, 60) + f"{adjust_size(virtual_mem.used)}" + fg.rs)
            print(
                fg(250, 200, 0) + "P" +
                fg(250, 190, 0) + "e" +
                fg(250, 180, 0) + "r" +
                fg(250, 170, 0) + "c" +
                fg(250, 160, 0) + "e" +
                fg(250, 150, 0) + "n" +
                fg(250, 140, 0) + "t" +
                fg(250, 130, 0) + "a" +
                fg(250, 120, 0) + "g" +
                fg(250, 110, 0) + "e" +
                fg(250, 100, 0) + ": " +
                fg(250, 105, 60) + f"{virtual_mem.percent}%" + fg.rs + "\n")

        @staticmethod
        def Sysinfo_SWAP():
            print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "SWAP", fg(250, 195, 60), "-" * 40, fg.rs + "\n")
            swap = psutil.swap_memory()
            print(
                fg(250, 200, 0) + "T" +
                fg(250, 190, 0) + "o" +
                fg(250, 180, 0) + "t" +
                fg(250, 170, 0) + "a" +
                fg(250, 160, 0) + "l" +
                fg(250, 150, 0) + ": " +
                fg(250, 105, 60) + f"{adjust_size(swap.total)}" + fg.rs)
            print(
                fg(250, 200, 0) + "F" +
                fg(250, 190, 0) + "r" +
                fg(250, 180, 0) + "e" +
                fg(250, 170, 0) + "e" +
                fg(250, 160, 0) + ": " +
                fg(250, 105, 60) + f"{adjust_size(swap.free)}" + fg.rs)
            print(
                fg(250, 200, 0) + "U" +
                fg(250, 190, 0) + "s" +
                fg(250, 180, 0) + "e" +
                fg(250, 170, 0) + "d" +
                fg(250, 160, 0) + ": " +
                fg(250, 105, 60) + f"{adjust_size(swap.used)}" + fg.rs)
            print(
                fg(250, 200, 0) + "P" +
                fg(250, 190, 0) + "e" +
                fg(250, 180, 0) + "r" +
                fg(250, 170, 0) + "c" +
                fg(250, 160, 0) + "e" +
                fg(250, 150, 0) + "n" +
                fg(250, 140, 0) + "t" +
                fg(250, 130, 0) + "a" +
                fg(250, 120, 0) + "g" +
                fg(250, 110, 0) + "e" +
                fg(250, 100, 0) + ": " +
                fg(250, 105, 60) + f"{swap.percent}%" + fg.rs + "\n")

        @staticmethod
        def Sysinfo_HDD():
            print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "Disk Information", fg(250, 195, 60), "-" * 40,
                  fg.rs + "\n")
            partitions = psutil.disk_partitions()
            for p in partitions:
                print(
                    fg(250, 200, 0) + "D" +
                    fg(250, 190, 0) + "e" +
                    fg(250, 180, 0) + "v" +
                    fg(250, 170, 0) + "i" +
                    fg(250, 160, 0) + "c" +
                    fg(250, 150, 0) + "e" +
                    fg(250, 140, 0) + ": " +
                    fg(250, 105, 60) + f"{p.device}")
                print(
                    fg(250, 200, 0) + "M" +
                    fg(250, 190, 0) + "o" +
                    fg(250, 180, 0) + "u" +
                    fg(250, 170, 0) + "n" +
                    fg(250, 160, 0) + "t" +
                    fg(250, 150, 0) + "p" +
                    fg(250, 140, 0) + "o" +
                    fg(250, 130, 0) + "i" +
                    fg(250, 120, 0) + "n" +
                    fg(250, 110, 0) + "t" +
                    fg(250, 90, 0) + ": " +
                    fg(250, 105, 60) + f"{p.mountpoint}")
                print(
                    fg(250, 200, 0) + "F" +
                    fg(250, 190, 0) + "i" +
                    fg(250, 180, 0) + "l" +
                    fg(250, 170, 0) + "e " +
                    fg(250, 160, 0) + "s" +
                    fg(250, 150, 0) + "y" +
                    fg(250, 140, 0) + "s" +
                    fg(250, 130, 0) + "t" +
                    fg(250, 120, 0) + "e" +
                    fg(250, 110, 0) + "m " +
                    fg(250, 100, 0) + "t" +
                    fg(250, 90, 0) + "y" +
                    fg(250, 80, 0) + "p" +
                    fg(250, 70, 0) + "e" +
                    fg(250, 60, 0) + ": " +
                    fg(250, 105, 60) + f"{p.fstype}" + "\n")

                try:
                    partition_usage = psutil.disk_usage(p.mountpoint)
                except PermissionError:
                    continue

                print(
                    fg(250, 200, 0) + "  T" +
                    fg(230, 200, 0) + "o" +
                    fg(210, 200, 0) + "t" +
                    fg(190, 200, 0) + "a" +
                    fg(170, 200, 0) + "l " +
                    fg(150, 200, 0) + "S" +
                    fg(130, 200, 0) + "i" +
                    fg(110, 200, 0) + "z" +
                    fg(90, 200, 0) + "e" +
                    fg(70, 200, 0) + ": " +
                    fg(250, 105, 60) + f"{adjust_size(partition_usage.total)}")
                print(
                    fg(250, 200, 0) + "  U" +
                    fg(230, 200, 0) + "s" +
                    fg(210, 200, 0) + "e" +
                    fg(190, 200, 0) + "d" +
                    fg(170, 200, 0) + ": " +
                    fg(250, 105, 60) + f"{adjust_size(partition_usage.used)}")
                print(
                    fg(250, 200, 0) + "  F" +
                    fg(230, 200, 0) + "r" +
                    fg(210, 200, 0) + "e" +
                    fg(190, 200, 0) + "e" +
                    fg(170, 200, 0) + ": " +
                    fg(250, 105, 60) + f"{adjust_size(partition_usage.free)}")
                print(
                    fg(250, 200, 0) + "  P" +
                    fg(230, 200, 0) + "e" +
                    fg(210, 200, 0) + "r" +
                    fg(190, 200, 0) + "c" +
                    fg(170, 200, 0) + "e" +
                    fg(150, 200, 0) + "n" +
                    fg(130, 200, 0) + "t" +
                    fg(110, 200, 0) + "a" +
                    fg(90, 200, 0) + "g" +
                    fg(70, 200, 0) + "e" +
                    fg(50, 200, 0) + ": " +
                    fg(250, 105, 60) + f"{partition_usage.percent}%" + "\n")

            disk_io = psutil.disk_io_counters()
            print(
                fg(250, 200, 160) + "R" +
                fg(250, 190, 150) + "e" +
                fg(250, 180, 140) + "a" +
                fg(250, 170, 130) + "d " +
                fg(250, 160, 120) + "s" +
                fg(250, 150, 110) + "i" +
                fg(250, 140, 100) + "n" +
                fg(250, 130, 90) + "c" +
                fg(250, 120, 80) + "e " +
                fg(250, 110, 70) + "b" +
                fg(250, 100, 60) + "o" +
                fg(250, 90, 50) + "o" +
                fg(250, 80, 40) + "t" +
                fg(250, 70, 30) + ": " +
                fg(250, 105, 60) + f"{adjust_size(disk_io.read_bytes)}")
            print(
                fg(250, 200, 160) + "W" +
                fg(250, 190, 150) + "r" +
                fg(250, 180, 140) + "i" +
                fg(250, 170, 130) + "t" +
                fg(250, 160, 120) + "t" +
                fg(250, 150, 110) + "e" +
                fg(250, 140, 100) + "n " +
                fg(250, 130, 90) + "s" +
                fg(250, 120, 80) + "i" +
                fg(250, 110, 70) + "n" +
                fg(250, 100, 60) + "c" +
                fg(250, 90, 50) + "e " +
                fg(250, 80, 40) + "b" +
                fg(250, 70, 30) + "o" +
                fg(250, 60, 20) + "o" +
                fg(250, 50, 10) + "t" +
                fg(250, 40, 0) + ": " +
                fg(250, 105, 60) + f"{adjust_size(disk_io.write_bytes)}")

        @staticmethod
        def Sysinfo_GPU():
            print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "GPU Details", fg(250, 195, 60), "-" * 40, fg.rs + "\n")

            gpus = GPUtil.getGPUs()
            for gpu in gpus:
                print(
                    fg(200, 255, 0) + "I" +
                    fg(190, 255, 0) + "D" +
                    fg(180, 255, 0) + ": " +
                    fg(250, 105, 60) + f"{gpu.id}",
                    fg(200, 255, 0) + "N" +
                    fg(190, 255, 0) + "a" +
                    fg(180, 255, 0) + "m" +
                    fg(170, 255, 0) + "e" +
                    fg(160, 255, 0) + ": " +
                    fg(250, 105, 60) + f"{gpu.name}")
                print(
                    fg(200, 200, 0) + "\tL" +
                    fg(190, 200, 0) + "o" +
                    fg(180, 200, 0) + "a" +
                    fg(170, 200, 0) + "d" +
                    fg(160, 200, 0) + ": " +
                    fg(189, 252, 201) + f"{gpu.load * 100}" + fg(250, 105, 60) + " %")
                print(
                    fg(200, 200, 0) + "\tF" +
                    fg(190, 200, 0) + "r" +
                    fg(180, 200, 0) + "e" +
                    fg(170, 200, 0) + "e " +
                    fg(160, 200, 0) + "M" +
                    fg(150, 200, 0) + "e" +
                    fg(140, 200, 0) + "m" +
                    fg(130, 200, 0) + ": " +
                    fg(189, 252, 201) + f"{gpu.memoryFree}" + fg(250, 105, 60) + " MB")
                print(
                    fg(200, 200, 0) + "\tU" +
                    fg(190, 200, 0) + "s" +
                    fg(180, 200, 0) + "e" +
                    fg(170, 200, 0) + "d " +
                    fg(160, 200, 0) + "M" +
                    fg(150, 200, 0) + "e" +
                    fg(140, 200, 0) + "m" +
                    fg(130, 200, 0) + ": " +
                    fg(189, 252, 201) + f"{gpu.memoryUsed}" + fg(250, 105, 60) + " MB")
                print(
                    fg(200, 200, 0) + "\tT" +
                    fg(190, 200, 0) + "o" +
                    fg(180, 200, 0) + "t" +
                    fg(170, 200, 0) + "a" +
                    fg(160, 200, 0) + "l " +
                    fg(150, 200, 0) + "M" +
                    fg(140, 200, 0) + "e" +
                    fg(130, 200, 0) + "m" +
                    fg(120, 200, 0) + ": " +
                    fg(189, 252, 201) + f"{gpu.memoryTotal}" + fg(250, 105, 60) + " MB")
                print(
                    fg(200, 200, 0) + "\tT" +
                    fg(190, 200, 0) + "e" +
                    fg(180, 200, 0) + "m" +
                    fg(170, 200, 0) + "p" +
                    fg(160, 200, 0) + "e" +
                    fg(150, 200, 0) + "r" +
                    fg(140, 200, 0) + "a" +
                    fg(130, 200, 0) + "t" +
                    fg(120, 200, 0) + "u" +
                    fg(110, 200, 0) + "r" +
                    fg(100, 200, 0) + "e" +
                    fg(90, 200, 0) + ": " +
                    fg(189, 252, 201) + f"{gpu.temperature}" + fg(250, 105, 60) + "°C" + fg.rs + "\n")

        @staticmethod
        def Sysinfo_Network():
            print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "Network Information", fg(250, 195, 60), "-" * 40,
                  fg.rs + "\n" + fg.rs)
            if_addrs = psutil.net_if_addrs()
            for interface_name, interface_addresses in if_addrs.items():
                for address in interface_addresses:
                    print(
                        fg(250, 200, 0) + "I" +
                        fg(250, 190, 0) + "n" +
                        fg(250, 180, 0) + "t" +
                        fg(250, 170, 0) + "e" +
                        fg(250, 160, 0) + "r" +
                        fg(250, 150, 0) + "f" +
                        fg(250, 140, 0) + "a" +
                        fg(250, 130, 0) + "c" +
                        fg(250, 120, 0) + "e" +
                        fg(250, 110, 0) + ": " +
                        fg(250, 105, 60) + f"{interface_name}" + fg.rs)

                    if str(address.family) == 'AddressFamily.AF_INET':

                        print(
                            fg(250, 200, 0) + "  I" +
                            fg(250, 190, 0) + "P " +
                            fg(250, 180, 0) + "A" +
                            fg(250, 170, 0) + "d" +
                            fg(250, 160, 0) + "d" +
                            fg(250, 150, 0) + "r" +
                            fg(250, 140, 0) + "e" +
                            fg(250, 130, 0) + "s" +
                            fg(250, 120, 0) + "s" +
                            fg(250, 110, 0) + ": " +
                            fg(0, 255, 154) + f"{address.address}" + fg.rs)
                        print(
                            fg(250, 200, 0) + "  N" +
                            fg(250, 190, 0) + "e" +
                            fg(250, 180, 0) + "t" +
                            fg(250, 170, 0) + "m" +
                            fg(250, 160, 0) + "a" +
                            fg(250, 150, 0) + "s" +
                            fg(250, 140, 0) + "k" +
                            fg(250, 130, 0) + ": " +
                            fg(0, 255, 154) + f"{address.netmask}" + fg.rs)
                        print(
                            fg(250, 200, 0) + "  B" +
                            fg(250, 190, 0) + "r" +
                            fg(250, 180, 0) + "o" +
                            fg(250, 170, 0) + "a" +
                            fg(250, 160, 0) + "d" +
                            fg(250, 150, 0) + "c" +
                            fg(250, 140, 0) + "a" +
                            fg(250, 130, 0) + "s" +
                            fg(250, 120, 0) + "t " +
                            fg(250, 110, 0) + "I" +
                            fg(250, 100, 0) + "P" +
                            fg(250, 90, 0) + ": " +
                            fg(0, 255, 154) + f"{address.broadcast}" + fg.rs)

                    elif str(address.family) == 'AddressFamily.AF_PACKET':
                        print(
                            fg(250, 200, 0) + "  M" +
                            fg(250, 190, 0) + "A" +
                            fg(250, 180, 0) + "C " +
                            fg(250, 170, 0) + "A" +
                            fg(250, 160, 0) + "d" +
                            fg(250, 150, 0) + "d" +
                            fg(250, 140, 0) + "r" +
                            fg(250, 130, 0) + "e" +
                            fg(250, 120, 0) + "s" +
                            fg(250, 110, 0) + "s" +
                            fg(250, 100, 0) + ": " +
                            fg(0, 255, 154) + f"{address.address}" + fg.rs)
                        print(
                            fg(250, 200, 0) + "  N" +
                            fg(250, 190, 0) + "e" +
                            fg(250, 180, 0) + "t" +
                            fg(250, 170, 0) + "m" +
                            fg(250, 160, 0) + "a" +
                            fg(250, 150, 0) + "s" +
                            fg(250, 170, 0) + "k" +
                            fg(250, 160, 0) + ": " +
                            fg(0, 255, 154) + f"{address.netmask}" + fg.rs)
                        print(
                            fg(250, 200, 0) + "  B" +
                            fg(250, 190, 0) + "r" +
                            fg(250, 180, 0) + "o" +
                            fg(250, 170, 0) + "a" +
                            fg(250, 160, 0) + "d" +
                            fg(250, 150, 0) + "c" +
                            fg(250, 140, 0) + "a" +
                            fg(250, 130, 0) + "s" +
                            fg(250, 120, 0) + "t " +
                            fg(250, 110, 0) + "M" +
                            fg(250, 100, 0) + "A" +
                            fg(250, 90, 0) + "C" +
                            fg(250, 80, 0) + ": " +
                            fg(0, 255, 154) + f"{address.broadcast}" + fg.rs)
            print(fg.rs + "\n")
            net_io = psutil.net_io_counters()

            print(
                fg(0, 255, 255) + "T" +
                fg(0, 245, 245) + "o" +
                fg(0, 235, 235) + "t" +
                fg(0, 225, 225) + "a" +
                fg(0, 215, 215) + "l " +
                fg(0, 205, 205) + "B" +
                fg(0, 195, 195) + "y" +
                fg(0, 185, 185) + "t" +
                fg(0, 175, 175) + "e" +
                fg(0, 165, 165) + "s " +
                fg(0, 155, 155) + "S" +
                fg(0, 145, 145) + "e" +
                fg(0, 135, 135) + "n" +
                fg(0, 125, 125) + "t" +
                fg(0, 115, 115) + ": " +
                fg(0, 255, 154) + f"{adjust_size(net_io.bytes_sent)}" + fg.rs)
            print(
                fg(0, 255, 255) + "T" +
                fg(0, 245, 245) + "o" +
                fg(0, 235, 235) + "t" +
                fg(0, 225, 225) + "a" +
                fg(0, 215, 215) + "l " +
                fg(0, 205, 205) + "B" +
                fg(0, 195, 195) + "y" +
                fg(0, 185, 185) + "t" +
                fg(0, 175, 175) + "e" +
                fg(0, 165, 165) + "s " +
                fg(0, 155, 155) + "R" +
                fg(0, 145, 145) + "e" +
                fg(0, 135, 135) + "c" +
                fg(0, 125, 125) + "e" +
                fg(0, 115, 115) + "i" +
                fg(0, 105, 105) + "v" +
                fg(0, 95, 95) + "e" +
                fg(0, 85, 85) + "d" +
                fg(0, 75, 75) + ": " +
                fg(0, 255, 154) + f"{adjust_size(net_io.bytes_recv)}" + fg.rs)

    class speedtest_v2:
        @staticmethod
        def speedtest_v2_run():
            print(
                fg(160, 70, 170) + "L" +
                fg(165, 70, 165) + "o" +
                fg(170, 70, 160) + "a" +
                fg(175, 70, 155) + "d" +
                fg(180, 70, 150) + "i" +
                fg(185, 70, 145) + "n" +
                fg(190, 70, 140) + "g " +
                fg(195, 70, 135) + "s" +
                fg(200, 70, 130) + "e" +
                fg(205, 70, 125) + "r" +
                fg(210, 70, 120) + "v" +
                fg(215, 70, 115) + "e" +
                fg(220, 70, 110) + "r " +
                fg(225, 70, 105) + "l" +
                fg(230, 70, 100) + "i" +
                fg(235, 70, 95) + "s" +
                fg(240, 70, 90) + "t" +
                fg(245, 70, 85) + "." +
                fg(250, 70, 80) + "." +
                fg(255, 70, 75) + "." + fg.rs)
            test.get_servers()

            print(
                fg(155, 70, 170) + "C" +
                fg(160, 70, 165) + "h" +
                fg(165, 70, 160) + "o" +
                fg(170, 70, 155) + "o" +
                fg(175, 70, 150) + "s" +
                fg(180, 70, 145) + "i" +
                fg(185, 70, 140) + "n" +
                fg(190, 70, 135) + "g " +
                fg(195, 70, 130) + "b" +
                fg(200, 70, 125) + "e" +
                fg(205, 70, 120) + "s" +
                fg(210, 70, 115) + "t " +
                fg(215, 70, 110) + "s" +
                fg(220, 70, 105) + "e" +
                fg(225, 70, 100) + "r" +
                fg(230, 70, 95) + "v" +
                fg(235, 70, 90) + "e" +
                fg(240, 70, 85) + "r" +
                fg(245, 70, 80) + "." +
                fg(250, 70, 75) + "." +
                fg(255, 70, 70) + "." + fg.rs)
            best = test.get_best_server()

            print(
                fg(155, 70, 170) + "F" +
                fg(160, 70, 165) + "o" +
                fg(165, 70, 160) + "u" +
                fg(170, 70, 155) + "n" +
                fg(175, 70, 150) + "d" +
                fg(180, 70, 145) + ": " +
                fg(255, 255, 255) + f"{best['host']} " +
                fg(185, 70, 135) + "l" +
                fg(190, 70, 130) + "o" +
                fg(195, 70, 125) + "c" +
                fg(200, 70, 120) + "a" +
                fg(205, 70, 115) + "t" +
                fg(210, 70, 110) + "e" +
                fg(215, 70, 105) + "d " +
                fg(220, 70, 100) + "i" +
                fg(225, 70, 95) + "n " +
                fg(255, 255, 255) + f"{best['country']}" + fg.rs)

            print(
                fg(155, 70, 170) + "P" +
                fg(160, 70, 165) + "i" +
                fg(165, 70, 160) + "n" +
                fg(170, 70, 155) + "g " +
                fg(175, 70, 150) + "t" +
                fg(180, 70, 145) + "e" +
                fg(185, 70, 140) + "s" +
                fg(190, 70, 135) + "t" +
                fg(195, 70, 130) + "." +
                fg(200, 70, 125) + "." +
                fg(205, 70, 120) + "." + fg.rs)
            ping_result = test.results.ping
            print(
                fg(255, 255, 204) + "Ping: " + fg(255, 255, 255) + f"{ping_result}" + fg(255, 10, 150) + " ms" + fg.rs)

            print(
                fg(155, 70, 170) + "P" +
                fg(160, 70, 165) + "e" +
                fg(165, 70, 160) + "r" +
                fg(170, 70, 155) + "f" +
                fg(175, 70, 150) + "o" +
                fg(180, 70, 145) + "r" +
                fg(185, 70, 140) + "m" +
                fg(190, 70, 135) + "i" +
                fg(195, 70, 130) + "n" +
                fg(200, 70, 125) + "g " +
                fg(205, 70, 120) + "d" +
                fg(210, 70, 115) + "o" +
                fg(215, 70, 110) + "w" +
                fg(220, 70, 105) + "n" +
                fg(225, 70, 100) + "l" +
                fg(230, 70, 95) + "o" +
                fg(235, 70, 90) + "a" +
                fg(240, 70, 85) + "d " +
                fg(245, 70, 80) + "t" +
                fg(250, 70, 75) + "e" +
                fg(255, 70, 70) + "s" +
                fg(255, 70, 65) + "t" +
                fg(255, 70, 60) + "." +
                fg(255, 70, 55) + "." +
                fg(255, 70, 50) + "." + fg.rs)
            download_result = test.download()
            print(fg(255, 255, 204) + "Download speed: " + fg(255, 255, 255) +
                  f"{download_result / 1024 / 1024:.2f}" + fg(255, 10, 150) + " Mbit/s" + fg.rs)

            print(
                fg(155, 70, 170) + "P" +
                fg(160, 70, 165) + "e" +
                fg(165, 70, 160) + "r" +
                fg(170, 70, 155) + "f" +
                fg(175, 70, 150) + "o" +
                fg(180, 70, 145) + "r" +
                fg(185, 70, 140) + "m" +
                fg(190, 70, 135) + "i" +
                fg(195, 70, 130) + "n" +
                fg(200, 70, 125) + "g " +
                fg(205, 70, 120) + "u" +
                fg(210, 70, 115) + "p" +
                fg(215, 70, 110) + "l" +
                fg(220, 70, 105) + "o" +
                fg(225, 70, 100) + "a" +
                fg(230, 70, 95) + "d " +
                fg(235, 70, 90) + "t" +
                fg(240, 70, 85) + "e" +
                fg(245, 70, 80) + "s" +
                fg(250, 70, 75) + "t" +
                fg(255, 70, 70) + "." +
                fg(255, 70, 65) + "." +
                fg(255, 70, 60) + "." + fg.rs)
            upload_result = test.upload()
            print(fg(255, 255, 204) + "Upload speed: " + fg(255, 255, 255) + f"{upload_result / 1024 / 1024:.2f}" + fg(
                255, 10, 150) + " Mbit/s" + fg.rs)

    class process_v2:
        @staticmethod
        def main():
            print('*** Create a list of all running processes ***')

            listOfProcessNames = list()
            for proc in psutil.process_iter():
                pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
                listOfProcessNames.append(pInfoDict)
            for elem in listOfProcessNames:
                print(elem)

            print('*** Top 10 process with highest memory usage ***')
            listOfRunningProcess = getListOfProcessSortedByMemory()
            for elem in listOfRunningProcess[:10]:
                print(elem)


# ****************************************************************************
# MAIN SCRIPT
# ****************************************************************************

class menu:
    @staticmethod
    def menulista():
        while True:
            menu_list_def.menu_def.clear()
            logos.main_logo()
            verch.ver_ch_start()
            menu_list_def.menu_def.menu_A()
            menu_list_def.menu_def.exits_text()

            system_a = int(input("" + lang.language.langs["main"][6]))

            if system_a == 0:
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.menu_def.menu_listaA()
                    menu_list_def.menu_def.back_text()

                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        modul.System.systems()
                    if system_lista == 1:
                        modul.Devices.devices()
                    if system_lista == 2:
                        modul.Phone.phone()
                    if system_lista == 3:
                        modul.Network_Internet.networks()
                    if system_lista == 4:
                        modul.Personalization.personalization()
                    if system_lista == 5:
                        modul.Apps.apps()
                    if system_lista == 6:
                        modul.Accounts.accounts()
                    if system_lista == 7:
                        modul.Time_Language.time_language()
                    if system_lista == 8:
                        modul.Gaming.gaming()
                    if system_lista == 9:
                        modul.Extras.Extra()
                    if system_lista == 10:
                        modul.Ease_of_Access.ease_of_Access()
                    if system_lista == 11:
                        modul.Search.search()
                    if system_lista == 12:
                        modul.Privacy.privacy()
                    if system_lista == 13:
                        modul.Update_Security.update()
                    if system_lista == 14:
                        modul.Mixed_reality.mixed_reality()
                    if system_lista == 15:
                        modul.Surface_Hub.surface_hub()
                    if system_lista == 16:
                        modul.Shell_Command.menu()
                    if system_lista == 17:
                        modul.GoodMod.good()

                    if system_lista == 20:
                        break

            if system_a == 1:
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()

                    menu_list_def.menu_def.menu_C()
                    menu_list_def.menu_def.back_text()

                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        modul.my_script.beta_my_script()

                    if system_lista == 20:
                        break

            if system_a == 2:
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()

                    menu_list_def.menu_def.menu_B()
                    menu_list_def.menu_def.back_text()

                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        modul.SteamDB_finder.steamdb_generate()
                    if system_lista == 1:
                        modul.SteamDB_finder.steamdb_finder_a()
                    if system_lista == 2:
                        modul.SteamDB_finder.steamdb_finder_b()
                    if system_lista == 3:
                        modul.SteamDB_finder.steam_run_game()

                    if system_lista == 4:
                        modul.SteamDB.game.CSGOServer_730()
                    if system_lista == 5:
                        modul.SteamDB.userinfo.my_userid_info()
                    if system_lista == 6:
                        modul.SteamDB.userinfo.userid_info()
                    if system_lista == 7:
                        modul.SteamDB.playerbans.bann_user()
                    if system_lista == 8:
                        modul.SteamDB.playersummaries.GetPlayerSummaries()
                    if system_lista == 9:
                        modul.SteamDB.playersummaries.GetPlayerSummaries_player()

                    if system_lista == 20:
                        break

            if system_a == 3:
                while True:
                    menu_list_def.menu_def.clear()
                    logos.BattleNet()
                    verch.ver_ch_start()
                    print("[ 0]: Diablo III - Account")
                    print("[ 1]; Diablo III - Heroes")
                    print("[10]: Battlenet Access_Token")
                    menu_list_def.menu_def.back_text()
                    system_lista = int(input(" " + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        while True:
                            menu_list_def.menu_def.clear()
                            logos.BattleNet()
                            verch.ver_ch_start()
                            modul.BattleNET.D3()
                            menu_list_def.menu_def.back_text()
                            system_lista = int(input(" " + lang.language.langs["main"][6]))

                            if system_lista == 20:
                                break


                    if system_lista == 1:
                        while True:
                            menu_list_def.menu_def.clear()
                            logos.BattleNet()
                            verch.ver_ch_start()
                            modul.BattleNET.D3_hero()
                            menu_list_def.menu_def.back_text()
                            system_lista = int(input(" " + lang.language.langs["main"][6]))

                            if system_lista == 20:
                                break



                    if system_lista == 10:
                        while True:
                            menu_list_def.menu_def.clear()
                            logos.BattleNet()
                            verch.ver_ch_start()
                            modul.BattleNET.acess_token()
                            menu_list_def.menu_def.back_text()
                            system_lista = int(input(" " + lang.language.langs["main"][6]))

                            if system_lista == 20:
                                break

                    if system_lista == 20:
                        break

            if system_a == 4:
                while True:
                    menu_list_def.menu_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.systeminfo.systeminfo()
                    menu_list_def.menu_def.back_text()
                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        while True:
                            menu_list_def.menu_def.clear()
                            logos.main_logo()
                            verch.ver_ch_start()
                            menu_list_def.systeminfo.sysinfo()
                            menu_list_def.menu_def.back_text()
                            system_lista = int(input("" + lang.language.langs["main"][6]))

                            if system_lista == 0:
                                while True:
                                    menu_list_def.menu_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_win()
                                    menu_list_def.menu_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 1:
                                while True:
                                    menu_list_def.menu_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_boot()
                                    menu_list_def.menu_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 2:
                                while True:
                                    menu_list_def.menu_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_CPU()
                                    menu_list_def.menu_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 3:
                                while True:
                                    menu_list_def.menu_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_ram()
                                    menu_list_def.menu_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 4:
                                while True:
                                    menu_list_def.menu_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_SWAP()
                                    menu_list_def.menu_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 5:
                                while True:
                                    menu_list_def.menu_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_Network()
                                    menu_list_def.menu_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 6:
                                while True:
                                    menu_list_def.menu_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_GPU()
                                    menu_list_def.menu_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 7:
                                while True:
                                    menu_list_def.menu_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_HDD()
                                    menu_list_def.menu_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 8:
                                while True:
                                    menu_list_def.menu_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()
                                    modul.Sysinfo_all.Sysinfo_win()
                                    modul.Sysinfo_all.Sysinfo_CPU()
                                    modul.Sysinfo_all.Sysinfo_ram()
                                    modul.Sysinfo_all.Sysinfo_Network()
                                    modul.Sysinfo_all.Sysinfo_HDD()
                                    modul.Sysinfo_all.Sysinfo_GPU()
                                    modul.Sysinfo_all.Sysinfo_boot()
                                    menu_list_def.menu_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 20:
                                break

                    if system_lista == 1:
                        while True:
                            menu_list_def.menu_def.clear()
                            logos.main_logo()
                            verch.ver_ch_start()
                            modul.process_v2.main()
                            menu_list_def.menu_def.back_text()
                            system_lista = int(input("" + lang.language.langs["main"][6]))
                            if system_lista == 20:
                                break

                    if system_lista == 2:
                        while True:
                            menu_list_def.menu_def.clear()
                            logos.main_logo()
                            verch.ver_ch_start()
                            modul.speedtest_v2.speedtest_v2_run()
                            menu_list_def.menu_def.back_text()
                            system_lista = int(input("" + lang.language.langs["main"][6]))
                            if system_lista == 20:
                                break

                    if system_lista == 20:
                        break


# ----------------------------------------------------------------------------------------------------------------------
# NOT VISIBLE BETA POPUP MENÜ
# ----------------------------------------------------------------------------------------------------------------------

            if system_a == 5:
                while True:
                    print(datetime.datetime.now())

                    time.sleep(0.5)
                    print(fg(255, 80, 250) + "  _      ___         __                 __  _____  ____            " + fg.rs)
                    time.sleep(0.2)
                    print(fg(255, 80, 200) + " | | /| / (_)__  ___/ /__ _    _____   / / / / _ \/  _/ ___  __ __ " + fg.rs)
                    time.sleep(0.2)
                    print(fg(255, 80, 150) + " | |/ |/ / / _ \/ _  / _ \ |/|/ (_-<  / /_/ / , _// /  / _ \/ // / " + fg.rs)
                    time.sleep(0.2)
                    print(fg(255, 80, 100) + " |__/|__/_/_//_/\_,_/\___/__,__/___/  \____/_/|_/___/ / .__/\_, /  " + fg.rs)
                    time.sleep(0.2)
                    print(fg(20, 180, 90) + "                Create by LexyGuru" +
                      fg(255, 80, 50) + "                   /_/   /___/   " + fg.rs)
                    print("")

                    time.sleep(.5)

# ----------------------------------------------------------------------------------------------------------------------
# Token Access
# ----------------------------------------------------------------------------------------------------------------------

                    def process_thread():
                        global proc
                        config = ROOT_DIR + "\\config\\battenet.json"

                        json.load(codecs.open(config, 'r', 'utf-8-sig'))
                        with open(config, encoding='utf-8-sig') as f:
                            configs = json.load(f)

                        Client_ID = str(configs['Client_ID'][0])
                        Client_Sicret = str(configs['Client_Sicret'][0])

                        command = "curl -u " + Client_ID + ":" + Client_Sicret + \
                                  " -d grant_type=client_credentials https://oauth.battle.net/token"
                        save = command + " > c:\\temp\\battle_acess.json"
                        os.system("" + save)

                        config_save = "c:\\temp\\battle_acess.json"
                        json.load(codecs.open(config_save, 'r', 'utf-8-sig'))
                        with open(config_save, encoding='utf-8-sig') as f:
                            command = json.load(f)
                        keyword = "access_token: {access_token}".format(**command)

                        proc = keyword

                    def main():
                        thread = threading.Thread(target=process_thread, daemon=True)
                        thread.start()

                        while True:

                            sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, 'Loading list of packages',
                                              time_between_frames=100)
                            thread.join(timeout=.1)
                            if not thread.is_alive():
                                break
                        sg.popup_animated(None)

                        output = proc.__str__().replace('\\r\\n', '\n')
                        sg.popup_scrolled(output, font='Courier 10')


                    main()

                    menu_list_def.menu_def.back_text()

                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 20:
                        break

            if system_a == 6:
                while True:
                    import time
                    from datetime import timedelta

                    start = time.time()

                    code(fg(255, 80, 250) + "  _      ___         __                 __  _____  ____            " + fg.rs)
                    code(fg(255, 80, 200) + " | | /| / (_)__  ___/ /__ _    _____   / / / / _ \/  _/ ___  __ __ " + fg.rs)
                    code(fg(255, 80, 150) + " | |/ |/ / / _ \/ _  / _ \ |/|/ (_-<  / /_/ / , _// /  / _ \/ // / " + fg.rs)
                    code(fg(255, 80, 100) + " |__/|__/_/_//_/\_,_/\___/__,__/___/  \____/_/|_/___/ / .__/\_, /  " + fg.rs)
                    code(fg(20, 180, 90) + "                Create by LexyGuru" +
                          fg(255, 80, 50) + "                   /_/   /___/   " + fg.rs)

                    end = time.time()

                    elapsed_time = end - start

                    print("elapsed time: " + str(timedelta(seconds=elapsed_time)))

                    menu_list_def.menu_def.back_text()

                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 20:
                        break



            if system_a == 20:
                #os.remove("ver.json")
                exit()

menu.menulista()


