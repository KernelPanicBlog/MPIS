#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
#
#Manjaro script post-instalation that allow to the users to choose different options
#such as install an application or config some tools and environments.

import os
import sys, traceback

def main():
	try:
		clear()
		banner()
		raw_input('Press any key to continue...!')
		clear()
		help()
		raw_input('Press any key to continue...!')
		def main_menu():
			while True:
				print ('''
 |\033[1;36mMenú Principal\033[1;m|
1) Update System
2) Install applications
3) List applications installed
4) Uninstall applications
5) Install DEs & WMs 
6) Personalitation
7) Help
8) Exit
''')

				update_menu = raw_input("\033[1;36mMPIS > \033[1;m")
				clear()
				while update_menu == "1":
					
					print ('''
|\033[1;36mUpdate System\033[1;m|
1) Refresh Mirrors and Keys
2) Pacman repositories update
3) AUR repositories update
4) Update all system
5) Clear cache and orphan packages
6) See the content of mirrorlist file
7) Back
8) Go Home
					''')
					update = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
					if update == "1":
					    print ("Installing keys...")
					    os.system("sudo pacman -S archlinux-keyring manjaro-keyring")
					    os.system("sudo pacman-keys --init")
					    os.system("sudo pacman-keys --populate archlinux manjaro")
					    print ("Keys instaled")
					    print ("Updating Mirrors...")
					    os.system("sudo pacman-mirrors -g")
					    print ("Mirrors Updated")
					    raw_input('Task Finished. Press Enter to continue')
					elif update == "2":
						if os.system("sudo pacman -Syy") == 0:
							raw_input('Task Finished. Press Enter to continue')
						else:
							raw_input('Task Finished with errors. Press Enter to continue')
					elif update == "3":
						if os.system("yaourt -Syy") == 0:
							raw_input('Task Finished. Press Enter to continue')
						else:
							raw_input('Task Finished with errors. Press Enter to continue')
					elif update == "4":
						print ("Do you want refresh mirrors in the full system update?")
						opupdate = raw_input("1) Yes 2) No > ")
						if opupdate == "1":
							os.system("sudo rm -f /var/lib/pacman/db.lck && sudo pacman-mirrors -g && sudo pacman -Syyuu  && sudo pacman -Suu")
						elif opupdate == "2":
							os.system("sudo rm -f /var/lib/pacman/db.lck && sudo pacman -Syyuu  && sudo pacman -Suu")
						else:
							print ("\033[1;31mSorry, invalid command!\033[1;m")
						raw_input('Task Finished. Press Enter to continue')
					elif update == "5":
					    print ("Cleaning caché...")
					    if os.system("sudo pacman -Sc && sudo pacman -Scc") == 0:
					    	print ("Cache cleared")
					    	print ("Cleaning orphan packages...")
					    	os.system("sudo pacman -Rsn && yaourt -Rsn ")
					    	print ("Orphan packages cleared")
					    	raw_input('Task Finished. Press Enter to continue')
					    else:
					    	raw_input('Task Finished with errors. Press Enter to continue')

					elif update == "6":
						file = open('/etc/pacman.d/mirrorlist', 'r')
						print file.read()					
					elif update == "back" or update == "7":
						clear()
						main_menu()					
					elif update == "gohome" or update == "8":
						clear()
						main_menu()
					elif update == "exit":
						sys.exit(0)
					else:
						print ("\033[1;31mSorry, invalid command!\033[1;m") 					
				
				while update_menu == "2":
					clear()
					print ('''
|\033[1;36mInstall Applications\033[1;m|
1) Ofimatic
2) Multimedia
3) Development
4) Internet
5) Games
6) Hacking Tools (Beta)
7) Back
8) Go Home
					''')
					application_menu = raw_input("\033[1;36mMPIS > \033[1;m")
					
					while application_menu == "1":
						clear()
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
							clear()
							main_menu()
						elif ofimatic == "gohome" or ofimatic == "6":
							clear()
							main_menu()
						elif ofimatic == "exit":
							sys.exit(0)
						else:
							print ("\033[1;31mSorry, invalid command!\033[1;m")
							
					while application_menu == "2":
						clear()
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
18) Back
19) Go Home
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
						elif multimedia == "back" or multimedia == "18":
							clear()
							main_menu()
						elif multimedia == "gohome" or multimedia == "19":
							clear()
							main_menu()
						elif multimedia == "exit":
							sys.exit(0)
						else:
							print ("\033[1;31mSorry, invalid command!\033[1;m")
					
					while application_menu == "3":
						clear()
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
					
					while application_menu == "4":
						clear()
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
							print ("This application is on the AUR repository (community). It will be install at your own risk.")
							print ("What is your architecture?:")
							optele = raw_input("1) 32 Bits 2) 64 Bits > ")
							if optele == "1":
								os.system("wget -c https://tdesktop.com/linux32")
								os.system("tar xvf linux32")
								os.system("sudo mv Telegram /opt/telegram")
								os.system("./opt/telegram/Telegram")
							elif optele == "2":
								os.system("wget -c https://tdesktop.com/linux")
								os.system("tar xvf linux")
								os.system("sudo mv Telegram /opt/telegram")
								os.system("./opt/telegram/Telegram")
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
							clear()
							main_menu()
						elif internet == "gohome" or internet == "10":
							clear()
							main_menu()
						elif internet == "exit":
							sys.exit(0)
						else:
							print ("\033[1;31mSorry, invalid command!\033[1;m")
					
					while application_menu == "5":
						clear()
						print ('''
|\033[1;36mGames\033[1;m|
1) Install Steam
2) Install VisualBoyAdvance (Gameboy Advance)
3) Install Snes9x (Super Nintendo)
4) Install Pcsxr (Play Station)
5) Back
6) Go Home
						''')
						games = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
						if games == "1":
							if os.system("sudo pacman -S steam") == 0:
								raw_input('Task Finished. Press Enter to continue')
							else:
								raw_input('Task Finished with errors. Press Enter to continue')
						elif games == "2":
							if os.system("sudo pacman -S vbam-gtk") == 0:
								raw_input('Task Finished. Press Enter to continue')
							else:
								raw_input('Task Finished with errors. Press Enter to continue')
						elif games == "3":
							if os.system("sudo pacman snes9x-gtk") == 0:
								raw_input('Task Finished. Press Enter to continue')
							else:
								raw_input('Task Finished with errors. Press Enter to continue')
						elif games == "4":
							if os.system("sudo pacman -S pcsxr") == 0:
								raw_input('Task Finished. Press Enter to continue')
							else:
								raw_input('Task Finished with errors. Press Enter to continue')
						elif games == "back" or games == "5":
							clear()
							main_menu()
						elif games == "gohome" or games == "6":
							clear()
							main_menu()
						elif games == "exit":
							sys.exit(0)
						else:
							print ("\033[1;31mSorry, invalid command!\033[1;m")
					
					if application_menu == "back" or application_menu == "7":
						clear()
						main_menu()
					if application_menu == "gohome" or application_menu == "8":
						clear()
						main_menu()

				while update_menu == "5":
					clear()
					print ('''
|\033[1;36mDEs & WMs Instalations\033[1;m|
1) DEs (Desktop Environments)
2) WMs (Window Managers)
3) Back
4) Go Home
					''')
					
					dewm_menu = raw_input("\033[1;36mMPIS > \033[1;m")
					while dewm_menu == "1":
						clear()
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
							if os.system("sudo pacman kde4") == 0:
								raw_input('Task Finished. Press Enter to continue')
							else:
								raw_input('Task Finished with errors. Press Enter to continue')
						elif de_menu == "back" or de_menu == "6":
							clear()
							main_menu()
						elif de_menu == "gohome" or de_menu == "7":
							clear()
							main_menu()
						elif de_menu == "exit":
							sys.exit(0)
						else:
							print ("\033[1;31mSorry, invalid command!\033[1;m")
							
					while dewm_menu == "2":
						clear()
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
							clear()
							main_menu()
						elif wm_menu == "gohome" or wm_menu == "5":
							clear()
							main_menu()
						elif wm_menu == "exit":
							sys.exit(0)
						else:
							print ("\033[1;31mSorry, invalid command!\033[1;m")
					
					if dewm_menu == "back" or dewm_menu == "3":
						clear()
						main_menu()
					if dewm_menu == "gohome" or dewm_menu == "4":
						clear()
						main_menu()
						
				if update_menu == "7":
				    help()
				    raw_input('Press ENTER to continue...!')
				    clear()
				if update_menu == "8":
					end_message()
					sys.exit(0)
		clear()
		main_menu()
	except KeyboardInterrupt:
		print "\nYou had press the Ctrl+C keys combination. Accepted exit request. Bye!"
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

#Cleaning screen
def clear():
  os.system("clear")

def banner():

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
 \033[1;36mManjaro GNU/Linux Script Post Instalation\033[1;m  \033[1;m                         Y8b d88P 
 \033[1;32m  Author: SniferL4bs | www.sniferl4bs.com \033[1;m                         "Y88P"  
 \033[1;32m  Author: NeoRanger  | www.neositelinux.com.ar \033[1;m
 \033[1;32m  Colaborative Blog: | http://kernelpanicblog.wordpress.com \033[1;m
 
 Application in Testing Fase, please report your bugs!"""

def end_message():
	print ('''\033[1;36m
		Thanks for choosing us, we hope you have been helpful.
		The KernelPanicBlog Team. 
		Our web: http://kernelpanicblog.wordpress.com\033[1;m ''')

def help():
	print ('''				|\033[1;36mHelp\033[1;m|
			You can write 3 commands and do a shortcut:
			back -> command for return to the previous option
			gohome -> command for return to the main menu script
			exit -> program exit
			Ctrl+C -> shortcut to finish the script execution
			''')


if __name__ == "__main__":
    main()
