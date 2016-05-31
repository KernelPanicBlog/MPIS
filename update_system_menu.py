import os
import sys, traceback
import mpis

def update_system():
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
		if os.system("sudo pacman -S archlinux-keyring manjaro-keyring") == 0:
			if os.system("sudo pacman-keys --init") == 0:
				if os.system("sudo pacman-keys --populate archlinux manjaro") == 0:
					print ("Keys instaled")
					print ("Updating Mirrors...")
					if os.system("sudo pacman-mirrors -g") == 0:
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
								raw_input('Task Finished. Press Enter to continue')
							else:
								raw_input('Task Finished with errors. Press Enter to continue')
								print ("Cleaning orphan packages...")
							if os.system("sudo pacman -Rsn && yaourt -Rsn ") == 0:
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