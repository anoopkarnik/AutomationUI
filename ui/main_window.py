from gi.repository import Gtk
import os
from ui.subfolder_window import SubfolderWindow

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My Automation App")
        self.set_default_size(400, 300)  

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.default_location = "/home/anoop/Downloads/TechnicalWork/MyProjects"

        for folder_name in os.listdir(self.default_location):
            full_path = os.path.join(self.default_location,folder_name)
            if os.path.isdir(full_path) and folder_name!='AutomationUI':
                number_of_projects = len(os.listdir(full_path))
                button = Gtk.Button(label=f"Show {folder_name} Projects - {number_of_projects}")
                button.connect("clicked",self.on_service_button_clicked,folder_name)
                vbox.pack_start(button, True, True, 0)

    def on_service_button_clicked(self, widget, folder_name):
        full_path = os.path.join(self.default_location, folder_name)
        win = SubfolderWindow(full_path)
        win.show_all()