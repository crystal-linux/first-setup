# done.py
#
# Copyright 2022 mirkobrombin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundationat version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
from gi.repository import Gtk, Adw


@Gtk.Template(resource_path='/al/getcryst/FirstSetup/gtk/done.ui')
class VanillaDone(Adw.Bin):
    __gtype_name__ = 'VanillaDone'

    status_page = Gtk.Template.Child()
    btn_reboot = Gtk.Template.Child()
    btn_close = Gtk.Template.Child()

    def __init__(self, window, **kwargs):
        super().__init__(**kwargs)
        self.__window = window
        
        self.status_page.set_description(
            "Restart your PC to enjoy your {} experience.".format(
                self.__window.recipe["distro_name"]
            )
        )

        self.btn_reboot.connect("clicked", self.__on_reboot_clicked)
        self.btn_close.connect("clicked", self.__on_close_clicked)
    
    def set_result(self, result):
        if not result:
            self.status_page.set_icon_name("dialog-error-symbolic")
            self.status_page.set_title("Something went wrong")
            self.status_page.set_description("Please contact the distribution developers.")
            self.btn_reboot.set_visible(False)
            self.btn_close.set_visible(True)

    def __on_reboot_clicked(self, button):
        subprocess.run(['gnome-session-quit', '--reboot'])

    def __on_close_clicked(self, button):
        self.__window.close()

