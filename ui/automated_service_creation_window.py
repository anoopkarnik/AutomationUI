from gi.repository import Gtk
from services.automated_service_creation import create_service,delete_service
from ui.start_service_window import StartServiceWindow
import os

class AutomatedServiceCreationWindow(Gtk.Window):
    def __init__(self,url,service_details,project_path):
        Gtk.Window.__init__(self, title="Generate New Service")
        self.set_default_size(400, 300)  # Optional: You can set a default size for this window too

        self.url = url
        self.service_details = service_details
        self.project_path = project_path

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.start_service_button = Gtk.Button(label="Service Start/Stop")
        self.start_service_button.connect("clicked", self.on_start_service_clicked)
        vbox.pack_start(self.start_service_button, True, True, 0)

        frame = Gtk.Frame()
        frame.set_size_request(500,50)
        vbox.pack_start(frame,False,False,0)
        
        expander = Gtk.Expander()
        expander.set_label(f"<big> <b> Create Service </b> </big>")
        expander.set_use_markup(True)
        frame.add(expander)

        sublist_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
        expander.add(sublist_box)

        # Dropdown for Service Type
        self.create_service_type = Gtk.ComboBoxText()
        self.create_service_type.append_text("flask")
        self.create_service_type.append_text("springBoot")
        self.create_service_type.append_text("react")
        self.create_service_type.append_text("react native")
        sublist_box.pack_start(self.create_service_type, True, True, 0)

        self.entry_create_location = Gtk.FileChooserButton(title="Select a Folder", action=Gtk.FileChooserAction.SELECT_FOLDER)
        sublist_box.pack_start(self.entry_create_location, True, True, 0)

        self.entry_create_service_name = Gtk.Entry()
        self.entry_create_service_name.set_placeholder_text("Enter service name")
        sublist_box.pack_start(self.entry_create_service_name, True, True, 0)

        self.entry_create_service_port = Gtk.Entry()
        self.entry_create_service_port.set_placeholder_text("Enter service port")
        sublist_box.pack_start(self.entry_create_service_port, True, True, 0)

        self.check_create_local = Gtk.CheckButton(label="Create Local Service?")
        sublist_box.pack_start(self.check_create_local, True, True, 0)

        self.check_create_git = Gtk.CheckButton(label="Create Git Repo?")
        sublist_box.pack_start(self.check_create_git, True, True, 0)

        self.check_create_ecr = Gtk.CheckButton(label="Create Ecr Repo?")
        sublist_box.pack_start(self.check_create_ecr, True, True, 0)

        self.button_submit = Gtk.Button(label="Create Service")
        self.button_submit.connect("clicked", self.on_create_service)
        sublist_box.pack_start(self.button_submit, True, True, 0)

        frame = Gtk.Frame()
        frame.set_size_request(500,50)
        vbox.pack_start(frame,False,False,0)
        
        expander = Gtk.Expander()
        expander.set_label(f"<big> <b> Delete Service </b> </big>")
        expander.set_use_markup(True)
        frame.add(expander)

        sublist_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
        expander.add(sublist_box)

        # Dropdown for Service Type
        self.delete_service_type = Gtk.ComboBoxText()
        self.delete_service_type.append_text("flask")
        self.delete_service_type.append_text("springBoot")
        self.delete_service_type.append_text("react")
        self.delete_service_type.append_text("react native")
        sublist_box.pack_start(self.delete_service_type, True, True, 0)

        self.entry_delete_location = Gtk.FileChooserButton(title="Select a Folder", action=Gtk.FileChooserAction.SELECT_FOLDER)
        sublist_box.pack_start(self.entry_delete_location, True, True, 0)

        self.entry_delete_service_name = Gtk.Entry()
        self.entry_delete_service_name.set_placeholder_text("Enter service name")
        sublist_box.pack_start(self.entry_delete_service_name, True, True, 0)

        self.check_delete_local = Gtk.CheckButton(label="Delete Local Service?")
        sublist_box.pack_start(self.check_delete_local, True, True, 0)

        self.check_delete_git = Gtk.CheckButton(label="Delete Git Repo?")
        sublist_box.pack_start(self.check_delete_git, True, True, 0)

        self.check_delete_ecr = Gtk.CheckButton(label="Delete Ecr Repo?")
        sublist_box.pack_start(self.check_delete_ecr, True, True, 0)

        self.check_delete_image = Gtk.CheckButton(label="Delete Docker Image")
        sublist_box.pack_start(self.check_delete_image, True, True, 0)

        self.check_delete_container = Gtk.CheckButton(label="Delete Docker Container")
        sublist_box.pack_start(self.check_delete_container, True, True, 0)

        self.button_submit = Gtk.Button(label="Delete Service")
        self.button_submit.connect("clicked", self.on_delete_service)
        sublist_box.pack_start(self.button_submit, True, True, 0)

    

    def on_start_service_clicked(self, widget):
        service_location = os.path.join(self.project_path,"app")  
        win = StartServiceWindow(service_location, self.service_details['port_no'])
        win.show_all()


    def on_create_service(self, widget):
        try:
            create_service(self.url,self.service_details,self.create_service_type.get_active_text(),
            self.entry_create_location.get_filename(),
            self.entry_create_service_name.get_text(),self.entry_create_service_port.get_text(),self.check_create_local.get_active(),
            self.check_create_git.get_active(),self.check_create_ecr.get_active())
            self.destroy()
        except Exception as e:
            dialog = Gtk.MessageDialog(
                transient_for=self,
                flags=0,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.CANCEL,
                text="Error",
                )
            dialog.format_secondary_text(str(e))
            dialog.run()
            dialog.destroy()

    def on_delete_service(self, widget):
        try:
            delete_service(self.url,self.service_details,self.delete_service_type.get_active_text(),
            self.entry_delete_location.get_filename(),
            self.entry_delete_service_name.get_text(),self.check_delete_local.get_active(),
            self.check_delete_git.get_active(),self.check_delete_ecr.get_active(),self.check_delete_container.get_active(),
            self.check_delete_image.get_active())
            self.destroy()
        except Exception as e:
            dialog = Gtk.MessageDialog(
                transient_for=self,
                flags=0,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.CANCEL,
                text="Error",
                )
            dialog.format_secondary_text(str(e))
            dialog.run()
            dialog.destroy()
