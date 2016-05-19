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

 |\033[1;36mScript Post Instalación de GNU/Linux\033[1;m | V0.1 \033[1;m


 \033[1;32m+ -- -- +=[ Autor: SniferL4bs | Web: www.sniferl4bs.com\033[1;m
 \033[1;32m+ -- -- +=[ Autor: NeoRanger  | Web: www.neositelinux.com.ar\033[1;m

		'''
		def inicio1():
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

				opcion0 = raw_input("\033[1;36mLPIS > \033[1;m")
			
				while opcion0 == "1":
					print '''
|\033[1;36mActualización del sistema\033[1;m|
1) Refresco de Mirrors y Keys (Solo para Manjaro)
2) Actualizar Repositorios pacman
3) Actualizar Repositorios AUR
4) Actualizar el Sistema completo
5) Limpieza de caché y paquetes huérfanos
6) Ver el contenido del archivo mirrorlist

					'''
					repo = raw_input("\033[1;32mQue quiere hacer?> \033[1;m")
					if repo == "1":
					    print ("Instalando llaves...")
					    cmd1 = os.system("sudo pacman -S archlinux-keyring manjaro-keyring")
					    cmd2 = os.system("sudo pacman-keys --init")
					    cmd3 = os.system("sudo pacman-keys --populate archlinux manjaro")
					    print ("LLaves instaladas")
					    print ("Actualizando Mirrors...")
					    cmd4 = os.system("sudo pacman-mirrors -g")
					    print ("Mirrors Actualizados")
					elif repo == "2":
						cmd5 = os.system("sudo pacman -Syy")
					elif repo == "3":
						cmd6 = os.system("sudo yaourt -Syy")
					elif repo == "4":
					    cmd7 = os.system("sudo rm -f /var/lib/pacman/db.lck && sudo pacman-mirrors -g && sudo pacman -Syyuu  && sudo pacman -Suu")
					elif repo == "5":
					    print ("Limpiando caché...")
					    cmd8 = os.system("sudo pacman -Sc && sudo pacman -Scc")
					    print ("Caché limpiado")
					    print ("Limpiando paquetes huérfanos...")
					    cmd9 = os.system("sudo pacman -Rsn && yaourt -Rsn ")
					    print ("Paquetes huérfanos eliminados")
					elif repo == "6":
						file = open('/etc/pacman.d/mirrorlist', 'r')
						print file.read()					
					elif repo == "back":
						inicio1()					
					elif repo == "gohome":
						inicio1()
					else:
						print ("\033[1;31mLo siento, comando inválido!\033[1;m") 					
				
				while opcion0 == "2":
					print '''
|\033[1;36mInstalación de Aplicaciones\033[1;m|
1) Ofimática
2) Multimedia
3) Desarrollo
4) Internet
5) Juegos
6) Herramientas de Seguridad (En Beta)
					'''
					opcion1 = raw_input("\033[1;36mLPIS > \033[1;m")
					
					while opcion1 == "1":
						print '''
|\033[1;36mOfimática\033[1;m|
1) Instalar LibreOffice
2) Instalar OpenOffice
3) Instalar WPS
4) Instalar Calligra
						'''
						apps0 = raw_input("\033[1;32mQue quiere hacer?> \033[1;m")
						if apps0 == "1":
							cmd10 = os.system("sudo pacman -S libreoffice-still")
						elif apps0 == "2":
							cmd11 = os.system("sudo pacman -S openoffice")
						elif apps0 == "3":
							cmd12 = os.system("sudo pacman -S wps-office")
						elif apps0 == "4":
							cmd13 = os.system("sudo pacman -S calligra")
						elif apps0 == "back":
							inicio1()
						elif apps0 == "gohome":
							inicio1()
						else:
							print ("\033[1;31mLo siento, comando inválido!\033[1;m")
							
					while opcion1 == "2":
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
						apps1 = raw_input("\033[1;32mQue quiere hacer?> \033[1;m")
						if apps1 == "1":
							cmd14 = os.system("sudo pacman -S vlc")
						elif apps1 == "2":
							cmd15 = os.system("sudo pacman -S vokoscreen")
						elif apps1 == "3":
							cmd16 = os.system("sudo pacman -S audacity")
						elif apps1 == "4":
							cmd17 = os.system("sudo pacman -S openshot")
						elif apps1 == "5":
							cmd18 = os.system("sudo pacman -S audacious")
						elif apps1 == "6":
							cmd19 = os.system("sudo pacman -S smtube")
						elif apps1 == "7":
							cmd20 = os.system("sudo pacman -S moc")
						elif apps1 == "8":
							cmd21 = os.system("sudo pacman -S handbrake")
						elif apps1 == "9":
							cmd22 = os.system("sudo pacman -S sound-juicer")
						elif apps1 == "10":
							cmd23 = os.system("sudo pacman -S clipgrab")
						elif apps1 == "11":
							cmd24 = os.system("sudo pacman -S mumble")
						elif apps1 == "12":
							cmd25 = os.system("sudo pacman -S kodi")
						elif apps1 == "13":
							cmd26 = os.system("sudo pacman -S soundconverter")							
						elif apps1 == "14":
							cmd26 = os.system("sudo pacman -S soundkonverter")
						elif apps1 == "back":
							inicio1()
						elif apps1 == "gohome":
							inicio1()
						else:
							print ("\033[1;31mLo siento, comando inválido!\033[1;m")
					
					while opcion1 == "3":
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
						apps2 = raw_input("\033[1;32mQue quiere hacer?> \033[1;m")
						if apps2 == "1":
							cmd27 = os.system("sudo pacman -S geany")
						elif apps2 == "2":
							print ("Esta aplicación se encuentra en los repositorios comunitarios. Se instalará bajo su propio riesgo")
							cmd28 = os.system("yaourt -S sublime-text")
						elif apps2 == "3":
							print ("Esta aplicación se encuentra en los repositorios comunitarios. Se instalará bajo su propio riesgo")
							cmd28 = os.system("yaourt -S sublime-text-dev")
						elif apps2 == "4":
							cmd29 = os.system("sudo pacman -S gedit")
						elif apps2 == "5":
							cmd30 = os.system("sudo pacman -S eclipse")
						elif apps2 == "6":
							print ("Esta aplicación se encuentra en los repositorios comunitarios. Se instalará bajo su propio riesgo")
							cmd31 = os.system("yaourt -S android-studio")
						elif apps2 == "7":
							cmd32 = os.system("sudo pacman -S qtcreator")
						elif apps2 == "8":
							cmd33 = os.system("sudo pacman -S ninja-ide")
						elif apps2 == "back":
							inicio1()
						elif apps2 == "gohome":
							inicio1()
						else:
							print ("\033[1;31mLo siento, comando inválido!\033[1;m")
					
					while opcion1 == "4":
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
						apps3 = raw_input("\033[1;32mQue quiere hacer?> \033[1;m")
						if apps3 == "1":
							cmd34 = os.system("sudo pacman -S firefox")
						elif apps3 == "2":
							cmd35 = os.system("sudo pacman -S google-chorme")
						elif apps3 == "3":
							print ("Esta aplicación se encuentra en los repositorios comunitarios. Se instalará bajo su propio riesgo")
							cmd36 = os.system("yaourt -S vivaldi")
						elif apps3 == "4":
							print ("Esta aplicación se encuentra en los repositorios comunitarios. Se instalará bajo su propio riesgo")
							cmd36 = os.system("yaourt -S telegram-desktop")
						elif apps3 == "5":
							cmd37 = os.system("sudo pacman -S filezilla")
						elif apps3 == "6":
							cmd38 = os.system("sudo pacman -S chromium")
						elif apps3 == "7":
							cmd39 = os.system("sudo pacman -S qbittorrent")
						elif apps3 == "8":
							cmd40 = os.system("sudo pacman -S uget")
						
						
				if opcion0 == "7":
				    print '''
|\033[1;36mAyuda\033[1;m|
Una vez elegida la opción deseada tiene la posibilidad de escribir 3 comandos:
back -> comando para volver a la opción anterior
gohome -> comando para volver al menú principal del script
Ctrl+C -> combinación de teclas para terminar la ejecución del script
'''
						
		inicio1()
	except KeyboardInterrupt:
		print "Solicitud de Salida aceptada. Adiós!"
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()