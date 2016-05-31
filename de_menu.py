import os
import sys, traceback
import mpis

def de():
    print ('''
|\033[1;36mDesktop Environments\033[1;m|
1) Install XFCE
2) Install Gnome-Shell
3) Install LXDE
4) Install Plasma 5
5) Install KDE
6) Back
7) Go Home
			''')
    de_menu = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
    if de_menu == "1":
        if os.system("sudo pacman -S xfce4") == 0:
            raw_input('Task Finished. Press Enter to continue')
        else:
            raw_input('Task Finished with errors. Press Enter to continue')
    elif de_menu == "2":
        if os.system("sudo pacman -S gnome-shell") == 0:
            raw_input('Task Finished. Press Enter to continue')
        else:
            raw_input('Task Finished with errors. Press Enter to continue')
    elif de_menu == "3":
        if os.system("sudo pacman -S lxde") == 0:
            raw_input('Task Finished. Press Enter to continue')
        else:
            raw_input('Task Finished with errors. Press Enter to continue')
    elif de_menu == "4":
        if os.system("sudo pacman -S plasma5") == 0:
            raw_input('Task Finished. Press Enter to continue')
        else:
            raw_input('Task Finished with errors. Press Enter to continue')
    elif de_menu == "5":
        if os.system("sudo pacman -S  kde4") == 0:
            raw_input('Task Finished. Press Enter to continue')
        else:
            raw_input('Task Finished with errors. Press Enter to continue')
    elif de_menu == "back" or de_menu == "6":
        mpis.clear()
        main_menu()
    elif de_menu == "gohome" or de_menu == "7":
        mpis.clear()
        main_menu()
    elif de_menu == "exit":
        sys.exit(0)
    else:
        print ("\033[1;31mSorry, invalid command!\033[1;m")