#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
# This file is part of MPIS (https://github.com/KernelPanicBlog/MPIS).
#
# MPIS(Manjaro Post Installation Script) is free software; you can redistribute
# it and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the License,or
# any later version.
#
# MPIS (Manjaro Post Installation Script):
# It allows  users to choose different options such as
# install an application or CONFIG some tools and environments.
#
# MPIS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MPIS; If not, see <http://www.gnu.org/licenses/>.
# ______________________________________________________________________________
from enum import IntEnum


class Estilo(IntEnum):

    normal = 0
    negrita = 1
    subrayado = 4
    tachado = 7


class Texto(IntEnum):

    blanco = 30
    rojo = 31
    verde = 32
    amarillo = 33
    azul = 34
    morado = 35
    cian = 36
    gris = 37
    grisclaro = 38
    reset = 39
    blancoligero = 90
    rojoligero = 91
    verdeligero = 92
    amarilloligero = 93
    azulligero = 94
    moradoligero = 95
    cianligero = 96
    negroligero = 97
    grisligero = 98


class Fondo(IntEnum):

    blanco = 40
    rojo = 41
    verde = 42
    amarillo = 43
    azul = 44
    morado = 45
    cian = 46
    gris = 47
    negro = 48
    reset = 49
    blancoligero = 100
    rojoligero = 101
    verdeligero = 102
    amarilloligero = 103
    azulligero = 104
    moradoligero = 105
    cianligero = 106
    negroligero = 107


class Formato:
    """
    """
    def __init__(self):
        self.CS = "\033["
        self.CF = "1;m"

    def aplicar(self, estilo=Estilo.normal.value,
                color_texto=Texto.reset.value,
                color_fondo=Fondo.reset.value):

        return self.CS + str(estilo) + ";"\
                  + str(color_texto) + ";"\
                  + str(color_fondo) + "m"

    def reset(self):
        return self.CS + self.CF

colorize = Formato()


def main():
    string = ""
    for txt in Texto:
        for fon in Fondo:
            string += colorize.aplicar(2, txt.value, fon.value) + "{0},{1} ".format(txt, fon)
        print(string)
        string = ""


if __name__ == "__main__":

    main()
