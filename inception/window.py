import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class WindowHandler:
    def __init__(self, window):
        self.win = window


class MainWindow:
    def __init__(self, handler):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("window.glade")
        self.builder.connect_signals(handler(self))

        self.set_window("main_window")

    def set_window(self, window):
        self.window = self.builder.get_object(window)
        self.window.show_all()

    def main(self):
        Gtk.main()

app = MainWindow(WindowHandler)
app.main()
