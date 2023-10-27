from gi.repository import Gtk
import os
from ui.automated_service_creation_window import AutomatedServiceCreationWindow

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My Automation App")
        self.set_default_size(1000, 300)  

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        self.default_location = "/home/anoop/Downloads/TechnicalWork/MyProjects"
        self.folder_to_window = {}
        self.folder_to_window['AutomatedServiceCreation'] = self.on_automated_service_creation_button_clicked

        for project_type_name in os.listdir(self.default_location):
            project_type_path = os.path.join(self.default_location,project_type_name)
            if os.path.isdir(project_type_path) and project_type_name!='AutomationUI' and project_type_name!='trial':
                number_of_projects = len(os.listdir(project_type_path))
                frame = Gtk.Frame()
                frame.set_size_request(1000, 50)
                vbox.pack_start(frame,False,False,0)
                expander = Gtk.Expander()
                expander.set_label(f"<big><b>Show {project_type_name} Projects - {number_of_projects}</b></big>")
                expander.set_use_markup(True)
                frame.add(expander)
                sublist_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
                expander.add(sublist_box)
                for project_name in os.listdir(project_type_path):
                    project_path = os.path.join(project_type_path, project_name)
                    if os.path.isdir(project_path):
                        button = Gtk.Button(label=f"Open {project_name} window")
                        button.connect("clicked", self.folder_to_window.get(project_name,self.on_project_button_clicked), project_name)
                        sublist_box.pack_start(button, True, True, 0)
                # button = Gtk.Button()
                # button.connect("clicked",self.on_service_button_clicked,folder_name)


    def on_automated_service_creation_button_clicked(self, widget, project_name):
        project_path = os.path.join(self.default_location, project_name)
        win = AutomatedServiceCreationWindow()
        win.show_all()

    def on_project_button_clicked(self, widget, project_name):
        print(f"Running service for subfolder: {project_name}")
        # Here you can run the corresponding service based on the subfolder name