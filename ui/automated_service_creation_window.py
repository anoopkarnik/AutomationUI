from gi.repository import Gtk
from services.automated_service_creation import run

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

        # CheckButton for Create Git
        self.check_create_git = Gtk.CheckButton(label="Create Git Repo?")
        vbox.pack_start(self.check_create_git, True, True, 0)

        # Entry for Git Repo Name
        self.entry_git_name = Gtk.Entry()
        self.entry_git_name.set_placeholder_text("Enter git repo name")

        # Show/Hide Git Repo Name based on CheckButton
        # self.entry_git_name.set_visible(False)
        # self.check_create_git.connect("toggled", self.on_git_toggled)

        self.button_submit = Gtk.Button(label="Submit")
        self.button_submit.connect("clicked", self.on_submit_clicked)
        vbox.pack_start(self.button_submit, True, True, 0)

    # def on_git_toggled(self, widget):
    #     self.vbox.remove(self.button_submit)
    #     if widget.get_active():
    #         self.vbox.pack_start(self.entry_git_name, True, True, 0)
    #         self.entry_git_name.show()
    #     else:
    #         self.vbox.remove(self.entry_git_name)
    #     self.vbox.pack_start(self.button_submit, True, True, 0)
    #     self.button_submit.show()

    def on_submit_clicked(self, widget):
        # Here, you can call your service to make the POST request with these parameters.
        print("Service Type:", self.combo_service_type.get_active_text())
        print("Folder Path:", self.entry_location.get_filename())
        print("Service Name:", self.entry_service_name.get_text())
        print("Create Git Repo:", self.check_create_git.get_active())
        run(self.combo_service_type.get_active_text(),self.entry_location.get_filename(),
        self.entry_service_name.get_text(),self.check_create_git.get_active())

        # if self.check_create_git.get_active():
        #     print("Git Repo Name:", self.entry_git_name.get_text())
