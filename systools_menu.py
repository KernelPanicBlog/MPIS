import os
import sys, traceback
import mpis

def systools():
	print ('''
|\033[1;36mSystem Tools\033[1;m|
1) Terminator
2) Manjaro Settings Manager (GTK)
3) Manjaro Settings Manager (Plasma5)
4) VirtualBox
5) Octopi (Pacman GUI)
6) Pamac (Pacman GUI)
7) Back
8) Go Home
			''')
	systools = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
	if systools == "1":
		if os.system("sudo pacman -S terminator") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif systools == "2":
		if os.system("sudo pacman -S manjaro-settings-manager") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif systools == "3":
		if os.system("sudo pacman -S manjaro-settings-manager") == 0:
			if os.system("sudo pacman -S manjaro-settings-manager-kcm") == 0:
				if os.system("sudo pacman -S manjaro-settings-manager-knotifier") == 0:
					raw_input('Task Finished. Press Enter to continue')
				else:
					raw_input('Task Finished with errors. Press Enter to continue')
	elif systools == "4":
		if os.system("sudo pacman -S virtualbox") == 0:
			print ("Don't forget install virtualbox's kernel modules")
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif systools == "5":
		if os.system("sudo pacman -S octopi") == 0:
			if os.system("sudo pacman -S octopi-notifier") == 0:
				raw_input('Task Finished. Press Enter to continue')
			else:
				raw_input('Task Finished with errors. Press Enter to continue')
	elif systools == "6":
		if os.system("sudo pacman -S pamac") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif systools == "back" or systools == "7":
		mpis.clear()
		main_menu()
	elif systools == "gohome" or systools == "8":
		mpis.clear()
		main_menu()
	elif systools == "exit":
		sys.exit(0)
	else:
		print ("\033[1;31mSorry, invalid command!\033[1;m")