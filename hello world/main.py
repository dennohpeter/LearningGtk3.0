import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk




class Main:

    def __init__(self):
        gladeFile = 'hello world.glade'

        self.builder = gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)

        window = self.builder.get_object('window')
        window.connect('delete-event', gtk.main_quit)
        window.show()

    def on_button_clicked(self, widget):
        label = self.builder.get_object('label')
        label.set_text("Hello World")


if __name__ == '__main__':
    main = Main()
    gtk.main()
