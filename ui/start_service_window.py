# start_service_window.py
import subprocess
import threading
from gi.repository import Gtk, GLib

class StartServiceWindow(Gtk.Window):
    def __init__(self, service_location, port_no):
        Gtk.Window.__init__(self, title="Service Logs")
        self.set_default_size(600, 400)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # ScrolledWindow for the logs
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)
        vbox.pack_start(scrolled_window, True, True, 0)

        # Create a TextView for logs
        self.textview = Gtk.TextView()
        self.textview.set_editable(False)
        self.textview.set_cursor_visible(False)
        self.textbuffer = self.textview.get_buffer()
        scrolled_window.add(self.textview)  # Add the TextView to the ScrolledWindow

        # Start and Stop buttons
        self.restart_button = Gtk.Button(label="Restart Service")
        self.restart_button.connect("clicked", self.on_restart_clicked, service_location, port_no)
        vbox.pack_start(self.restart_button, False, False, 0)

        self.start_button = Gtk.Button(label="Start Service")
        self.start_button.connect("clicked", self.on_start_clicked, service_location, port_no)
        vbox.pack_start(self.start_button, False, False, 0)

        self.stop_button = Gtk.Button(label="Stop Service")
        self.stop_button.connect("clicked", self.on_stop_clicked)
        vbox.pack_start(self.stop_button, False, False, 0)

        self.proc = None

    def on_restart_clicked(self,widget,service_location,port_no):
        if self.proc:
            self.proc.terminate()
            self.proc = None
            # Clear the TextView
            GLib.idle_add(self.clear_textview)
        
        cmd = ["gunicorn", "-w", "1", "-b", f"0.0.0.0:{port_no}","--access-logfile","/app/logs/access.log","--error-logfile","/app/logs/error.log", "app:app"]
        
        # Change working directory to service location
        self.proc = subprocess.Popen(
            cmd,
            cwd=service_location,  # Important: Set the working directory
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )

        # Create a new thread to read the output and errors
        threading.Thread(target=self.read_output, args=(self.proc.stdout,)).start()
        threading.Thread(target=self.read_output, args=(self.proc.stderr,)).start()

    def on_start_clicked(self, widget, service_location, port_no):
        cmd = ["gunicorn", "-w", "1", "-b", f"0.0.0.0:{port_no}", "--access-logfile","logs/access.log","--error-logfile","logs/error.log","app:app"]
        
        # Change working directory to service location
        self.proc = subprocess.Popen(
            cmd,
            cwd=service_location,  # Important: Set the working directory
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )

        # Create a new thread to read the output and errors
        threading.Thread(target=self.read_output, args=(self.proc.stdout,)).start()
        threading.Thread(target=self.read_output, args=(self.proc.stderr,)).start()


    def on_stop_clicked(self, widget):
        if self.proc:
            self.proc.terminate()
            self.proc = None
            # Clear the TextView
            GLib.idle_add(self.clear_textview)

    def read_output(self, pipe):
        while True:
            line = pipe.readline()
            if line:
                GLib.idle_add(self.update_textview, line)
            else:
                break

    def update_textview(self, text):
        end_iter = self.textbuffer.get_end_iter()
        self.textbuffer.insert(end_iter, text)
    
    def clear_textview(self):
        self.textbuffer.set_text('') 
