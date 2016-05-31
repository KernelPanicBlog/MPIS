import os
import sys, traceback
import mpis
def wm():
    print ('''
|\033[1;36mWindow Managers\033[1;m|
1) Install i3-wm
2) Install Openbox
3) Install Fluxbox
4) Back
5) Go Home
            ''')
    wm_menu = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
    if wm_menu == "1":
    	if os.system("sudo pacman -S i3-wm") == 0:
    		raw_input('Task Finished. Press Enter to continue')
        else:
        	raw_input('Task Finished with errors. Press Enter to continue')
    elif wm_menu == "2":
    	if os.system("sudo pacman -S openbox") == 0:
    		raw_input('Task Finished. Press Enter to continue')
    	else:
    		raw_input('Task Finished with errors. Press Enter to continue')
    elif wm_menu == "3":
    	if os.system("sudo pacman -S fluxbox") == 0:
    		raw_input('Task Finished. Press Enter to continue')
    	else:
    		raw_input('Task Finished with errors. Press Enter to continue')
    elif wm_menu == "back" or wm_menu == "4":
    	mpis.clear()
    	mpis.main_menu()
    elif wm_menu == "gohome" or wm_menu == "5":
    	mpis.clear()
    	mpis.main_menu()
    elif wm_menu == "exit":
    	sys.exit(0)
    else:
    	print ("\033[1;31mSorry, invalid command!\033[1;m")