#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Manjaro script post-instalation that allow to the users to choose different
# options such as install an application or config some tools and environments.

import sys
import traceback
import core
import os


def main():
    try:
        mpisw = core.Mpis()
        mpisw.clear()
        mpisw.banner()
        mpisw.pause()
        mpisw.clear()
        mpisw.help()
        mpisw.pause()
        # main menu
        while True:
            mpisw.clear()
            print('|\033[1;36m--Main Menu-- \033[1;m|')
            for i in mpisw.main_menu:
                print('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
            main_input = mpisw.user_input()
            # update system menu :completo: testiar.
            while main_input == 1:
                mpisw.clear()
                print('|\033[1;36mUpdate System\033[1;m|')
                for i in mpisw.menu_update_system:
                    print('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                update_input = mpisw.user_input()
                if update_input == 1:
                    print("Installing keys...")
                    if os.system("sudo pacman -S archlinux-keyring "
                                 "manjaro-keyring") == 0:
                        if os.system("sudo pacman-keys --init") == 0:
                            if os.system("sudo pacman-keys --populate "
                                         "archlinux manjaro") == 0:
                                print("Keys Installed")
                    print("Updating Mirrors...")
                    if os.system("sudo pacman-mirrors -g") == 0:
                        print("Mirrors Updated")
                    mpisw.pause(mpisw.msgTF)
                elif update_input == 2:
                    mpisw.execute_command("sudo pacman -Syy")
                elif update_input == 3:
                    mpisw.execute_command("yaourt -Syy")
                elif update_input == 4:
                    print("Do you want refresh mirrors in the "
                          "full system update?")
                    opupdate = int(input("1) Yes 2) No > "))
                    if opupdate == 1:
                        mpisw.execute_command("sudo rm -f "
                                              "/var/lib/pacman/db.lck && "
                                              "sudo pacman-mirrors -g && "
                                              "sudo pacman -Syyuu  && "
                                              "sudo pacman -Suu")
                    elif opupdate == 2:
                        mpisw.execute_command("sudo rm -f "
                                              "/var/lib/pacman/db.lck && "
                                              "sudo pacman -Syyuu  && "
                                              "sudo pacman -Suu")
                    else:
                        print("\033[1;31mSorry, invalid command!\033[1;m")
                elif update_input == 5:
                    print("Cleaning cache...")
                    mpisw.execute_command("sudo pacman -Sc && "
                                          "sudo pacman -Scc", "Cache cleared")

                    print("Cleaning orphan packages...")
                    mpisw.execute_command("sudo pacman -Rsn && yaourt -Rsn ",
                                          "Orphan packages cleared")
                elif update_input == 6:
                    with open('/etc/pacman.d/mirrorlist', 'r') as f:
                        print(f.read())
                    mpisw.pause()
                    mpisw.clear()
                elif update_input == 7:
                    main_input = 0
                    break
                elif update_input == 8:
                    mpisw.clear()
                    mpisw.end_message()
                    sys.exit(0)

            # menu install app :completo: testiar
            while main_input == 2:
                mpisw.clear()
                print('|\033[1;36mInstall Applications\033[1;m|')
                for i in mpisw.menu_install_app:
                    print('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                install_input = int(input("\033[1;36mMPIS > \033[1;m"))

                # menu ofimatic :completo: testiar
                while install_input == 1:
                    mpisw.clear()
                    print('|\033[1;36mOfimatic033[1;m|')
                    for i in mpisw.menu_Ofimatic:
                        print('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    ofimatic_input = mpisw.user_input()
                    if ofimatic_input < 5:
                        mpisw.execute_command(mpisw.apps_ofimatic[
                                                  ofimatic_input-1][1])
                    elif ofimatic_input == 5:
                        install_input = 0
                    elif ofimatic_input == 6:
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)

                # menu multimedia :completo: testiar
                while install_input == 2:
                    mpisw.clear()
                    print('|\033[1;36mMultimedia033[1;m|')
                    for i in mpisw.menu_multimedia:
                        print('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    multimedia_input = mpisw.user_input()
                    if multimedia_input <= 19 and multimedia_input != 0:
                        mpisw.execute_command(mpisw.apps_multimedia[
                            multimedia_input - 1][1])
                    elif multimedia_input == 20:
                        install_input = 0
                    elif multimedia_input == 21:
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)

                # menu development :completo: testiar
                while install_input == 3:
                    mpisw.clear()
                    print('|\033[1;Development[1;m|')
                    for i in mpisw.menu_development:
                        print('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    development_input = mpisw.user_input()
                    if development_input <= 8 and development_input != 0:
                        mpisw.execute_command(mpisw.apps_development[
                                    development_input - 1][1])
                    elif development_input == 9:
                        install_input = 0
                    elif development_input == 10:
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)

                # menu Internet :completo: testiar
                while install_input == 4:
                    mpisw.clear()
                    print('|\033[1;Internet[1;m|')
                    for i in mpisw.menu_Internet:
                        print('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    internet_input = mpisw.user_input()
                    if internet_input <= 8 and internet_input != 0:
                        mpisw.execute_command(mpisw.apps_internet[
                                internet_input - 1][1])
                    elif internet_input == 9:
                        install_input = 0
                    elif internet_input == 10:
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)

                # menu games  :completo: testiar
                while install_input == 5:
                    mpisw.clear()
                    print('|\033[1;Games[1;m|')
                    for i in mpisw.menu_Games:
                        print('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    games_input = mpisw.user_input()
                    if games_input <= 8 and games_input != 0:
                        mpisw.execute_command(mpisw.apps_Games[
                                                games_input - 1][1])
                    elif games_input == 12:
                        install_input = 0
                    elif games_input == 13:
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)

                # menu system tools :completo: testiar
                while install_input == 6:
                    mpisw.clear()
                    print('|\033[1;System Tools[1;m|')
                    for i in mpisw.menu_Sys_Tools:
                        print('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    systools_input = mpisw.user_input()
                    if systools_input == 1:
                        mpisw.execute_command("sudo pacman -S terminator")
                    elif systools_input == 2:
                        mpisw.execute_command("sudo pacman -S "
                                              "manjaro-settings-manager")
                    elif systools_input == 3:
                        if mpisw.execute_command("sudo pacman -S "
                                                 "manjaro-settings-"
                                                 "manager") == 0:
                            if mpisw.execute_command("sudo pacman -S "
                                                     "manjaro-settings-"
                                                     "manager-kcm") == 0:
                                mpisw.execute_command("sudo pacman -S manjaro-"
                                                      "settings-manager-"
                                                      "knotifier")
                    elif systools_input == 4:
                        if mpisw.execute_command("sudo pacman -S "
                                                 "virtualbox") == 0:
                            print("Don't forget install virtualbox's "
                                  "kernel modules")
                    elif systools_input == 5:
                        if mpisw.execute_command("sudo pacman -S octopi") == 0:
                            mpisw.execute_command("sudo pacman -S "
                                                  "octopi-notifier")
                    elif systools_input == 6:
                        mpisw.execute_command("sudo pacman -S pamac")
                    elif systools_input == 7:
                        install_input = 0
                    elif systools_input == 8:
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)

                # menu back
                while install_input == 7:
                    main_input = 0
                    install_input = 0

                # menu exit
                while install_input == 8:
                    sys.exit(0)

            # no implementado todavia
            while main_input == 3:
                mpisw.clear()
                print(mpisw.msgNf)
                mpisw.pause()
                main_input = 0

            # no implementado todavia
            while main_input == 4:
                mpisw.clear()
                print(mpisw.msgNf)
                mpisw.pause()
                main_input = 0

            # menu Install DEs & WMs :completo: testiar
            while main_input == 5:
                mpisw.clear()
                print('|\033[1;36mDEs & WMs Installations\033[1;m|')
                for i in mpisw.menu_DEs_WMs:
                    print('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                des_wms_input = int(input("\033[1;36mMPIS > \033[1;m"))
                # menu Desktop Environments :completo: testiar
                while des_wms_input == 1:
                    mpisw.clear()
                    print('|\033[1;36mDesktop Environments\033[1;m|')
                    for i in mpisw.menu_DEs:
                        print('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    des_input = mpisw.user_input()
                    if des_input < 6:
                        mpisw.execute_command(mpisw.apps_DEs[des_input - 1][1])
                    # back menu
                    elif des_input == 6:
                        des_wms_input = 0
                    # exit menu
                    elif des_input == 7:
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)
                # menu Window Managers :completo: testiar
                while des_wms_input == 2:
                    mpisw.clear()
                    print('|\033[1;36mWindow Managers\033[1;m|')
                    for i in mpisw.menu_WMs:
                        print('\033[1;36m' + i[1] + '.- ' + i[0] + '\033[1;m')
                    wms_input = mpisw.user_input()
                    if wms_input < 4:
                        mpisw.execute_command(mpisw.apps_WMs[wms_input - 1][1])
                    # back menu
                    elif wms_input == 4:
                        des_wms_input = 0
                    # exit menu
                    elif wms_input == 5:
                        mpisw.clear()
                        mpisw.end_message()
                        sys.exit(0)
                # back menu
                while des_wms_input == 3:
                    mpisw.clear()
                    des_wms_input = 0
                    main_input = 0
                # exit menu
                while des_wms_input == 4:
                    mpisw.clear()
                    mpisw.end_message()
                    sys.exit(0)

            # no implementado todavia
            while main_input == 6:
                mpisw.clear()
                print(mpisw.msgNf)
                mpisw.pause()
                main_input = 0

            # menu update script sin testiar
            while main_input == 7:
                mpisw.execute_command("wget -c "
                                      "https://www.dropbox.com/s/"
                                      "ky7yb2pfnt2tnlv/apps.config?dl=0 "
                                      "https://www.dropbox.com/s/"
                                      "dvh13gpldqhfifv/menus.config?dl=0")
                mpisw.reload()
                mpisw.pause(mpisw.msgTF)
                main_input = 0

            # menu help
            while main_input == 8:
                mpisw.help()
                mpisw.pause()
                mpisw.clear()
                main_input = 0

            # exit
            while main_input == 9:
                mpisw.clear()
                mpisw.end_message()
                sys.exit(0)
    except KeyboardInterrupt:
        print("\nYou had press the Ctrl+C keys combination. Accepted exit "
              "request. Bye!")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == '__main__':
    main()
