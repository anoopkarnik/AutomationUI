from gi.repository import Gtk
from services.notion_flask_api_service import update_books, update_movies_tvshows, update_dashboard_status,add_to_calendar
from ui.start_service_window import StartServiceWindow
import os

class NotionFlaskApiServiceWindow(Gtk.Window):
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

        self.books_button_submit = Gtk.Button(label="Update Books")
        self.books_button_submit.connect("clicked", self.on_update_books)
        vbox.pack_start(self.books_button_submit, True, True, 0)

        self.movies_tvshows_button_submit = Gtk.Button(label="Update Movies Tvshows")
        self.movies_tvshows_button_submit.connect("clicked", self.on_update_movies_tvshows)
        vbox.pack_start(self.movies_tvshows_button_submit, True, True, 0)

        self.dashboard_button_submit = Gtk.Button(label="Update Dashboard Status")
        self.dashboard_button_submit.connect("clicked", self.on_update_dashboard_status)
        vbox.pack_start(self.dashboard_button_submit, True, True, 0)

        self.calendar_button_submit = Gtk.Button(label="Add to Calendar")
        self.calendar_button_submit.connect("clicked", self.on_add_to_calendar)
        vbox.pack_start(self.calendar_button_submit, True, True, 0)

    def on_start_service_clicked(self, widget):
        service_location = os.path.join(self.project_path,"app")  
        win = StartServiceWindow(service_location, self.service_details['port_no'])
        win.show_all()
    
    def on_update_books(self,widget):
        update_books(self.url,self.service_details)

    def on_update_movies_tvshows(self, widget):
        update_movies_tvshows(self.url,self.service_details)

    def on_update_dashboard_status(self, widget):
        update_dashboard_status(self.url,self.service_details)
    
    def on_add_to_calendar(self,widget):
        add_to_calendar(self.url,self.service_details)