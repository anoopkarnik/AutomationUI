from gi.repository import Gtk
from services.automated_service_creation import create_service

class AutomatedServiceCreationWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Generate New Service")
        self.set_default_size(400, 300)  # Optional: You can set a default size for this window too

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.vbox = vbox
        self.add(vbox)

        # Dropdown for Service Type
        self.combo_service_type = Gtk.ComboBoxText()
        self.combo_service_type.append_text("flask")
        self.combo_service_type.append_text("springBoot")
        self.combo_service_type.append_text("react")
        self.combo_service_type.append_text("react native")
        vbox.pack_start(self.combo_service_type, True, True, 0)

        self.entry_location = Gtk.FileChooserButton(title="Select a Folder", action=Gtk.FileChooserAction.SELECT_FOLDER)
        vbox.pack_start(self.entry_location, True, True, 0)

        self.entry_service_name = Gtk.Entry()
        self.entry_service_name.set_placeholder_text("Enter service name")
        vbox.pack_start(self.entry_service_name, True, True, 0)

        self.check_create_local = Gtk.CheckButton(label="Create Local Service?")
        vbox.pack_start(self.check_create_local, True, True, 0)
        self.entry_local_name = Gtk.Entry()
        self.entry_local_name.set_placeholder_text("Enter local service name")

        self.check_create_git = Gtk.CheckButton(label="Create Git Repo?")
        vbox.pack_start(self.check_create_git, True, True, 0)
        self.entry_git_name = Gtk.Entry()
        self.entry_git_name.set_placeholder_text("Enter git repo name")

        self.check_create_ecr = Gtk.CheckButton(label="Create Ecr Repo?")
        vbox.pack_start(self.check_create_ecr, True, True, 0)
        self.entry_ecr_name = Gtk.Entry()
        self.entry_ecr_name.set_placeholder_text("Enter ecr repo name")


        self.button_submit = Gtk.Button(label="Submit")
        self.button_submit.connect("clicked", self.on_submit_clicked)
        vbox.pack_start(self.button_submit, True, True, 0)

    def on_submit_clicked(self, widget):
        try:
            print("Service Type:", self.combo_service_type.get_active_text())
            print("Service Name:", self.entry_service_name.get_text())
            print("Folder Path:", self.entry_location.get_filename())
            print("Create Local Repo:", self.check_create_local.get_active())
            print("Create Git Repo:", self.check_create_git.get_active())
            print("Create Ecr Repo:", self.check_create_ecr.get_active())
            create_service(self.combo_service_type.get_active_text(),self.entry_location.get_filename(),
            self.entry_service_name.get_text(),self.check_create_local.get_active(),
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
