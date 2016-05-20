#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#Script post-instalación que permitirá al usuario poder elegir diferentes
#aplicaciones a instalar y configurar algunas herramientas.

import os
import sys, traceback


def main():
	try:
		print '''

 |\033[1;36mScript Post Instalación de Manjaro GNU/Linux\033[1;m | V0.1 \033[1;m


 \033[1;32m+ -- -- +=[ Autor: SniferL4bs | Web: www.sniferl4bs.com\033[1;m
 \033[1;32m+ -- -- +=[ Autor: NeoRanger  | Web: www.neositelinux.com.ar\033[1;m

		'''
		def main_menu():
			while True:
				print '''
 |\033[1;36mMenú Principal\033[1;m|
1) Actualización del sistema
2) Instalación de aplicaciones
3) Listado de aplicaciones instaladas
4) Desinstalación de aplicaciones
5) Instalación de DE y WMs 
6) Personalización
7) Ayuda

			'''

				update_menu = raw_input("\033[1;36mLPIS > \033[1;m")
			
				while update_menu == "1":
					print '''
|\033[1;36mActualización del sistema\033[1;m|
1) Refresco de Mirrors y Keys (Solo para Manjaro)
2) Actualizar Repositorios pacman
3) Actualizar Repositorios AUR
4) Actualizar el Sistema completo
5) Limpieza de caché y paquetes huérfanos
6) Ver el contenido del archivo mirrorlist

					'''
					update = raw_input("\033[1;32mQue quiere hacer?> \033[1;m")
					if update == "1":
					    print ("Instalando llaves...")
					    cmd1 = os.system("sudo pacman -S archlinux-keyring manjaro-keyring")
					    cmd2 = os.system("sudo pacman-keys --init")
					    cmd3 = os.system("sudo pacman-keys --populate archlinux manjaro")
					    print ("LLaves instaladas")
					    print ("Actualizando Mirrors...")
					    cmd4 = os.system("sudo pacman-mirrors -g")
					    print ("Mirrors Actualizados")
					elif update == "2":
						cmd5 = os.system("sudo pacman -Syy")
					elif update == "3":
						cmd6 = os.system("sudo yaourt -Syy")
					elif update == "4":
					    cmd7 = os.system("sudo rm -f /var/lib/pacman/db.lck && sudo pacman-mirrors -g && sudo pacman -Syyuu  && sudo pacman -Suu")
					elif update == "5":
					    print ("Limpiando caché...")
					    cmd8 = os.system("sudo pacman -Sc && sudo pacman -Scc")
					    print ("Caché limpiado")
					    print ("Limpiando paquetes huérfanos...")
					    cmd9 = os.system("sudo pacman -Rsn && yaourt -Rsn ")
					    print ("Paquetes huérfanos eliminados")
					elif update == "6":
						file = open('/etc/pacman.d/mirrorlist', 'r')
						print file.read()					
					elif update == "back":
						main_menu()					
					elif update == "gohome":
						main_menu()
					else:
						print ("\033[1;31mLo siento, comando inválido!\033[1;m") 					
				
				while update_menu == "2":
					print '''
|\033[1;36mInstalación de Aplicaciones\033[1;m|
1) Ofimática
2) Multimedia
3) Desarrollo
4) Internet
5) Juegos
6) Herramientas de Seguridad (En Beta)
					'''
					application_menu = raw_input("\033[1;36mLPIS > \033[1;m")
					
					while application_menu == "1":
						print '''
|\033[1;36mOfimática\033[1;m|
1) Instalar LibreOffice
2) Instalar OpenOffice
3) Instalar WPS
4) Instalar Calligra
						'''
						ofimatic = raw_input("\033[1;32mQue quiere hacer?> \033[1;m")
						if ofimatic == "1":
							cmd10 = os.system("sudo pacman -S libreoffice-still")
						elif ofimatic == "2":
							cmd11 = os.system("sudo pacman -S openoffice")
						elif ofimatic == "3":
							cmd12 = os.system("sudo pacman -S wps-office")
						elif ofimatic == "4":
							cmd13 = os.system("sudo pacman -S calligra")
						elif ofimatic == "back":
							main_menu()
						elif ofimatic == "gohome":
							main_menu()
						else:
							print ("\033[1;31mLo siento, comando inválido!\033[1;m")
							
					while application_menu == "2":
						print '''
|\033[1;36mMultimedia\033[1;m|
1) Instalar VLC
2) Instalar Vokoscreen
3) Instalar Audacity
4) Instalar OpenShot
5) Instalar Audacious
6) Instalar SMTube
7) Instalar moc (Reproductor de música por terminal)
8) Instalar Handbrake
9) Instalar SoundJuicer
10) Instalar Clipgrab
11) Instalar Mumble
12) Instalar KODI
13) Instalar SoundConverter (GTK)
14) Instalar SoundKonverter (QT)

						'''
						multimedia = raw_input("\033[1;32mQue quiere hacer?> \033[1;m")
						if multimedia == "1":
							cmd14 = os.system("sudo pacman -S vlc")
						elif multimedia == "2":
							cmd15 = os.system("sudo pacman -S vokoscreen")
						elif multimedia == "3":
							cmd16 = os.system("sudo pacman -S audacity")
						elif multimedia == "4":
							cmd17 = os.system("sudo pacman -S openshot")
						elif multimedia == "5":
							cmd18 = os.system("sudo pacman -S audacious")
						elif multimedia == "6":
							cmd19 = os.system("sudo pacman -S smtube")
						elif multimedia == "7":
							cmd20 = os.system("sudo pacman -S moc")
						elif multimedia == "8":
							cmd21 = os.system("sudo pacman -S handbrake")
						elif multimedia == "9":
							cmd22 = os.system("sudo pacman -S sound-juicer")
						elif multimedia == "10":
							cmd23 = os.system("sudo pacman -S clipgrab")
						elif multimedia == "11":
							cmd24 = os.system("sudo pacman -S mumble")
						elif multimedia == "12":
							cmd25 = os.system("sudo pacman -S kodi")
						elif multimedia == "13":
							cmd26 = os.system("sudo pacman -S soundconverter")							
						elif multimedia == "14":
							cmd26 = os.system("sudo pacman -S soundkonverter")
						elif multimedia == "back":
							main_menu()
						elif multimedia == "gohome":
							main_menu()
						else:
							print ("\033[1;31mLo siento, comando inválido!\033[1;m")
					
					while application_menu == "3":
						print '''
|\033[1;36mDesarrollo\033[1;m|
1) Instalar Geany
2) Instalar Sublime Text 2
3) Instalar Sublime Text 3
4) Instalar Gedit
5) Instalar Eclipse
6) Instalar Android Studio
7) Instalar QtCreator
8) Instalar NinjaIDE

						'''
						development = raw_input("\033[1;32mQue quiere hacer?> \033[1;m")
						if development == "1":
							cmd27 = os.system("sudo pacman -S geany")
						elif development == "2":
							print ("Esta aplicación se encuentra en los repositorios comunitarios. Se instalará bajo su propio riesgo")
							cmd28 = os.system("yaourt -S sublime-text")
						elif development == "3":
							print ("Esta aplicación se encuentra en los repositorios comunitarios. Se instalará bajo su propio riesgo")
							cmd28 = os.system("yaourt -S sublime-text-dev")
						elif development == "4":
							cmd29 = os.system("sudo pacman -S gedit")
						elif development == "5":
							cmd30 = os.system("sudo pacman -S eclipse")
						elif development == "6":
							print ("Esta aplicación se encuentra en los repositorios comunitarios. Se instalará bajo su propio riesgo")
							cmd31 = os.system("yaourt -S android-studio")
						elif development == "7":
							cmd32 = os.system("sudo pacman -S qtcreator")
						elif development == "8":
							cmd33 = os.system("sudo pacman -S ninja-ide")
						elif development == "back":
							main_menu()
						elif development == "gohome":
							main_menu()
						else:
							print ("\033[1;31mLo siento, comando inválido!\033[1;m")
					
					while application_menu == "4":
						print '''
|\033[1;36mInternet\033[1;m|
1) Instalar Firefox
2) Instalar Google Chrome
3) Instalar Vivaldi
4) Instalar Telegram Desktop
5) Instalar Filezilla
6) Instalar Chromium
7) Instalar qBittorrent
8) Instalar UGet

						'''
						internet = raw_input("\033[1;32mQue quiere hacer?> \033[1;m")
						if internet == "1":
							cmd34 = os.system("sudo pacman -S firefox")
						elif internet == "2":
							cmd35 = os.system("sudo pacman -S google-chorme")
						elif internet == "3":
							print ("Esta aplicación se encuentra en los repositorios comunitarios. Se instalará bajo su propio riesgo")
							cmd36 = os.system("yaourt -S vivaldi")
						elif internet == "4":
							print ("Esta aplicación se encuentra en los repositorios comunitarios. Se instalará bajo su propio riesgo")
							cmd36 = os.system("yaourt -S telegram-desktop")
						elif internet == "5":
							cmd37 = os.system("sudo pacman -S filezilla")
						elif internet == "6":
							cmd38 = os.system("sudo pacman -S chromium")
						elif internet == "7":
							cmd39 = os.system("sudo pacman -S qbittorrent")
						elif internet == "8":
							cmd40 = os.system("sudo pacman -S uget")
						elif development == "back":
							main_menu()
						elif development == "gohome":
							main_menu()
						else:
							print ("\033[1;31mLo siento, comando inválido!\033[1;m")
					
					while application_menu == "5":
						print '''
|\033[1;36mJuegos\033[1;m|
1) Instalar Steam
2) Instalar VisualBoyAdvance (Gameboy Advance)
3) Instalar Snes9x (Super Nintendo)
4) Instalar Pcsxr (Play Station)
						'''
						games = raw_input("\033[1;32mQue quiere hacer?> \033[1;m")
						if games == "1":
							cmd41 = os.system("sudo pacman -S steam")
						elif games == "2":
							cmd42 = os.system("sudo pacman -S vbam-gtk")
						elif games == "3":
							cmd43 = os.system("sudo pacman snes9x-gtk")
						elif games == "4":
							cmd44 = os.system("sudo pacman -S pcsxr")
						elif development == "back":
							main_menu()
						elif development == "gohome":
							main_menu()
						else:
							print ("\033[1;31mLo siento, comando inválido!\033[1;m")
							
				while update_menu == "5":
					print '''
|\033[1;36mInstalación de DEs y WMs\033[1;m|
1) DEs (Desktop Environments)
2) WMs (Window Managers)
					'''
					
					dewm_menu = raw_input("\033[1;36mLPIS > \033[1;m")
					while dewm_menu == "1":
						print '''
|\033[1;36mDesktop Environmets\033[1;m|
1) Instalar XFCE
2) Instalar Gnome-Shell
3) Instalar LXDE
4) Instalar Plasma 5
5) Instalar KDE
						'''
						de_menu = raw_input("\033[1;32mQue quiere hacer?> \033[1;m")
						if de_menu == "1":
							cmd45 = os.system("sudo pacman -S xfce4")
						elif de_menu == "2":
							cmd46 = os.system("sudo pacman -S gnome-shell")
						elif de_menu == "3":
							cmd47 = os.system("sudo pacman -S lxde")
						elif de_menu == "4":
							cmd48 = os.system("sudo pacman -S plasma5")
						elif de_menu == "5":
							cmd49 = os.system("sudo pacman kde4")
						elif development == "back":
							main_menu()
						elif development == "gohome":
							main_menu()
						else:
							print ("\033[1;31mLo siento, comando inválido!\033[1;m")
							
					while dewm_menu == "2":
						print '''
|\033[1;36mWindow Managers\033[1;m|
1) Instalar i3-wm
2) Instalar Openbox
3) Instalar Fluxbox
						'''
						wm_menu = raw_input("\033[1;32mQue quiere hacer?> \033[1;m")
						if wm_menu == "1":
							cmd50 = os.system("sudo pacman -S i3-wm")
						elif wm_menu == "2":
							cmd51 = os.system("sudo pacman -S openbox")
						elif wm_menu == "3":
							cmd52 = os.system("sudo pacman -S fluxbox")
						elif development == "back":
							main_menu()
						elif development == "gohome":
							main_menu()
						else:
							print ("\033[1;31mLo siento, comando inválido!\033[1;m")
						
				if update_menu == "7":
				    print '''
|\033[1;36mAyuda\033[1;m|
Una vez elegida la opción deseada tiene la posibilidad de escribir 3 comandos:
back -> comando para volver a la opción anterior
gohome -> comando para volver al menú principal del script
Ctrl+C -> combinación de teclas para terminar la ejecución del script
'''
						
		main_menu()
	except KeyboardInterrupt:
		print "Solicitud de Salida aceptada. Adiós!"
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()