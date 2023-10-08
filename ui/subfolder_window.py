# File: ui/subfolder_window.py
import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SubfolderWindow(Gtk.Window):
    def __init__(self, parent_folder_path):
        Gtk.Window.__init__(self, title=f"Subfolders in {os.path.basename(parent_folder_path)}")
        self.set_default_size(300, 200)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        for folder_name in os.listdir(parent_folder_path):
            full_path = os.path.join(parent_folder_path, folder_name)
            if os.path.isdir(full_path):
                button = Gtk.Button(label=f"Run {folder_name}")
                button.connect("clicked", self.on_subfolder_button_clicked, folder_name)
                vbox.pack_start(button, True, True, 0)

    def on_subfolder_button_clicked(self, widget, subfolder_name):
        print(f"Running service for subfolder: {subfolder_name}")
        # Here you can run the corresponding service based on the subfolder name
