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
		raw_input('Press ENTER to continue...!')
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
2) pacman repositories update
3) AUR repositories update
4) Update all system
5) Clear cache and orphan packages
6) See the content of mirrorlist file

					''')
					update = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
					if update == "1":
					    print ("Installing keys...")
					    cmd1 = os.system("sudo pacman -S archlinux-keyring manjaro-keyring")
					    cmd2 = os.system("sudo pacman-keys --init")
					    cmd3 = os.system("sudo pacman-keys --populate archlinux manjaro")
					    print ("Keys instaled")
					    print ("Updating Mirrors...")
					    cmd4 = os.system("sudo pacman-mirrors -g")
					    print ("Mirrors Updated")
					    raw_input('Task Finished. Press Enter to continue')
					elif update == "2":
						cmd5 = os.system("sudo pacman -Syy")
						raw_input('Task Finished. Press Enter to continue')
					elif update == "3":
						cmd6 = os.system("yaourt -Syy")
						raw_input('Task Finished. Press Enter to continue')
					elif update == "4":
					    cmd7 = os.system("sudo rm -f /var/lib/pacman/db.lck && sudo pacman-mirrors -g && sudo pacman -Syyuu  && sudo pacman -Suu")
					    raw_input('Task Finished. Press Enter to continue')
					elif update == "5":
					    print ("Cleaning caché...")
					    cmd8 = os.system("sudo pacman -Sc && sudo pacman -Scc")
					    print ("Cache cleared")
					    print ("Cleaning orphan packages...")
					    cmd9 = os.system("sudo pacman -Rsn && yaourt -Rsn ")
					    print ("Orphan packages cleared")
					    raw_input('Task Finished. Press Enter to continue')
					elif update == "6":
						file = open('/etc/pacman.d/mirrorlist', 'r')
						print file.read()					
					elif update == "back":
						main_menu()					
					elif update == "gohome":
						main_menu()
					elif update == "exit":
						cmdexit = sys.exit(0)
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
6) Hacking Tools (En Beta)
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
						''')
						ofimatic = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
						if ofimatic == "1":
							cmd10 = os.system("sudo pacman -S libreoffice-still")
							raw_input('Task Finished. Press Enter to continue')
						elif ofimatic == "2":
							cmd11 = os.system("sudo pacman -S openoffice")
							raw_input('Task Finished. Press Enter to continue')
						elif ofimatic == "3":
							print ("This application is on the AUR repository (community). It is installed at your own risk.")
							cmd12 = os.system("yaourt -S wps-office")
							raw_input('Task Finished. Press Enter to continue')
						elif ofimatic == "4":
							cmd13 = os.system("sudo pacman -S calligra")
							raw_input('Task Finished. Press Enter to continue')
						elif ofimatic == "back":
							main_menu()
						elif ofimatic == "gohome":
							main_menu()
						elif ofimatic == "exit":
							cmdexit = sys.exit(0)
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

						''')
						multimedia = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
						if multimedia == "1":
							cmd14 = os.system("sudo pacman -S vlc")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "2":
							print ("This application is on the AUR repository (community). It is installed at your own risk.")
							cmd15 = os.system("yaourt -S vokoscreen")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "3":
							cmd16 = os.system("sudo pacman -S audacity")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "4":
							cmd17 = os.system("sudo pacman -S openshot")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "5":
							cmd18 = os.system("sudo pacman -S audacious")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "6":
							cmd19 = os.system("sudo pacman -S smtube")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "7":
							cmd20 = os.system("sudo pacman -S moc")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "8":
							cmd21 = os.system("sudo pacman -S handbrake")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "9":
							cmd22 = os.system("sudo pacman -S sound-juicer")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "10":
							cmd23 = os.system("sudo pacman -S clipgrab")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "11":
							cmd24 = os.system("sudo pacman -S mumble")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "12":
							cmd25 = os.system("sudo pacman -S kodi")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "13":
							cmd26 = os.system("sudo pacman -S soundconverter")
							raw_input('Task Finished. Press Enter to continue')				
						elif multimedia == "14":
							cmd26 = os.system("sudo pacman -S soundkonverter")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "15":
							cmd26 = os.system("sudo pacman -S youtube-dl")
							raw_input('Task Finished. Press Enter to continue')
						elif multimedia == "back":
							main_menu()
						elif multimedia == "gohome":
							main_menu()
						elif multimedia == "exit":
							cmdexit = sys.exit(0)
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

						''')
						development = raw_input("\033[1;32mWhat you want to do??> \033[1;m")
						if development == "1":
							cmd27 = os.system("sudo pacman -S geany")
						elif development == "2":
							print ("This application is on the AUR repository (community). It is installed at your own risk.")
							cmd28 = os.system("yaourt -S sublime-text")
							raw_input('Task Finished. Press Enter to continue')
						elif development == "3":
							print ("This application is on the AUR repository (community). It is installed at your own risk.")
							cmd28 = os.system("yaourt -S sublime-text-dev")
							raw_input('Task Finished. Press Enter to continue')
						elif development == "4":
							cmd29 = os.system("sudo pacman -S gedit")
							raw_input('Task Finished. Press Enter to continue')
						elif development == "5":
							cmd30 = os.system("sudo pacman -S eclipse")
							raw_input('Task Finished. Press Enter to continue')
						elif development == "6":
							print ("This application is on the AUR repository (community). It is installed at your own risk.")
							cmd31 = os.system("yaourt -S android-studio")
							raw_input('Task Finished. Press Enter to continue')
						elif development == "7":
							cmd32 = os.system("sudo pacman -S qtcreator")
							raw_input('Task Finished. Press Enter to continue')
						elif development == "8":
							cmd33 = os.system("sudo pacman -S ninja-ide")
							raw_input('Task Finished. Press Enter to continue')
						elif development == "back":
							main_menu()
						elif development == "gohome":
							main_menu()
						elif development == "exit":
							cmdexit = sys.exit(0)
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

						''')
						internet = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
						if internet == "1":
							cmd34 = os.system("sudo pacman -S firefox")
							raw_input('Task Finished. Press Enter to continue')
						elif internet == "2":
							print ("This application is on the AUR repository (community). It is installed at your own risk.")
							cmd35 = os.system("yaourt -S google-chrome")
							raw_input('Task Finished. Press Enter to continue')
						elif internet == "3":
							print ("This application is on the AUR repository (community). It is installed at your own risk.")
							cmd36 = os.system("yaourt -S vivaldi")
							raw_input('Task Finished. Press Enter to continue')
						elif internet == "4":
							print ("This application is on the AUR repository (community). It is installed at your own risk.")
							print ("What is your architecture?:")
							optele = raw_input("1) 32 Bits 2) 64 Bits")
							if optele == "1":
								optele32_1 = os.system("wget -c https://tdesktop.com/linux32")
								optele32_2 = os.system("tar xvf linux32")
								optele32_3 = os.system("sudo mv Telegram /opt/telegram")
								optele32_4 = os.system("./opt/telegram/Telegram")
							if optele == "2":
								optele32_1 = os.system("wget -c https://tdesktop.com/linux")
								optele32_2 = os.system("tar xvf linux")
								optele32_3 = os.system("sudo mv Telegram /opt/telegram")
								optele32_4 = os.system("./opt/telegram/Telegram")
							raw_input('Task Finished. You have tu close Telegram to continue. Press Enter to continue')
						elif internet == "5":
							cmd37 = os.system("sudo pacman -S filezilla")
							raw_input('Task Finished. Press Enter to continue')
						elif internet == "6":
							cmd38 = os.system("sudo pacman -S chromium")
							raw_input('Task Finished. Press Enter to continue')
						elif internet == "7":
							cmd39 = os.system("sudo pacman -S qbittorrent")
							raw_input('Task Finished. Press Enter to continue')
						elif internet == "8":
							cmd40 = os.system("sudo pacman -S uget")
							raw_input('Task Finished. Press Enter to continue')
						elif internet == "back":
							main_menu()
						elif internet == "gohome":
							main_menu()
						elif internet == "exit":
							cmdexit = sys.exit(0)
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
						''')
						games = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
						if games == "1":
							cmd41 = os.system("sudo pacman -S steam")
							raw_input('Task Finished. Press Enter to continue')
						elif games == "2":
							cmd42 = os.system("sudo pacman -S vbam-gtk")
							raw_input('Task Finished. Press Enter to continue')
						elif games == "3":
							cmd43 = os.system("sudo pacman snes9x-gtk")
							raw_input('Task Finished. Press Enter to continue')
						elif games == "4":
							cmd44 = os.system("sudo pacman -S pcsxr")
							raw_input('Task Finished. Press Enter to continue')
						elif games == "back":
							main_menu()
						elif games == "gohome":
							main_menu()
						elif games == "exit":
							cmdexit = sys.exit(0)
						else:
							print ("\033[1;31mSorry, invalid command!\033[1;m")

				while update_menu == "5":
					clear()
					print ('''
|\033[1;36mDEs & WMs Instalations\033[1;m|
1) DEs (Desktop Environments)
2) WMs (Window Managers)
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
						''')
						de_menu = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
						if de_menu == "1":
							cmd45 = os.system("sudo pacman -S xfce4")
							raw_input('Task Finished. Press Enter to continue')
						elif de_menu == "2":
							cmd46 = os.system("sudo pacman -S gnome-shell")
							raw_input('Task Finished. Press Enter to continue')
						elif de_menu == "3":
							cmd47 = os.system("sudo pacman -S lxde")
							raw_input('Task Finished. Press Enter to continue')
						elif de_menu == "4":
							cmd48 = os.system("sudo pacman -S plasma5")
							raw_input('Task Finished. Press Enter to continue')
						elif de_menu == "5":
							cmd49 = os.system("sudo pacman kde4")
							raw_input('Task Finished. Press Enter to continue')
						elif de_menu == "back":
							main_menu()
						elif de_menu == "gohome":
							main_menu()
						elif de_menu == "exit":
							cmdexit = sys.exit(0)
						else:
							print ("\033[1;31mSorry, invalid command!\033[1;m")
							
					while dewm_menu == "2":
						clear()
						print ('''
|\033[1;36mWindow Managers\033[1;m|
1) Install i3-wm
2) Install Openbox
3) Install Fluxbox
						''')
						wm_menu = raw_input("\033[1;32mWhat you want to do?> \033[1;m")
						if wm_menu == "1":
							cmd50 = os.system("sudo pacman -S i3-wm")
							raw_input('Task Finished. Press Enter to continue')
						elif wm_menu == "2":
							cmd51 = os.system("sudo pacman -S openbox")
							raw_input('Task Finished. Press Enter to continue')
						elif wm_menu == "3":
							cmd52 = os.system("sudo pacman -S fluxbox")
							raw_input('Task Finished. Press Enter to continue')
						elif wm_menu == "back":
							main_menu()
						elif wm_menu == "gohome":
							main_menu()
						elif wm_menu == "exit":
							cmdexit = sys.exit(0)
						else:
							print ("\033[1;31mSorry, invalid command!\033[1;m")
						
				if update_menu == "7":
				    print ('''
|\033[1;36mHelp\033[1;m|
After selecting the desired option has the ability to write 3 commands and a shortcut:
back -> command for return to the previous option
gohome -> command for return to the main menu script
exit -> program exit
Ctrl+C -> shortcut to finish the script execution
''')
				if update_menu == "8":
					print ('''
Thanks for choosing us, we hope you have been helpful.
The KernelPanicBlog Team.
Our web: http://kernelpanicblog.wordpress.com
					''')
					cmdexit = sys.exit(0)
		clear()
		main_menu()
	except KeyboardInterrupt:
		print "You had press the Ctrl+C keys combination. Accepted exit request. Bye!"
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
 \033[1;36mScript Post Instalation Manjaro GNU/Linux\033[1;m  \033[1;m                         Y8b d88P 
 \033[1;32m  Author: SniferL4bs | www.sniferl4bs.com \033[1;m                         "Y88P"  
 \033[1;32m  Author: SniferL4bs | www.neositelinux.com.ar \033[1;m
 
 Application in Testing Fase, please report your bugs!"""

if __name__ == "__main__":
    main()
