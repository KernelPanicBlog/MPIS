import os
import sys, traceback
import mpis

def games():
	print ('''
|\033[1;36mGames\033[1;m|
1) Install Steam
2) Install VisualBoyAdvance (Gameboy Advance)
3) Install Snes9x (Super Nintendo)
4) Install Pcsxr (Play Station)
5) Install Pcsxr2 (Play Station 2)
6) Install PPSSPP (PSP)
7) Install DeSmuME (Nintendo DS)
8) Install Stella (Atari)
9) Install Fceux
10) Install Yabause
11) Back
12) Go Home
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
		if os.system("sudo pacman -S snes9x-gtk") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif games == "4":
		if os.system("sudo pacman -S pcsxr") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif games == "5":
		if os.system("sudo pacman -S pcsxr2") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif games == "6":
		if os.system("sudo pacman -S ppsspp") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif games == "7":
		if os.system("sudo pacman -S desmume") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif games == "8":
		if os.system("sudo pacman -S stella") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif games == "9":
		if os.system("sudo pacman -S fceux") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif games == "10":
		if os.system("sudo pacman -S yabause") == 0:
			raw_input('Task Finished. Press Enter to continue')
		else:
			raw_input('Task Finished with errors. Press Enter to continue')
	elif games == "back" or games == "11":
		mpis.clear()
		main_menu()
	elif games == "gohome" or games == "12":
		mpis.clear()
		main_menu()
	elif games == "exit":
		sys.exit(0)
	else:
		print ("\033[1;31mSorry, invalid command!\033[1;m")