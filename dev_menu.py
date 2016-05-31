import os
import sys, traceback
import mpis

def development():
	print ('''
|\033[1;36mDevelopment\033[1;m|
1) Install Geany
2) Install Sublime Text 2
3) Install Sublime Text 3
4) Install Gedit
5) Install Eclipse
6) Install Android Studio
7) Install QtCreator
8) Install NinjaIDE
9) Back
10) Go Home
			''')
	development = raw_input("\033[1;32mWhat you want to do??> \033[1;m")
	if development == "1":
		if os.system("sudo pacman -S geany") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif development == "2":
		print ("This application is on the AUR repository (community). It will be install at your own risk.")
		if os.system("yaourt -S sublime-text") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif development == "3":
		print ("This application is on the AUR repository (community). It will be install at your own risk.")
		if os.system("yaourt -S sublime-text-dev") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif development == "4":
		if os.system("sudo pacman -S gedit") == 0:
			raw_input('Task Finished. Press Enter to continue')
			else:
				raw_input('Task Finished with errors. Press Enter to continue')
	elif development == "5":
		if os.system("sudo pacman -S eclipse") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif development == "6":
		print ("This application is on the AUR repository (community). It will be install at your own risk.")
		if os.system("yaourt -S android-studio") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
		elif development == "7":
			if os.system("sudo pacman -S qtcreator") == 0:
				raw_input('Task Finished. Press Enter to continue')
			else:
				raw_input('Task Finished with errors. Press Enter to continue')
		elif development == "8":
			if os.system("sudo pacman -S ninja-ide") == 0:
				raw_input('Task Finished. Press Enter to continue')
			else:
				raw_input('Task Finished with errors. Press Enter to continue')
		elif development == "back" or development == "9":
			clear()
			main_menu()
		elif development == "gohome" or development == "10":
			clear()
			main_menu()
		elif development == "exit":
			sys.exit(0)
		else:
			print ("\033[1;31mSorry, invalid command!\033[1;m")