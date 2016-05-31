import os
import sys, traceback
import mpis

def multimedia():
	print ('''
|\033[1;36mMultimedia\033[1;m|
1) Install VLC
2) Install Vokoscreen
3) Install Audacity
4) Install OpenShot
5) Install Audacious
6) Install SMTube
7) Install moc (Music Player form Terminal)
8) Install Handbrake
9) Install SoundJuicer
10) Install Clipgrab
11) Install Mumble
12) Install KODI
13) Install SoundConverter (GTK)
14) Install SoundKonverter (QT)
15) Install Youtube-dl
16) Install mpv
17) Install simplescreenrecorder
18) Install OBS Studio
19) Install Totem
20) Back
21) Go Home
			''')
	multimedia = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
	if multimedia == "1":
		if os.system("sudo pacman -S vlc") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
		elif multimedia == "2":
			print ("This application is on the AUR repository (community). It will be install at your own risk.")
			if os.system("yaourt -S vokoscreen") == 0:
				raw_input('Task Finished. Press Enter to continue')
			else:
				raw_input('Task Finished with errors. Press Enter to continue')
		elif multimedia == "3":
			if os.system("sudo pacman -S audacity") == 0:
				raw_input('Task Finished. Press Enter to continue')
			else:
				raw_input('Task Finished with errors. Press Enter to continue')
		elif multimedia == "4":
			if os.system("sudo pacman -S openshot") == 0:
				raw_input('Task Finished. Press Enter to continue')
			else:
				raw_input('Task Finished with errors. Press Enter to continue')
		elif multimedia == "5":
			if os.system("sudo pacman -S audacious") == 0:
				raw_input('Task Finished. Press Enter to continue')
			else:
				raw_input('Task Finished with errors. Press Enter to continue')
		elif multimedia == "6":
			if os.system("sudo pacman -S smtube") == 0:
				raw_input('Task Finished. Press Enter to continue')
			else:
				raw_input('Task Finished with errors. Press Enter to continue')
		elif multimedia == "7":
			if os.system("sudo pacman -S moc") == 0:
				raw_input('Task Finished. Press Enter to continue')
			else:
				raw_input('Task Finished with errors. Press Enter to continue')
		elif multimedia == "8":
			if os.system("sudo pacman -S handbrake") == 0:
				raw_input('Task Finished. Press Enter to continue')
			else:
				raw_input('Task Finished with errors. Press Enter to continue')
		elif multimedia == "9":
			if os.system("sudo pacman -S sound-juicer") == 0:
				raw_input('Task Finished. Press Enter to continue')
			else:
				raw_input('Task Finished with errors. Press Enter to continue')
			elif multimedia == "10":
				if os.system("sudo pacman -S clipgrab") == 0:
					raw_input('Task Finished. Press Enter to continue')
				else:
					raw_input('Task Finished with errors. Press Enter to continue')
			elif multimedia == "11":
				if os.system("sudo pacman -S mumble") == 0:
					raw_input('Task Finished. Press Enter to continue')
				else:
					raw_input('Task Finished with errors. Press Enter to continue')
			elif multimedia == "12":
				if os.system("sudo pacman -S kodi") == 0:
					raw_input('Task Finished. Press Enter to continue')
				else:
					raw_input('Task Finished with errors. Press Enter to continue')
			elif multimedia == "13":
				if os.system("sudo pacman -S soundconverter") == 0:
					raw_input('Task Finished. Press Enter to continue')				
				else:
					raw_input('Task Finished with errors. Press Enter to continue')				
			elif multimedia == "14":
				if os.system("sudo pacman -S soundkonverter") == 0:
					raw_input('Task Finished. Press Enter to continue')
				else:
					raw_input('Task Finished with errors. Press Enter to continue')
			elif multimedia == "15":
				if os.system("sudo pacman -S youtube-dl") == 0:
					raw_input('Task Finished. Press Enter to continue')
				else:
					raw_input('Task Finished with errors. Press Enter to continue')
			elif multimedia == "16":
				if os.system("sudo pacman -S mpv") == 0:
					raw_input('Task Finished. Press Enter to continue')
				else:
					raw_input('Task Finished with errors. Press Enter to continue')
			elif multimedia == "17":
				print ("This application is on the AUR repository (community). It will be install at your own risk.")
				if os.system("yaourt -S simplescreenrecorder") == 0:
					raw_input('Task Finished. Press Enter to continue')
				else:
					raw_input('Task Finished with errors. Press Enter to continue')
			elif multimedia == "18":
				if os.system("sudo pacman -S obs-studio"):
					raw_input('Task Finished. Press Enter to continue')
				else:
					raw_input('Task Finished with errors. Press Enter to continue')
			elif multimedia == "19":
				if os.system("sudo pacman -S totem"):
					raw_input('Task Finished. Press Enter to continue')
				else:
					raw_input('Task Finished with errors. Press Enter to continue')
			elif multimedia == "back" or multimedia == "20":
				clear()
				main_menu()
			elif multimedia == "gohome" or multimedia == "21":
				clear()
				main_menu()
			elif multimedia == "exit":
				sys.exit(0)
			else:
				print ("\033[1;31mSorry, invalid command!\033[1;m")