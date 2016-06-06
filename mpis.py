#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os
import sys
import traceback
import csv


class Mpis():
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
        self.apps_ofimatic= []
        self.apps_multimedia = []
        self.apps_development = []
        self.apps_internet = []
        self.apps_Games = []
        self.apps_DEs = []
        self.apps_WMs = []
        self.__load_menus()
        self.__load_apps()
        self.msgMpis = '\033[1;36mMPIS > \033[1;m'
        self.msgTFWE = 'Task Finished with errors. press enter to continue'
        self.msgTF = 'Task Finished. Press Enter to continue'
        self.msgAur = "This application is on the AUR repository (community). It will be install at your own risk."
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
                if i[0] == "Ofimatic":
                    self.apps_ofimatic.append([i[1], i[2]])
                elif i[0] == "Multimedia":
                    self.apps_multimedia.append([i[1], i[2]])
                elif i[0] == "Development":
                    self.apps_development.append([i[1], i[2]])
                elif i[0] == "Internet":
                    self.apps_internet.append([i[1], i[2]])
                elif i[0] == "Games":
                    self.apps_Games.append([i[1], i[2]])
                elif i[0] == "DEs":
                    self.apps_DEs.append([i[1], i[2]])
                elif i[0] == "WMs":
                    self.apps_WMs.append([i[1], i[2]])

    def reload(self):
        self.__load_apps()
        self.__load_menus()

    def execute_command(self, command, msg="..."):
        a = 0
        if command == "Telegram":
            print (
            "This application will be installed from the Official Web Site.")
            print ("What is your architecture?:")
            optele = raw_input("1) 32 Bits 2) 64 Bits > ")
            if optele == "1":
                os.system("wget -c https://tdesktop.com/linux32")
                os.system("tar xvf linux32")
                os.system("sudo mv Telegram /opt/telegram")
                os.system("rm -r linux32")
                os.system("./opt/telegram/Telegram")
            elif optele == "2":
                os.system("wget -c https://tdesktop.com/linux")
                os.system("tar xvf linux")
                os.system("sudo mv Telegram /opt/telegram")
                os.system("rm -r linux")
                os.system("./opt/telegram/Telegram")
            else:
                print ("\033[1;31mSorry, invalid command!\033[1;m")
        else:
            if command.startswith("yaourt"):
                print (self.msgAur)
            if os.system(command) == 0:
                if msg != "...":
                    print(msg)
                a = 0
                raw_input(self.msgTF)
            else:
                a = 2
                raw_input(self.msgTFWE)
        return a

    def clear(self):
        os.system("clear")

    def end_message(self):
        print ('''\033[1;36m
    		Thanks for choosing us, we hope you have been helpful.
    		The KernelPanicBlog Team.
    		Our web: http://kernelpanicblog.wordpress.com\033[1;m ''')

    def banner(self):

        print """
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

     Application in Testing Fase, please report your bugs!"""

    def help(self):
        print ('''				|\033[1;36mHelp\033[1;m|
    			You can write 2 commands and do a shortcut:
    			back -> command for return to the previous option
    			exit -> program exit
    			Ctrl+C -> shortcut to finish the script execution
    			''')


def main():
    try:
        mpisw = Mpis()
        # main menu
        while True:
            mpisw.clear()
            mpisw.banner()
            raw_input("Press any key to continue ....")
            mpisw.clear()
            mpisw.help()
            raw_input("Press any key to continue ....")
            mpisw.clear()
            print ('|\033[1;36m--Main Menu-- \033[1;m|')
            for i in mpisw.main_menu:
                print ('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
            main_input = raw_input(mpisw.msgMpis)
            # update system menu :completo: testiar.
            while main_input == "1":
                mpisw.clear()
                print ('|\033[1;36mUpdate System\033[1;m|')
                for i in mpisw.menu_update_system:
                    print ('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                update_input = raw_input(mpisw.msgMpis)
                if update_input == "1":
                    print ("Installing keys...")
                    if os.system("sudo pacman -S archlinux-keyring "
                                 "manjaro-keyring") == 0:
                        if os.system("sudo pacman-keys --init") == 0:
                            if os.system("sudo pacman-keys --populate "
                                         "archlinux manjaro") == 0:
                                print ("Keys Installed")
                    print ("Updating Mirrors...")
                    if os.system("sudo pacman-mirrors -g") == 0:
                        print ("Mirrors Updated")
                    raw_input(mpisw.msgTF)
                elif update_input == "2":
                    mpisw.execute_command("sudo pacman -Syy")
                elif update_input == "3":
                    mpisw.execute_command("yaourt -Syy")
                elif update_input == "4":
                    print ("Do you want refresh mirrors in the "
                           "full system update?")
                    opupdate = raw_input("1) Yes 2) No > ")
                    if opupdate == "1":
                        mpisw.execute_command("sudo rm -f "
                                              "/var/lib/pacman/db.lck && "
                                              "sudo pacman-mirrors -g && "
                                              "sudo pacman -Syyuu  && "
                                              "sudo pacman -Suu")
                    elif opupdate == "2":
                        mpisw.execute_command("sudo rm -f "
                                              "/var/lib/pacman/db.lck && "
                                              "sudo pacman -Syyuu  && "
                                              "sudo pacman -Suu")
                    else:
                        print ("\033[1;31mSorry, invalid command!\033[1;m")
                elif update_input == "5":
                    print ("Cleaning cache...")
                    mpisw.execute_command("sudo pacman -Sc && "
                                          "sudo pacman -Scc", "Cache cleared")

                    print ("Cleaning orphan packages...")
                    mpisw.execute_command("sudo pacman -Rsn && yaourt -Rsn ",
                                          "Orphan packages cleared")
                elif update_input == "6":
                    with open('/etc/pacman.d/mirrorlist', 'r') as f:
                        print f.read()
                elif update_input == "7":
                    main_input = 0
                    break
                elif update_input == "8":
                    mpisw.clear()
                    mpisw.end_message()
                    sys.exit(0)

            # menu install app :completo: testiar
            while main_input == "2":
                mpisw.clear()
                print ('|\033[1;36mInstall Applications\033[1;m|')
                for i in mpisw.menu_install_app:
                    print ('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                install_input = raw_input("\033[1;36mMPIS > \033[1;m")

                # menu ofimatic :completo: testiar
                while install_input == "1":
                    mpisw.clear()
                    print ('|\033[1;36mOfimatic033[1;m|')
                    for i in mpisw.menu_Ofimatic:
                        print ('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    ofimatic_input = raw_input("\033[1;36mMPIS > \033[1;m")
                    a = int(ofimatic_input)
                    if a < 5:
                        mpisw.execute_command(mpisw.apps_ofimatic[a-1][1])
                    elif ofimatic_input == "5":
                        install_input = 0
                    elif ofimatic_input == "6":
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)

                # menu multimedia :completo: testiar
                while install_input == "2":
                    mpisw.clear()
                    print ('|\033[1;36mMultimedia033[1;m|')
                    for i in mpisw.menu_multimedia:
                        print ('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    multimedia_input = raw_input(mpisw.msgMpis)
                    a = int(multimedia_input)
                    if a <= 19 and a != 0:
                        mpisw.execute_command(mpisw.apps_multimedia[int(
                            multimedia_input) - 1][1])
                    elif multimedia_input == "20":
                        install_input = 0
                    elif multimedia_input == "21":
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)

                # menu development :completo: testiar
                while install_input == "3":
                    mpisw.clear()
                    print ('|\033[1;Development[1;m|')
                    for i in mpisw.menu_development:
                        print ('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    development_input = raw_input(mpisw.msgMpis)
                    a = int(development_input)
                    if a <= 8 and a != 0:
                        mpisw.execute_command(mpisw.apps_development[int(
                            development_input) - 1][1])
                    elif development_input == "9":
                        install_input = 0
                    elif development_input == "10":
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)

                # menu Internet :completo: testiar
                while install_input == "4":
                    mpisw.clear()
                    print ('|\033[1;Internet[1;m|')
                    for i in mpisw.menu_Internet:
                        print ('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    internet_input = raw_input(mpisw.msgMpis)
                    a = int(internet_input)
                    if a <= 8 and a != 0:
                        mpisw.execute_command(mpisw.apps_internet[int(
                            internet_input) - 1][1])
                    elif internet_input == "9":
                        install_input = 0
                    elif internet_input == "10":
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)

                # menu games  :completo: testiar
                while install_input == "5":
                    mpisw.clear()
                    print ('|\033[1;Games[1;m|')
                    for i in mpisw.menu_Games:
                        print ('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    games_input = raw_input(mpisw.msgMpis)
                    a = int(games_input)
                    if a <= 8 and a != 0:
                        mpisw.execute_command(mpisw.apps_Games[int(
                            games_input) - 1][1])
                    elif games_input == "12":
                        install_input = 0
                    elif games_input == "13":
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)

                # menu system tools :completo: testiar
                while install_input == "6":
                    mpisw.clear()
                    print ('|\033[1;System Tools[1;m|')
                    for i in mpisw.menu_Sys_Tools:
                        print ('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    systools_input = raw_input(mpisw.msgMpis)
                    if systools_input == "1":
                        mpisw.execute_command("sudo pacman -S terminator")
                    elif systools_input == "2":
                        mpisw.execute_command("sudo pacman -S "
                                              "manjaro-settings-manager")
                    elif systools_input == "3":
                        if mpisw.execute_command("sudo pacman -S "
                                                 "manjaro-settings-"
                                                 "manager") == 0:
                            if mpisw.execute_command("sudo pacman -S "
                                                     "manjaro-settings-"
                                                     "manager-kcm") == 0:
                                mpisw.execute_command("sudo pacman -S manjaro-"
                                                      "settings-manager-"
                                                      "knotifier")
                    elif systools_input == "4":
                        if mpisw.execute_command("sudo pacman -S "
                                                 "virtualbox") == 0:
                            print ("Don't forget install virtualbox's "
                                   "kernel modules")
                    elif systools_input == "5":
                        if mpisw.execute_command("sudo pacman -S octopi") == 0:
                            mpisw.execute_command("sudo pacman -S "
                                                  "octopi-notifier")
                    elif systools_input == "6":
                        mpisw.execute_command("sudo pacman -S pamac")
                    elif systools_input == "7":
                        install_input = 0
                    elif systools_input == "8":
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)

                # menu back
                while install_input == "7":
                    main_input = 0
                    install_input = 0

                # menu exit
                while install_input == "8":
                    sys.exit(0)

            # no implementado todavia
            while main_input == "3":
                mpisw.clear()
                print (mpisw.msgNf)
                raw_input('Press ENTER to continue...!')
                main_input = 0

            # no implementado todavia
            while main_input == "4":
                mpisw.clear()
                print (mpisw.msgNf)
                raw_input('Press ENTER to continue...!')
                main_input = 0

            # menu Install DEs & WMs :completo: testiar
            while main_input == "5":
                mpisw.clear()
                print ('|\033[1;36mDEs & WMs Installations\033[1;m|')
                for i in mpisw.menu_DEs_WMs:
                    print ('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                DEs_WMs_input = raw_input("\033[1;36mMPIS > \033[1;m")
                # menu Desktop Environments :completo: testiar
                while DEs_WMs_input == "1":
                    print ('|\033[1;36mDesktop Environments\033[1;m|')
                    for i in mpisw.menu_DEs:
                        print ('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    DEs_input = raw_input("\033[1;36mMPIS > \033[1;m")
                    a = int(DEs_input)
                    if a < 6:
                        mpisw.execute_command(mpisw.apps_DEs[a - 1][1])
                    # back menu
                    elif DEs_input == "6":
                        DEs_WMs_input = 0
                    # exit menu
                    elif DEs_input == "7":
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)
                # menu Window Managers :completo: testiar
                while DEs_WMs_input == "2":
                    print ('|\033[1;36mWindow Managers\033[1;m|')
                    for i in mpisw.menu_WMs:
                        print ('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    WMs_input = raw_input("\033[1;36mMPIS > \033[1;m")
                    a = int(WMs_input)
                    if a < 4:
                        mpisw.execute_command(mpisw.apps_WMs[a - 1][1])
                    # back menu
                    elif WMs_input == "5":
                        DEs_WMs_input = 0
                    # exit menu
                    elif WMs_input == "6":
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)
                # back menu
                while DEs_WMs_input == "3":
                    mpisw.clear()
                    DEs_WMs_input = 0
                    main_input = 0
                # exit menu
                while DEs_WMs_input == "4":
                    mpisw.clear()
                    mpisw.end_message()
                    sys.exit(0)

            #no implementado todavia
            while main_input == "6":
                mpisw.clear()
                print (mpisw.msgNf)
                raw_input('Press ENTER to continue...!')
                main_input = 0

            # menu update script sin testiar
            while main_input == "7":
                mpisw.execute_command("wget -c "
                                      "https://www.dropbox.com/s/"
                                      "ky7yb2pfnt2tnlv/apps.config?dl=0 "
                                      "https://www.dropbox.com/s/"
                                      "dvh13gpldqhfifv/menus.config?dl=0")
                mpisw.reload()

            #menu help
            while main_input == "8":
                mpisw.help()
                raw_input('Press ENTER to continue...!')
                mpisw.clear()
                main_input = 0

            #exit
            while main_input == "9":
                mpisw.clear()
                mpisw.end_message()
                sys.exit(0)
    except KeyboardInterrupt:
        print "\nYou had press the Ctrl+C keys combination. Accepted exit request. Bye!"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == '__main__':
    main()