import requests
import os
from sty import fg
import json
import lang.language
import psutil
import platform
import GPUtil
from datetime import datetime
import subprocess
import speedtest
from subprocess import Popen, CREATE_NEW_CONSOLE

ROOT_DIR = os.path.abspath(os.curdir)
file_exists = os.path.exists('ver.json')

start = ROOT_DIR + "\winscript\godm.ps1"
ms_list = ROOT_DIR + "\winscript\ms_list.ps1"
win_install = ROOT_DIR + "\winscript\win_inst_list.ps1"
win_search = ROOT_DIR + "\winscript\win_sear_que_inst.ps1"
win_upgrade = ROOT_DIR + "\winscript\win_upg_all.ps1"
power_set = ROOT_DIR + "\winscript\power_set.ps1"

update_powershell = ROOT_DIR + "\winscript\windows_runas_update.ps1"
update_powershell_fixer = ROOT_DIR + "\winscript\windows_runas_update_fixer.ps1"

restart_vga_driver = ROOT_DIR + "\winscript\windows_runas_vga_driver_restart.ps1"
restart_vga_driver_start = ROOT_DIR + "\winscript\windows_runas_vga_restart_start.ps1"
restart_vga_id = "pnputil /restart-device "
vga_list = '"'

steam_fix = ROOT_DIR + "\winscript\steam_fix_service.ps1"

C_DIR_VGA_IN = "C:/TEMP/"
C_DIR_IN = "C:/TEMP/IMPORT.json"
C_DIR_EX = "C:/TEMP/EXPORT.json"

w_scan_updates = "Update-MpSignature"
w_scan_Quick = "Start-MpScan -ScanType QuickScan"
w_scan_Full = "Start-MpScan -ScanType FullScan"


def adjust_size(size):
    factor = 1024
    for i in ["B", "KiB", "MiB", "GiB", "TiB"]:
        if size > factor:
            size = size / factor
        else:
            return f"{size:.3f}{i}"


# ****************************************************************************
# logo
# ****************************************************************************
class logos:
    @staticmethod
    def main_logo():
        print(fg(255, 80, 250) + "  _      ___         __                 __  _____  ____            " + fg.rs)
        print(fg(255, 80, 200) + " | | /| / (_)__  ___/ /__ _    _____   / / / / _ \/  _/ ___  __ __ " + fg.rs)
        print(fg(255, 80, 150) + " | |/ |/ / / _ \/ _  / _ \ |/|/ (_-<  / /_/ / , _// /  / _ \/ // / " + fg.rs)
        print(fg(255, 80, 100) + " |__/|__/_/_//_/\_,_/\___/__,__/___/  \____/_/|_/___/ / .__/\_, /  " + fg.rs)
        print(fg(255, 80, 50) + "                Create by LexyGuru                   /_/   /___/   " + fg.rs)
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
        print(fg(255, 80, 250) + "   ___      __         ___             _         __  " + fg.rs)
        print(fg(255, 80, 200) + "  / _ )___ / /____ _  / _ \_______    (_)__ ____/ /_ " + fg.rs)
        print(fg(255, 80, 150) + " / _  / -_) __/ _ `/ / ___/ __/ _ \  / / -_) __/ __/ " + fg.rs)
        print(fg(255, 80, 100) + "/____/\__/\__/\_,_/ /_/  /_/  \___/_/ /\__/\__/\__/  " + fg.rs)
        print(fg(255, 80, 950) + "         Create by LexyGuru" + fg(255, 80, 50) + "      |___/               " + fg.rs)
        print("")

    @staticmethod
    def main_logo_v2():
        print(fg(255, 80, 250) + "  _      ___         __                 __  _____  ____            " + fg.rs)
        print(fg(255, 80, 200) + " | | /| / (_)__  ___/ /__ _    _____   / / / / _ \/  _/ ___  __ __ " + fg.rs)
        print(fg(255, 80, 150) + " | |/ |/ / / _ \/ _  / _ \ |/|/ (_-<  / /_/ / , _// /  / _ \/ // / " + fg.rs)
        print(fg(255, 80, 100) + " |__/|__/_/_//_/\_,_/\___/__,__/___/  \____/_/|_/___/ / .__/\_, /  " + fg.rs)
        print(fg(20, 180, 90) + "                Create by LexyGuru" + fg(255, 80,
                                                                          50) + "                   /_/   /___/   " + fg.rs)
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
        print(fg(255, 80, 250) + "   ______                 ___  ___    ___        _ " + fg.rs)
        print(fg(255, 80, 200) + "  / __/ /____ ___ ___ _  / _ \/ _ )  / _ | ___  (_)" + fg.rs)
        print(fg(255, 80, 150) + " _\ \/ __/ -_) _ `/  ' \/ // / _  | / __ |/ _ \/ / " + fg.rs)
        print(fg(255, 80, 100) + "/___/\__/\__/\_,_/_/_/_/____/____/ /_/ |_/ .__/_/  " + fg.rs)
        print(fg(20, 180, 90) + "            Create by LexyGuru" + fg(255, 80, 50) + "          /_/        " + fg.rs)
        print("")


# ****************************************************************************
# ver_ch
# ****************************************************************************
class verch:

    @staticmethod
    def ver_ch():
        url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/main/SVG_DIR/verzion.json'
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
        url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/beta/SVG_DIR/verzion.json'
        x = requests.get(url)
        beta_ver = x.json()['next_beta'][0]

        url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/beta/SVG_DIR/verzion.json'
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

        if file_exists == True:
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

        if file_exists == False:
            url = 'https://raw.githubusercontent.com/LexyGuru/Terminal_Windows_URI_PY/main/SVG_DIR/verzion.json'
            x = requests.get(url)
            current = x.json()

            json_object = json.dumps(current)

            with open("ver.json", "w") as outfile:
                outfile.write(json_object)


# ****************************************************************************
# language_def_list
# ****************************************************************************
class menu_list_def:

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
    def menu_listaA():
        lista = lang.language.langs['menu_list']
        i = 0
        for i in range(0, len(lista)):
            print(lista[i])

    @staticmethod
    def menu_A():
        lista = lang.language.langs['menu_a']
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

        @staticmethod
        def beta_project_lang_steamdb():
            lista = lang.language.langs['beta_project_steamdb']
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

    class verch:

        @staticmethod
        def verch_lang():
            lista = lang.language.langdb['verch_lang']
            i = 0
            for i in range(0, len(lista)):
                print(lista[i])


# ****************************************************************************
# modul
# ****************************************************************************
class modul:
    class SteamDB:
        pass

    class Accounts:
        @staticmethod
        def accounts():
            while True:
                menu_list_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.accounts_list.accounts_listA()
                menu_list_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    os.system("start ms-settings:yourinfo")
                if system_lista == 1:
                    os.system("start ms-settings:emailandaccounts")
                if system_lista == 2:
                    while True:
                        menu_list_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()

                        menu_list_def.accounts_list.menu_accounts_sigin_list('self')
                        menu_list_def.back_text()
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
                        menu_list_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()

                        menu_list_def.accounts_list.menu_accounts_family_list('self')
                        menu_list_def.back_text()
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
                menu_list_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.apps_list.apps_listA()
                menu_list_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    while True:
                        menu_list_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()

                        menu_list_def.apps_list.menu_apps_list('self')
                        menu_list_def.back_text()
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
                        menu_list_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()

                        menu_list_def.apps_list.menu_apps_ofline_maps_list('self')
                        menu_list_def.back_text()
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
                menu_list_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.devices_list.devices_listA()
                menu_list_def.back_text()

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
                        menu_list_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.devices_list.menu_devices_typing_list()
                        menu_list_def.back_text()
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
                menu_list_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.ease_of_access.eace_of_access_listA()
                menu_list_def.back_text()
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
                        menu_list_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.ease_of_access.ease_of_access_narrator_list('self')
                        menu_list_def.back_text()
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
                menu_list_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.extra_list.extra_listA()
                menu_list_def.extra_back_text()
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
                        menu_list_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.extra_list.menu_weather_list()
                        menu_list_def.back_text()
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
                menu_list_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.gaming_list.gaming_listA()
                menu_list_def.back_text()
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
                menu_list_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.goodm.goodmod_listA()
                menu_list_def.back_text()
                system_lista = int(input("" + lang.language.langs["main"][6]))

                if system_lista == 0:
                    result = subprocess.run([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe',
                                             r'' + start], stdout=subprocess.PIPE,
                                            stderr=subprocess.STDOUT, shell=True)
                    print(result)

                if system_lista == 1:
                    while True:
                        menu_list_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.goodm.power_listA('self')
                        menu_list_def.back_text()
                        system_lista = int(input("" + lang.language.langs["main"][6]))

                        if system_lista == 0:
                            os.system("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")

                        if system_lista == 1:
                            os.system("start powercfg.cpl")

                        if system_lista == 2:
                            menu_list_def.clear()
                            logos.main_logo()
                            verch.ver_ch_start()
                            menu_list_def.goodm.power_menu_listA('self')
                            menu_list_def.back_text()

                            Popen('powershell ' + power_set, creationflags=CREATE_NEW_CONSOLE)
                            system_lista = input("" + lang.language.langs["main"][9])
                            os.system("powercfg /setactive " + system_lista)

                            if system_lista == 20:
                                break

                        if system_lista == 20:
                            break

                if system_lista == 2:
                    while True:
                        menu_list_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.microsoft.microsoft_listA('self')
                        menu_list_def.back_text()
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
                                menu_list_def.clear()
                                logos.main_logo()
                                verch.ver_ch_start()
                                menu_list_def.microsoft.microsoft_install('self')
                                menu_list_def.back_text()

                                if system_lista == 0:
                                    Popen('powershell ' + win_search, creationflags=CREATE_NEW_CONSOLE)

                                if system_lista == 1:
                                    system_lista = input("" + lang.language.langs["main"][9])
                                    os.system("winget install " + system_lista)

                                if system_lista == 20:
                                    break

                        if system_lista == 6:
                            while True:
                                menu_list_def.clear()
                                logos.main_logo()
                                verch.ver_ch_start()
                                menu_list_def.microsoft.microsoft_uninstall('self')
                                menu_list_def.back_text()
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
                        menu_list_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.goodm.Update_Fixer('self')
                        menu_list_def.back_text()
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
                        menu_list_def.clear()
                        logos.main_logo()
                        verch.ver_ch_start()
                        menu_list_def.goodm.Windows_Defender('self')
                        menu_list_def.back_text()
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
                menu_list_def.clear()
                logos.main_logo()
                verch.ver_ch_start()
                menu_list_def.mixed_reality.mixed_reality_listA()
                menu_list_def.back_text()
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
        pass

    class Network_Internet:
        pass


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
        test = speedtest.Speedtest()
        def speedtest_v2_run(self):
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
            print(fg(255, 255, 204) + "Download speed: " + fg(255, 255,
                                                              255) + f"{download_result / 1024 / 1024:.2f}" + fg(255,
                                                                                                                 10,
                                                                                                                 150) + " Mbit/s" + fg.rs)
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

            pass


# ****************************************************************************
# MAIN SCRIPT
# ****************************************************************************

class menu:
    @staticmethod
    def menulista():
        while True:
            menu_list_def.clear()
            logos.main_logo()
            verch.ver_ch_start()
            menu_list_def.menu_A()
            menu_list_def.exits_text()

            system_a = int(input("" + lang.language.langs["main"][6]))

            if system_a == 0:
                while True:
                    menu_list_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()
                    menu_list_def.menu_listaA()
                    menu_list_def.back_text()

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
                        modul.Extras.extra()
                    if system_lista == 10:
                        modul.Ease_of_Access.ease_of_access()
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
                        modul.GoogMod.good()

                    if system_lista == 20:
                        break

            if system_a == 1:
                while True:
                    menu_list_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()

                    menu_list_def.menu_C()
                    menu_list_def.back_text()

                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        modul.my_script.beta_my_script()

                    if system_lista == 20:
                        break

            if system_a == 2:
                while True:
                    menu_list_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()

                    menu_list_def.menu_B()
                    menu_list_def.back_text()

                    system_lista = int(input("" + lang.language.langs["main"][6]))
                    if system_lista == 0:
                        modul.SteamDB.GetGameServersStatus.game.CSGOServers_730()
                    if system_lista == 1:
                        modul.SteamDB.GetOwnedGames.steamDB.my_userid_info()
                    if system_lista == 2:
                        modul.SteamDB.GetOwnedGames.steamDB.userid_info()
                    if system_lista == 3:
                        modul.SteamDB.GetPlayerBans.steamDB.bann_user()
                    if system_lista == 4:
                        modul.SteamDB.GetPlayerSummaries.GetPlayerSummaries()
                    if system_lista == 5:
                        modul.SteamDB.GetPlayerSummaries.GetPlayerSummaries_player()

                    if system_lista == 20:
                        break

            if system_a == 3:
                while True:
                    menu_list_def.clear()
                    logos.main_logo()
                    verch.ver_ch_start()

                    print(lang.language.langs["systeminfo"][0])
                    print(lang.language.langs["systeminfo"][1])
                    print(lang.language.langs["systeminfo"][2])
                    menu_list_def.back_text()
                    system_lista = int(input("" + lang.language.langs["main"][6]))

                    if system_lista == 0:
                        while True:
                            menu_list_def.clear()
                            logos.main_logo()
                            verch.ver_ch_start()

                            print("[ 0]: System WINDOWS")
                            print("[ 1]: System BOOT")
                            print("[ 2]: System CPU")
                            print("[ 3]: System RAM")
                            print("[ 4]: System SWAP")
                            print("[ 5]: System NETWORK")
                            print("[ 6]: System GPU")
                            print("[ 7]: System HDD")
                            print("[ 8]: All")
                            menu_list_def.back_text()
                            system_lista = int(input("" + lang.language.langs["main"][6]))

                            if system_lista == 0:
                                while True:
                                    menu_list_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_win()
                                    menu_list_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 1:
                                while True:
                                    menu_list_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_boot()
                                    menu_list_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 2:
                                while True:
                                    menu_list_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_CPU()
                                    menu_list_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 3:
                                while True:
                                    menu_list_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_ram()
                                    menu_list_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 4:
                                while True:
                                    menu_list_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_SWAP()
                                    menu_list_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 5:
                                while True:
                                    menu_list_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_Network()
                                    menu_list_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 6:
                                while True:
                                    menu_list_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_GPU()
                                    menu_list_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 7:
                                while True:
                                    menu_list_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()

                                    modul.Sysinfo_all.Sysinfo_HDD()
                                    menu_list_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 8:
                                while True:
                                    menu_list_def.clear()
                                    logos.main_logo()
                                    verch.ver_ch_start()
                                    modul.Sysinfo_all.Sysinfo_win()
                                    modul.Sysinfo_all.Sysinfo_CPU()
                                    modul.Sysinfo_all.Sysinfo_ram()
                                    modul.Sysinfo_all.Sysinfo_Network()
                                    modul.Sysinfo_all.Sysinfo_HDD()
                                    modul.Sysinfo_all.Sysinfo_GPU()
                                    modul.Sysinfo_all.Sysinfo_boot()
                                    menu_list_def.back_text()
                                    system_lista = int(input("" + lang.language.langs["main"][6]))
                                    if system_lista == 20:
                                        break

                            if system_lista == 20:
                                break

                    if system_lista == 1:
                        while True:
                            menu_list_def.clear()
                            logos.main_logo()
                            verch.ver_ch_start()

                            modul.process_v2.main()
                            menu_list_def.back_text()
                            system_lista = int(input("" + lang.language.langs["main"][6]))
                            if system_lista == 20:
                                break

                    if system_lista == 2:
                        while True:
                            menu_list_def.clear()
                            logos.main_logo()
                            verch.ver_ch_start()

                            modul.speedtest_v2.speedtest_v2_run()
                            menu_list_def.back_text()
                            system_lista = int(input("" + lang.language.langs["main"][6]))
                            if system_lista == 20:
                                break
                    
                    if system_lista == 20:
                        break

            if system_a == 20:
                # os.remove("ver.json")
                exit()


menu.menulista()
