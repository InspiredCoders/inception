import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Inception")
        self.set_border_width(30)
        layout = Gtk.Box(spacing=8)
        self.add(layout)

        self.path = Gtk.Entry()
        self.path.set_editable(False)
        layout.add(self.path)
        button = Gtk.Button('Browse')
        button.connect('clicked', self.on_file_clicked)
        self.button2 = Gtk.Button('Run')
        self.button2.set_sensitive(False)
        self.button2.connect('clicked', self.on_run_clicked)
        layout.add(button)
        layout.add(self.button2)

    def on_run_clicked(self, widget):
        pass

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
                                       Gtk.FileChooserAction.SELECT_FOLDER,
                                       (Gtk.STOCK_CANCEL,
                                        Gtk.ResponseType.CANCEL,
                                        "Select", Gtk.ResponseType.OK))

        dialog.set_default_size(400, 200)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            folder_path = dialog.get_filename()
            self.path.set_text(str(folder_path))
            self.button2.set_sensitive(True)

        dialog.destroy()


window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
