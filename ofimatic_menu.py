import os
import sys, traceback
import mpis

def ofimatic():
	print ('''
|\033[1;36mOfimatic033[1;m|
1) Install LibreOffice
2) Install OpenOffice
3) Install WPS
4) Install Calligra
5) Back
6) Go Home
			''')
	ofimatic = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
	if ofimatic == "1":
		if os.system("sudo pacman -S libreoffice-still") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif ofimatic == "2":
		if os.system("sudo pacman -S openoffice") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif ofimatic == "3":
		print ("This application is on the AUR repository (community). It will be install at your own risk.")
		if os.system("yaourt -S wps-office") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif ofimatic == "4":
		if os.system("sudo pacman -S calligra") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif ofimatic == "back" or ofimatic == "5":
		mpis.clear()
		main_menu()
	elif ofimatic == "gohome" or ofimatic == "6":
		mpis.clear()
		main_menu()
	elif ofimatic == "exit":
		sys.exit(0)
	else:
		print ("\033[1;31mSorry, invalid command!\033[1;m")