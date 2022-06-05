import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class NoGenerated(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Aviso", transient_for=parent, flags=0)

        self.set_default_size(200, 80)

        label = Gtk.Label(label="Recuerda que para cargar un archivo debes haber generado una escala de evaluación")
        label.set_line_wrap(True)

        box = self.get_content_area()
        box.add(label)
        self.show_all()
