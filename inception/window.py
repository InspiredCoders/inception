import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class WindowHandler:
    def __init__(self, window):
        self.win = window

    def on_window_destroy(self, *args):
        Gtk.main.quit()

    def on_about_clicked(self, widget):
        self.win.builder.get_object("about_dialog").show_all()

    def on_close_clicked(self, widget):
        pass

    def on_group_clicked(self, widget):
        pass


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
