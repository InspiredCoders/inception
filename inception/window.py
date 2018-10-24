import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from program import run_app


class WindowHandler:
    def __init__(self, window):
        self.win = window

    def on_window_destroy(self, *args):
        Gtk.main_quit()

    def on_about_clicked(self, widget):
        self.win.builder.get_object("about_dialog").show_all()

    def on_close_clicked(self, widget):
        self.win.builder.get_object("about_dialog").hide_on_delete()

    def on_warning_close(self, widget):
        self.win.builder.get_object("warning_message").hide_on_delete()

    def on_success_close(self, widget):
        self.win.builder.get_object("success_message").hide_on_delete()

    def on_group_clicked(self, widget):
        selection = self.win.builder.get_object("folder_choose")
        path = selection.get_filename()

        if path:
            run_app(path)
            selection.unselect_filename(path)
            self.win.builder.get_object("success_message").show_all()
        else:
            self.win.builder.get_object("warning_message").show_all()


class MainWindow:
    def __init__(self, handler):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("window.glade")
        self.builder.connect_signals(handler(self))

        self.about = self.builder.get_object("about_dialog")
        self.set_window("main_window")

    def set_window(self, window):
        self.window = self.builder.get_object(window)
        self.window.show_all()

    def main(self):
        Gtk.main()


if __name__ == "__main__":
    app = MainWindow(WindowHandler)
    app.main()
