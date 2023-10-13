# File: ui/subfolder_window.py
import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ui.automated_service_creation_window import AutomatedServiceCreationWindow

class SubfolderWindow(Gtk.Window):
    def __init__(self, parent_folder_path):
        Gtk.Window.__init__(self, title=f"Subfolders in {os.path.basename(parent_folder_path)}")
        self.set_default_size(300, 200)
        self.parent_folder_path = parent_folder_path

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.folder_to_window = {}
        self.folder_to_window['AutomatedServiceCreation'] = self.on_automated_service_creation_button_clicked

        for folder_name in os.listdir(parent_folder_path):
            full_path = os.path.join(parent_folder_path, folder_name)
            if os.path.isdir(full_path):
                button = Gtk.Button(label=f"Run {folder_name}")
                button.connect("clicked", self.folder_to_window.get(folder_name,self.on_subfolder_button_clicked), folder_name)
                vbox.pack_start(button, True, True, 0)
    
    def on_automated_service_creation_button_clicked(self, widget, folder_name):
        full_path = os.path.join(self.parent_folder_path, folder_name)
        win = AutomatedServiceCreationWindow()
        win.show_all()

    def on_subfolder_button_clicked(self, widget, subfolder_name):
        print(f"Running service for subfolder: {subfolder_name}")
        # Here you can run the corresponding service based on the subfolder name
