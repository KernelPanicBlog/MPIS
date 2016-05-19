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

 |\033[1;36mGNU/Linux Script Post Instalación de GNU/Linux\033[1;m | V1.0 \033[1;m


 \033[1;32m+ -- -- +=[ Autor: SniferL4bs | Web: www.sniferl4bs.com\033[1;m
 \033[1;32m+ -- -- +=[ Autor: NeoRanger  | Web: www.neositelinux.com.ar\033[1;m

		'''
		def inicio1():
			while True:
				print '''
1) Actualización del sistema
2) Instalación de aplicaciones
3) Listado de aplicaciones instaladas
4) Desinstalación de aplicaciones
5) Instalacion de DE y WMs 
6) Personalización
7) Ayuda

			'''

				opcion0 = raw_input("\033[1;36LPIS > \033[1;m")
			
				while opcion0 == "1":
					print '''
1) Refresco de Mirrors y Keys (Solo para Manjaro)
2) Actualizar Repositorios pacman
3) Actualizar Repositorios AUR
4) Actualizar el Sistema completo
5) View the contents of sources.list file

					'''
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
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
						cmd5 = os.system("sudo pacman -Sy")
					elif repo == "3":
						cmd6 = os.system("sudo yaourt -Sy")
					elif repo == "4":
					    cmd7 = os.system("sudo rm -f /var/lib/pacman/db.lck && sudo pacman-mirrors -g && sudo pacman -Syyuu  && sudo pacman -Suu")
					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					elif repo == "5":
						file = open('/etc/pacman.d/mirrorlist', 'r')
						print file.read()
					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					
						
		inicio1()
	except KeyboardInterrupt:
		print "Solicitud de Salida aceptada. Adios!"
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()