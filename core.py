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
        self.msgMpis = "\033[1;36mMPIS > \033[1;m"
        self.msgTFWE = "Task Finished with errors. press enter to continue"
        self.msgTF = "Task Finished. Press Enter to continue"
        self.msgAur = "This application is on the AUR repository " \
                      "(community). It will be install at your own risk."
        self.msgNf = "(not functional yet)"

    def __load_menus(self):
        with open("menus.config") as f:
            uncode = csv.reader(f)
            data = list(uncode)
        for i in data:
            if i[0] == "Ofimatic":
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
        with open("apps.config") as f:
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
    def pause(msg="Press any key to continue ...."):
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
                Thanks for choosing us, we hope you have been helpful.
                The KernelPanicBlog Team.
                Our web: http://kernelpanicblog.wordpress.com\033[1;m """)

    @staticmethod
    def banner():

        print("""
    888    d8P                                     888
    888   d8P                                      888
    888  d8P                                       888
    888d88K      .d88b.  888d888 88888b.   .d88b.  888
    8888888b    d8P  Y8b 888P"   888 "88b d8P  Y8b 888
    888  Y88b   88888888 888     888  888 88888888 888
    888   Y88b  Y8b.     888     888  888 Y8b.     888
    888    Y88b  "Y8888  888     888  888  "Y8888  888



    8888888b.                    d8b              888888b.   888
    888   Y88b                   Y8P              888  "88b  888
    888    888                                    888  .88P  888
    888   d88P  8888b.  88888b.  888  .d8888b     8888888K.  888  .d88b.   .d88b.
    8888888P"      "88b 888 "88b 888 d88P"        888  "Y88b 888 d88""88b d88P"88b
    888        .d888888 888  888 888 888          888    888 888 888  888 888  888
    888        888  888 888  888 888 Y88b.        888   d88P 888 Y88..88P Y88b 888
    888        "Y888888 888  888 888  "Y8888P     8888888P"  888  "Y88P"   "Y88888
                          Version 0.1a                                         888
     \033[1;36mManjaro GNU/Linux Post Installation Script\033[1;m \033[1;m                         Y8b d88P
     \033[1;32m  Author: SniferL4bs | www.sniferl4bs.com \033[1;m                         "Y88P"
     \033[1;32m  Author: NeoRanger  | www.neositelinux.com.ar \033[1;m
     \033[1;32m  Author: Harrinsoft |                         \033[1;m
     \033[1;32m  Colaborative Blog: | http://kernelpanicblog.wordpress.com \033[1;m

     Application in Testing Fase, please report your bugs!""")

    @staticmethod
    def help():
        print('''				|\033[1;36mHelp\033[1;m|
                You can write 2 commands and do a shortcut:
                back -> command for return to the previous option
                exit -> program exit
                Ctrl+C -> shortcut to finish the script execution
               ''')
