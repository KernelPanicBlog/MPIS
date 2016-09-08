#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of MPIS (https://github.com/KernelPanicBlog/MPIS).
#
# MPIS(Manjaro Post Installation Script) is free software; you can redistribute
# it and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the License,
# or any later version.
#
# MPIS (Manjaro Post Installation Script):
# It allows  users to choose different options such as
# install an application or config some tools and environments.
#
# MPIS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MPIS; If not, see <http://www.gnu.org/licenses/>.

###############################################################################
# PACKAGES
###############################################################################
PACKAGES = {
    "{} Office still":          ["pacman", "Office", ["libreoffice-still"]],
    "{} Office Fresh":          ["pacman", "Office", ["libreoffice-fresh"]],
    "{} OpenOffice":            ["pacman", "Office", ["openoffice"]],
    "{} WPS":                   ["yaourt", "Office", ["wps-office"]],
    "{} Calligra":              ["pacman", "Office", ["calligra"]],
    "{} VLC":                   ["pacman", "Multimedia", ["vlc"]],
    "{} VokoScreen":            ["yaourt", "Multimedia", ["vokoscreen"]],
    "{} OBS Studio":            ["pacman", "Multimedia", ["obs-studio"]],
    "{} audacity":              ["pacman", "Multimedia", ["audacity"]],
    "{} openshot":              ["pacman", "Multimedia", ["openshot"]],
    "{} audacious":             ["pacman", "Multimedia", ["audacious"]],
    "{} smtube":                ["pacman", "Multimedia", ["smtube"]],
    "{} moc":                   ["pacman", "Multimedia", ["moc"]],
    "{} handbrake":             ["pacman", "Multimedia", ["handbrake"]],
    "{} soundjuicer":           ["pacman", "Multimedia", ["sound-juicer"]],
    "{} clipgrab":              ["pacman", "Multimedia", ["clipgrab"]],
    "{} mumble":                ["pacman", "Multimedia", ["mumble"]],
    "{} kodi":                  ["pacman", "Multimedia", ["kodi"]],
    "{} Sound Converter GTK":   ["pacman", "Multimedia", ["soundconverter"]],
    "{} Sound Converter QT":    ["pacman", "Multimedia", ["soundkonverter"]],
    "{} youtube-dl":            ["pacman", "Multimedia", ["youtube-dl"]],
    "{} mpv":                   ["pacman", "Multimedia", ["mpv"]],
    "{} Simple Screen Recorder":["yaourt", "Multimedia", ["simplescreenrecorder"]],
    "{} totem":                 ["pacman", "Multimedia", ["totem"]],
    "{} geany":                 ["pacman", "Development", ["geany"]],
    "{} sublime text":          ["yaourt", "Development", ["sublime-text"]],
    "{} sublime text 3":        ["yaourt", "Development", ["sublime-text-dev"]],
    "{} gedit":                 ["pacman", "Development", ["gedit"]],
    "{} eclipse":               ["pacman", "Development", ["eclipse"]],
    "{} Android Studio":        ["yaourt", "Development", ["android-studio"]],
    "{} Qtcreator":             ["pacman", "Development", ["qtcreator"]],
    "{} ninja-ide":             ["pacman", "Development", ["ninja-ide"]],
    "{} Google Chrome":         ["yaourt", "Internet", ["google-chrome"]],
    "{} Vivaldi":               ["yaourt", "Internet", ["vivaldi"]],
    "{} filezilla":             ["pacman", "Internet", ["filezilla"]],
    "{} chromium":              ["pacman", "Internet", ["chromium"]],
    "{} qbittorrent":           ["pacman", "Internet", ["qbittorrent"]],
    "{} uget":                  ["pacman", "Internet", ["uget"]],
    "{} steam":                 ["pacman", "Games", ["steam-manjaro"]],
    "{} VisualBoyAdvance (Gameboy Advance)":
                                ["pacman", "Games",  ["vbam-gtk"]],
    "{} snes9x (Super Nintendo)":
                                ["pacman", "Games", ["snes9x-gtk"]],
    "{} pcsxr (Play Station)":  ["pacman", "Games", ["pcsxr"]],
    "{} pcsx2 (Play Station 2)":["pacman", "Games", ["pcsx2"]],
    "{} ppsspp (PSP)":          ["pacman", "Games", ["ppsspp"]],
    "{} DesmuME (Nintendo DS)": ["pacman", "Games", ["desmume"]],
    "{} stella (Atari)":        ["pacman", "Games", ["stella"]],
    "{} Fceux":                 ["pacman", "Games", ["ceux"]],
    "{} Yabause (GTK)":         ["pacman", "Games", ["yabause-gtk"]],
    "{} Yabause (QT)":          ["pacman", "Games", ["yabause-qt"]],
    "{} Terminator":            ["pacman", "System Tools", ["terminator"]],
    "{} Manjaro Settings Manager":
                                ["pacman", "System Tools", ["manjaro-settings-manager"]],
    "{} virtualbox":            ["pacman", "System Tools", ["virtualbox"]],
    "{} pamac":                 ["pacman", "System Tools", ["pamac"]],
    "{} LXDE":                  ["pacman", "DEs", ["lxde"]],
    "{} Plasma":                ["pacman", "DEs", ["plasma5"]],
    "{} telegram": ["web", "Internet", ["wget -c https://tdesktop.com/linux{}",
                                        "tar xvf linux{}",
                                        "sudo mv Telegram /opt/telegram",
                                        "rm -r linux{}"]],
    "{} Manjaro Settings Manager Plasma":
        ["pacman", "System Tools", ["manjaro-settings-manager",
                                    "manjaro-settings-manager-kcm",
                                    "manjaro-settings-manager-knotifier"]],
    "{} Octopi":       ["pacman", "System Tools", ["octopi",
                                                   "octopi-notifier"]],
    "{} xfce":         ["pacman", "DEs", ["xfce4",
                                          "xfce4-goodies"]],
    "{} gnome-shell":  ["pacman", "DEs", ["gnome-shell",
                                          "gnome-shell-extensions"]],
    "{} i3-wm":        ["pacman", "WMs", ["i3-wm",
                                          "i3lock",
                                          "i3status"]],
    "{} openbox":      ["pacman", "WMs", ["openbox",
                                          "oblogout",
                                          "obconf",
                                          "obmenu",
                                          "openbox-themes"]],
    "{} fluxbox":      ["pacman", "WMs", ["fluxbox",
                                          "fbnews",
                                          "fluxter"]]
}

ACTIONS = {
    "Install": "-S",
    "Uninstall": "-R"
}

ALIAS = {
    "Clear cache and orphan packages": [
        "sudo pacman -Sc",
        "sudo pacman -Scc",
        "sudo pacman -Rsn",
        "yaourt -Rsn"
    ],
    "List packages installed": [
        "pacman -Qe"
    ],
    "See the content of mirrorlist file": [
        "more /etc/pacman.d/mirrorlist"
    ],
    "See README File": [
        "more /usr/share/mpis/README.rst"
    ],
    "See CHANGELOG File": [
        "more /usr/share/mpis/CHANGELOG.rst"
    ],
    "Refresh Mirrors and Keys": [
        "sudo pacman -S archlinux-keyring manjaro-keyring",
        "sudo pacman-key --init",
        "sudo pacman-key --populate archlinux manjaro",
        "sudo pacman-mirrors -g",
    ],
    "Pacman repositories update": [
        "sudo pacman -Syy"
    ],
    "AUR repositories update": [
        "yaourt -Syy"
    ],
    "Update all system": [
        "sudo rm -f /var/lib/pacman/db.lck",
        "sudo pacman - Syyuu",
        "sudo pacman - Suu"
    ],
    "Update all system and refresh mirrors": [
        "sudo rm -f /var/lib/pacman/db.lck",
        "sudo pacman - mirrors - g",
        "sudo pacman - Syyuu",
        "sudo pacman - Suu"
    ]
}
###############################################################################
# Funciones
###############################################################################


def get_packages(name_pack):

    global PACKAGES

    return PACKAGES.get(name_pack)


def get_alias(name_alias):

    global ALIAS

    return ALIAS.get(name_alias)


def get_action(name_action):

    global ACTIONS

    return ACTIONS.get(name_action)


def get_category(name_category, name_padre):
    global PACKAGES
    _categoty = []
    prefix = name_padre.split()

    for key in PACKAGES.keys():
        package = PACKAGES[key]
        if package[1] == name_category:
            _categoty.append((key.format(prefix[0]), False))

    return _categoty
