import os
import sys, traceback
import mpis

def internet():
	print ('''
|\033[1;36mInternet\033[1;m|
1) Install Firefox
2) Install Google Chrome
3) Install Vivaldi
4) Install Telegram Desktop
5) Install Filezilla
6) Install Chromium
7) Install qBittorrent
8) Install UGet
9) Back
10) Go Home
			''')
	internet = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
	if internet == "1":
		if os.system("sudo pacman -S firefox") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif internet == "2":
		print ("This application is on the AUR repository (community). It will be install at your own risk.")
		if os.system("yaourt -S google-chrome") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif internet == "3":
		print ("This application is on the AUR repository (community). It will be install at your own risk.")
		if os.system("yaourt -S vivaldi") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif internet == "4":
		print ("This application will be installed from the Official Web Site.")
		print ("What is your architecture?:")
		optele = raw_input("1) 32 Bits 2) 64 Bits > ")
		if optele == "1":
			os.system("wget -c https://tdesktop.com/linux32")
			os.system("tar xvf linux32")
			os.system("sudo mv Telegram /opt/telegram")
			os.system("rm -r linux32")
			os.system("cd /opt/telegram")
			os.system("./Telegram")
		elif optele == "2":
			os.system("wget -c https://tdesktop.com/linux")
			os.system("tar xvf linux")
			os.system("sudo mv Telegram /opt/telegram")
			os.system("rm -r linux")
			os.system("cd /opt/telegram")
			os.system("./Telegram")
		else:
			print ("\033[1;31mSorry, invalid command!\033[1;m")
			raw_input('Task Finished. You have tu close Telegram to continue. Press Enter to continue')
	elif internet == "5":
		if os.system("sudo pacman -S filezilla") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif internet == "6":
		if os.system("sudo pacman -S chromium") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif internet == "7":
		if os.system("sudo pacman -S qbittorrent") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif internet == "8":
		if os.system("sudo pacman -S uget") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif internet == "back" or internet == "9":
		mpis.clear()
		main_menu()
	elif internet == "gohome" or internet == "10":
		mpis.clear()
		main_menu()
	elif internet == "exit":
		sys.exit(0)
	else:
		print ("\033[1;31mSorry, invalid command!\033[1;m")