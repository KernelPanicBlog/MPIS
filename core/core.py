#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv


class Mpis:
    def __init__(self):
        self.main_menu = []
        self.menu_multimedia = []
        self.menu_Ofimatic = []
        self.menu_update_system = []
        self.menu_install_app = []
        self.menu_development = []
        self.menu_Internet = []
        self.menu_Games = []
        self.menu_Sys_Tools = []
        self.menu_DEs_WMs = []
        self.menu_DEs = []
        self.menu_WMs = []
        self.apps_update_system = []
        self.apps_ofimatic = []
        self.apps_multimedia = []
        self.apps_development = []
        self.apps_internet = []
        self.apps_Games = []
        self.apps_DEs = []
        self.apps_WMs = []
        self.apps_System_Tools = []
        self.__load_menus()
        self.__load_apps()
        self.msgMpis = "\t\033[1;32mOption > \033[1;m"
        self.msgTFWE = "Task finished with errors. Press Enter to continue..."
        self.msgTF = "Task finished. Press Enter to continue..."
        self.msgAur = "This application will be installed from the AUR " \
                      "repository (community). It will be installed at " \
                      "your own risk."
        self.msgNf = "(not functional, yet)"

    def __load_menus(self):
        file_name = "menus.config"
        file_path = "/usr/lib/mpis/" + file_name
        menu_file = file_name if os.path.isfile(file_name) else file_path
        with open(menu_file) as f:
            uncode = csv.reader(f)
            data = list(uncode)
        for i in data:
            if i[0] == "Office":
                self.menu_Ofimatic.append([i[1], i[2]])
            elif i[0] == "Multimedia":
                self.menu_multimedia.append([i[1], i[2]])
            elif i[0] == "main_menu":
                self.main_menu.append([i[1], i[2]])
            elif i[0] == "menu_update_system":
                self.menu_update_system.append([i[1], i[2]])
            elif i[0] == "menu_install_app":
                self.menu_install_app.append([i[1], i[2]])
            elif i[0] == "Development":
                self.menu_development.append([i[1], i[2]])
            elif i[0] == "Internet":
                self.menu_Internet.append([i[1], i[2]])
            elif i[0] == "Games":
                self.menu_Games.append([i[1], i[2]])
            elif i[0] == "Sys_Tools":
                self.menu_Sys_Tools.append([i[1], i[2]])
            elif i[0] == "DEs_WMs":
                self.menu_DEs_WMs.append([i[1], i[2]])
            elif i[0] == "DEs":
                self.menu_DEs.append([i[1], i[2]])
            elif i[0] == "WMs":
                self.menu_WMs.append([i[1], i[2]])

    def __load_apps(self):
        file_name = "apps.config"
        file_path = "/usr/lib/mpis/" + file_name
        apps_file = file_name if os.path.isfile(file_name) else file_path
        with open(apps_file) as f:
            uncode = csv.reader(f)
            data = list(uncode)
            for i in data:
                if i[0] == "update_system":
                    if len(i) > 3:
                        aux = []
                        for a in range(2, len(i)):
                            aux.append(i[a])
                        self.apps_update_system.append([i[1], aux])
                    else:
                        aux = [i[2]]
                        self.apps_update_system.append([i[1], aux])
                elif i[0] == "Ofimatic":
                    if len(i) > 3:
                        aux = []
                        for a in range(2, len(i)):
                            aux.append(i[a])
                        self.apps_ofimatic.append([i[1], aux])
                    else:
                        aux = [i[2]]
                        self.apps_ofimatic.append([i[1], aux])
                elif i[0] == "Multimedia":
                    if len(i) > 3:
                        aux = []
                        for a in range(2, len(i)):
                            aux.append(i[a])
                        self.apps_multimedia.append([i[1], aux])
                    else:
                        aux = [i[2]]
                        self.apps_multimedia.append([i[1], aux])
                elif i[0] == "Development":
                    if len(i) > 3:
                        aux = []
                        for a in range(2, len(i)):
                            aux.append(i[a])
                        self.apps_development.append([i[1], aux])
                    else:
                        aux = [i[2]]
                        self.apps_development.append([i[1], aux])
                elif i[0] == "Internet":
                    if len(i) > 3:
                        aux = []
                        for a in range(2, len(i)):
                            aux.append(i[a])
                        self.apps_internet.append([i[1], aux])
                    else:
                        aux = [i[2]]
                        self.apps_internet.append([i[1], aux])
                elif i[0] == "Games":
                    if len(i) > 3:
                        aux = []
                        for a in range(2, len(i)):
                            aux.append(i[a])
                        self.apps_Games.append([i[1], aux])
                    else:
                        aux = [i[2]]
                        self.apps_Games.append([i[1], aux])
                elif i[0] == "DEs":
                    if len(i) > 3:
                        aux = []
                        for a in range(2, len(i)):
                            aux.append(i[a])
                        self.apps_DEs.append([i[1], aux])
                    else:
                        aux = [i[2]]
                        self.apps_DEs.append([i[1], aux])
                elif i[0] == "WMs":
                    if len(i) > 3:
                        aux = []
                        for a in range(2, len(i)):
                            aux.append(i[a])
                        self.apps_WMs.append([i[1], aux])
                    else:
                        aux = [i[2]]
                        self.apps_WMs.append([i[1], aux])
                elif i[0] == "System Tools":
                    if len(i) > 3:
                        aux = []
                        for a in range(2, len(i)):
                            aux.append(i[a])
                        self.apps_System_Tools.append([i[1], aux])
                    else:
                        aux = [i[2]]
                        self.apps_System_Tools.append([i[1], aux])

    def reload(self):
        self.__load_apps()
        self.__load_menus()

    def execute_command(self, command, option=False):
        flat = True
        for cmd in command:
            if cmd.startswith("yaourt"):
                print(self.msgAur)
            if flat and option:
                if os.system(cmd) == 0:
                    flat = True
                else:
                    flat = False
                    break
            elif flat or not option:
                if os.system(cmd) == 0:
                    flat = True
                else:
                    flat = False
        if flat:
            self.pause(self.msgTF)
        else:
            self.pause(self.msgTFWE)

    def user_input(self):
        try:
            return int(input(self.msgMpis))
        except ValueError:
            return 0

    @staticmethod
    def pause(msg="Press any key to continue..."):
        try:
            a = str(input(msg))
        except SyntaxError:
            pass

    @staticmethod
    def clear():
        os.system("clear")

    @staticmethod
    def end_message():
        print("""\033[1;36m
\tThanks for choosing us, we hope this script helped you.
\t\t- The KernelPanicBlog Team.
\tOur web: https://kernelpanicblog.wordpress.com\033[1;m
""")

    @staticmethod
    def banner():

        print("""\033[1;36m
   _  __                    _  _____                    ____  _
  | |/ /                   | ||  __ \          (¨)     |  _ \| |
  | ' / ___ _ __ _ __   ___| || |__) |_ _ _ __  _  ___ | |_) | | ___   __ _
  |  < / _ \ '__| '_ \ / _ \ ||  ___/ _` | '_ \| |/ __||  _ <| |/ _ \ / _` |
  | . \  __/ |  | | | |  __/ || |  | (_| | | | | | (__ | |_) | | (_) | (_| |
  |_|\_\___|_|  |_| |_|\___|_||_|   \__,_|_| |_|_|\___||____/|_|\___/ \__, |
                                                                       __/ |
                                                                      |___/\033[1;m
\t\033[1;36mManjaro Post Installation Script version 0.1a\033[1;m
\t\033[1;32mAuthors:\033[1;m
\t\t\033[1;32mSniferL4bs  | https://www.sniferl4bs.com\033[1;m
\t\t\033[1;32mNeoRanger   | https://www.neositelinux.com.ar\033[1;m
\t\t\033[1;32mHarrinsoft  |                         \033[1;m
\t\033[1;32mCollaborative Blog: | https://kernelpanicblog.wordpress.com\033[1;m

\tScript in testing phase, please report bugs :)
""")

    @staticmethod
    def help():
        print("""\n\033[1;36mHelp:\033[1;m\n
\tYou can select an option with the given
\tnumber or write 2 shortcuts:
\t- back -> return to the previous option
\t- exit or Ctrl+C -> finish the script execution
""")
