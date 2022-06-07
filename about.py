import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import os

class About(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Información del proyecto", transient_for=parent, flags=0)

        self.set_default_size(400, 200)
        self.set_border_width(5)

        # Labels
        lbl_projectName = Gtk.Label(label = "Evaluatron")
        lbl_projectVersion = Gtk.Label(label = "v 1.0")

        lbl_projectInfo = Gtk.Label()
        lbl_projectInfo.set_text("Este proyecto es en básicas palabras un generador de escala de notas con un evaluador automático que funciona de acuerdo a la escala de notas generada.")
        lbl_projectInfo.set_line_wrap(True)

        lbl_projectAuthor = Gtk.Label(label = "Creado por Angel Guerrero y Yostin Sepúlveda")

        btn_authorPage = Gtk.Button()
        btn_authorPage.connect("clicked", self.openGit)
        img_github = Gtk.Image().new_from_file("res/github.png")
        btn_authorPage.set_image(img_github)

        # Agregación
        box = Gtk.Box(orientation = 1, spacing=20)
        box.add(lbl_projectName)
        box.add(lbl_projectVersion)
        box.add(lbl_projectInfo)
        box.add(lbl_projectAuthor)
        box.add(btn_authorPage)

        dialogBox = self.get_content_area()
        dialogBox.add(box)

        self.show_all()

    def openGit(self, widget):
        os.system("sensible-browser https://github.com/AngelTheG/")
