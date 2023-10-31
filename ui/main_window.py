from gi.repository import Gtk
import requests
import os
from ui.automated_service_creation_window import AutomatedServiceCreationWindow
from ui.notion_flask_api_service_window import NotionFlaskApiServiceWindow

class MainWindow(Gtk.Window):
    def __init__(self,url='http://0.0.0.0',default_location='/home/anoop/Downloads/TechnicalWork/MyProjects'):
        Gtk.Window.__init__(self, title="My Automation App")
        self.set_default_size(1000, 300)  

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)
        self.url = url
        self.default_location = default_location
        self.folder_to_window = {}

        self.folder_to_window['AutomatedServiceCreation'] = {}
        self.folder_to_window['notion-flask-api-service'] = {}
        self.folder_to_window['default'] = {}

        service_name = 'AutomatedServiceCreation'
        self.folder_to_window[service_name ]['ServiceWindow'] = self.on_automated_service_creation_button_clicked
        self.folder_to_window[service_name ]['port_no'] = '8100'

        try:
            response = requests.get(f"{self.url}:{self.folder_to_window[service_name ]['port_no']}/")
            self.folder_to_window[service_name ]['running'] = True if response.status_code==200 else False
        except:
            self.folder_to_window[service_name ]['running'] = False


        service_name = 'notion-flask-api-service'
        self.folder_to_window[service_name]['ServiceWindow'] = self.on_notion_flask_api_service_button_clicked
        self.folder_to_window[service_name]['port_no'] = '8110'
        self.folder_to_window[service_name ]['running'] = False
        try:
            response = requests.get(f"{self.url}:{self.folder_to_window[service_name ]['port_no']}/")
            self.folder_to_window[service_name ]['running'] = True if response.status_code==200 else False
        except:
            self.folder_to_window[service_name ]['running'] = False

        service_name = 'default'
        self.folder_to_window[service_name]['ServiceWindow'] = self.on_project_button_clicked
        self.folder_to_window[service_name]['port_no'] = 'Not Assigned'
        self.folder_to_window[service_name ]['running'] = False

        for project_type_name in os.listdir(self.default_location):
            project_type_path = os.path.join(self.default_location,project_type_name)
            if os.path.isdir(project_type_path) and project_type_name!='AutomationUI':
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
                        print(self.folder_to_window.get(project_name,self.folder_to_window['default']))
                        port_no = self.folder_to_window.get(project_name,self.folder_to_window['default'])['port_no']
                        currently_running = self.folder_to_window.get(project_name,self.folder_to_window['default'])['running']
                        label = (f"Open {project_name} window | ") + ("Running" if currently_running else "Stopped") + (f" | {port_no}")
                        button = Gtk.Button(label=label)
                        button.connect("clicked", self.folder_to_window.get(project_name,self.folder_to_window['default'])['ServiceWindow'], project_name,
                        self.folder_to_window.get(project_name,self.folder_to_window['default']),project_path)
                        sublist_box.pack_start(button, True, True, 0)
                # button = Gtk.Button()
                # button.connect("clicked",self.on_service_button_clicked,folder_name)


    def on_automated_service_creation_button_clicked(self, widget, project_name,service_details,project_path):
        win = AutomatedServiceCreationWindow(self.url,service_details,project_path)
        win.show_all()

    def on_notion_flask_api_service_button_clicked(self, widget, project_name,service_details,project_path):
        win = NotionFlaskApiServiceWindow(self.url,service_details,project_path)
        win.show_all()

    def on_project_button_clicked(self, widget, project_name,service_details):
        print(f"Running service for subfolder: {project_name}")
        # Here you can run the corresponding service based on the subfolder name