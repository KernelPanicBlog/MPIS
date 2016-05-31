#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
#
#Manjaro script post-instalation that allow to the users to choose different options
#such as install an application or config some tools and environments.

import os
import sys, traceback
import update_system_menu
import ofimatic_menu
import multimedia_menu
import dev_menu
import internet_menu
import games_menu
import wm_menu
import de_menu
import systools

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
3) List applications installed (not functional yet)
4) Uninstall applications (not functional yet)
5) Install DEs & WMs 
6) Personalitation (not functional yet)
7) Help
8) Exit
''')
				main_menu1 = raw_input("\033[1;36mMPIS > \033[1;m")
				clear()
				while main_menu1 == "1":
					clear()
					update_system()
				
				while main_menu1 == "2":
					clear()
					print ('''
|\033[1;36mInstall Applications\033[1;m|
1) Ofimatic
2) Multimedia
3) Development
4) Internet
5) Games
6) System Tools
7) Back
8) Go Home
					''')
					application_menu = raw_input("\033[1;36mMPIS > \033[1;m")
					
					while application_menu == "1":
						clear()
						ofimatic_menu()
					while application_menu == "2":
						clear()
						multimedia_menu()
					while application_menu == "3":
						clear()
						dev_menu()
					while application_menu == "4":
						clear()
						internet_menu()
					while application_menu == "5":
						clear()
						games_menu()
					while application_menu == "6":
						clear()
						systools()
					# Option Back and Go Home from Applications Menu
					if application_menu == "back" or application_menu == "7":
						clear()
						main_menu()
					if application_menu == "gohome" or application_menu == "8":
						clear()
						main_menu()

				while main_menu1 == "5":
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
						de_menu.de()
					while dewm_menu == "2":
						clear()
						wm_menu.wm()
    				if dewm_menu == "back" or dewm_menu == "3":
    					clear()
    					main_menu()
    				if dewm_menu == "gohome" or dewm_menu == "4":
    					clear()
    					main_menu()

					# Option Back and Go Home from Main Menu
				if main_menu1 == "7":
				    help()
				    raw_input('Press ENTER to continue...!')
				    clear()
				if main_menu1 == "8":
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
