import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from about import About
from noGenerated import NoGenerated
from numbify import NumberEntry
from fpdf import FPDF

class Core(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_default_size(1280,720)
        self.set_border_width(20)
        self.set_resizable(False)

        # Variables iniciales
        self.readyToLoad = False
        self.dta_scores = []

        # Boton - Abrir archivo
        btn_openFile = Gtk.Button(label = "Abrir")
        btn_openFile.connect("clicked", self.openFile)

        # Boton - Guardar archivo
        self.btn_saveFile = Gtk.Button(label="Guardar")
        self.btn_saveFile.connect("clicked", self.saveFile)
        self.btn_saveFile.set_sensitive(False)

        # Boton - About
        btn_about = Gtk.Button()
        img_about = Gtk.Image().new_from_file("res/about.png") # 30px es el tamaño preciso
        btn_about.set_image(img_about)
        btn_about.connect("clicked", self.aboutShow)

        # Header
        self.header = Gtk.HeaderBar(title = "Evaluatron")
        self.header.set_subtitle("Seleccione un archivo para evaluar automáticamente")
        self.header.props.show_close_button = True

        self.header.pack_start(btn_openFile)
        self.header.pack_start(self.btn_saveFile)
        self.header.pack_end(btn_about)

        self.set_titlebar(self.header)

        # ListStore - Notas Rojas
        self.lss_red = Gtk.ListStore(int, str)
        trv_red = Gtk.TreeView(model = self.lss_red)
        renderer = Gtk.CellRendererText()
        
        for i, column_title in enumerate(["Puntaje", "Calificación",]):

            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            trv_red.append_column(column)

        # ListStore - Notas Azules
        self.lss_blue = Gtk.ListStore(int, str)
        trv_blue = Gtk.TreeView(model = self.lss_blue)
        
        for i, column_title in enumerate(["Puntaje", "Calificación",]):

            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            trv_blue.append_column(column)

        # ListStore - Notas Estudiantes
        self.lss_grades = Gtk.ListStore(str, int, str)
        trv_grades = Gtk.TreeView(model = self.lss_grades)

        for i, column_title in enumerate(["Estudiante", "Puntaje", "Calificación"]):

            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            trv_grades.append_column(column)

        # Labels
        lbl_max = Gtk.Label(label = "Puntaje máximo")
        lbl_max.set_justify(Gtk.Justification.LEFT)
        lbl_passScore = Gtk.Label(label = "Porcentaje de aprobación [%]")
        lbl_passScore.set_justify(Gtk.Justification.LEFT)
        lbl_type = Gtk.Label(label = "Tipo de evaluación")
        lbl_type.set_justify(Gtk.Justification.LEFT)

        # Entrys
        self.ent_max = NumberEntry()
        self.ent_max.set_input_purpose(2)
        self.ent_max.set_text("10")

        self.ent_passScore = NumberEntry()
        self.ent_passScore.set_text("60")
        self.ent_passScore.set_input_purpose(2)

        # ComboBox - Tipo de Notas
        self.cbb_type = Gtk.ComboBoxText()
        self.cbb_type.append("0", "7 - Calificación mínima 1")
        self.cbb_type.append("1", "7 - Calificación mínima 2")
        self.cbb_type.append("2", "Decimal")
        self.cbb_type.append("3", "Porcentual")
        self.cbb_type.append("4", "Alfabético (60%)")
        self.cbb_type.set_active(0)

        # Boton - Generar escala de notas
        btn_gen = Gtk.Button(label = "Generar")
        btn_gen.connect("clicked", self.generate)

        # Scrolled - Contenedor Rojos
        rll_red = Gtk.ScrolledWindow()
        rll_red.set_vexpand(True)
        rll_red.set_hexpand(True)

        rll_red.add(trv_red)

        # Scrolled - Contenedor Azules
        rll_blue = Gtk.ScrolledWindow()
        rll_blue.set_vexpand(True)
        rll_blue.set_hexpand(True)

        rll_blue.add(trv_blue)

        # Scrolled - Contenedor Notas de los Alumnos
        rll_grades = Gtk.ScrolledWindow()
        rll_grades.set_vexpand(True)

        rll_grades.add(trv_grades)
        

        # Grid - Parametros de la escala de notas
        grid = Gtk.Grid()
        grid.set_column_spacing(20)
        grid.set_row_spacing(10)

        grid.attach(lbl_max, 0, 0, 1, 1)
        grid.attach_next_to(lbl_passScore, lbl_max, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(lbl_type, lbl_passScore, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(self.ent_max, lbl_max, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.ent_passScore, lbl_passScore, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.cbb_type, lbl_type, Gtk.PositionType.BOTTOM, 2, 1)
        grid.attach_next_to(btn_gen, self.ent_passScore, Gtk.PositionType.BOTTOM, 2, 1)

        # Box - Contenedor de escala de notas
        infoBox = Gtk.Box(orientation = 1, spacing = 20)

        infoBox.pack_start(grid, False, True, 0)
        infoBox.pack_start(rll_grades, False, True, 0)

        # Box - Contenedor principal
        mainBox = Gtk.Box(spacing = 20)

        mainBox.pack_start(rll_red, False, True, 0)
        mainBox.pack_start(rll_blue, False, True, 0)
        mainBox.pack_start(infoBox, True, True, 0)

        # Fin del constructor
        self.add(mainBox)
    
    # Carga de un archivo csv
    def openFile(self, widget):
            
        # Si ya se generó una escala se puede cargar el archivo
        if self.readyToLoad:

            self.lss_grades.clear()

            # Creación del dialogo
            fileDialog = Gtk.FileChooserDialog(title="Selecciona el archivo a evaluar",
                                            parent=self,
                                            action=Gtk.FileChooserAction.OPEN)
            
            fileDialog.add_buttons(
                Gtk.STOCK_CANCEL,
                Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OPEN,
                Gtk.ResponseType.OK,
            )
            # Filtros de archivos
            filter_csv = Gtk.FileFilter()
            filter_csv.set_name("Archivo separado por comas (.csv)")
            filter_csv.add_pattern("*csv")

            fileDialog.add_filter(filter_csv)

            # Ejecución del dialogo
            response = fileDialog.run()
            if response == Gtk.ResponseType.OK:
                self.dta_scores = fileDialog.get_filename()
                fileName = fileDialog.get_filename().split("/")
                self.header.set_subtitle(fileName[-1])

                # Procesado del archivo elegido
            
                file = open(fileDialog.get_filename(), "r")
                for line in file:
                    line_text = line.replace("\n", "")
                    line_data = line_text.split(",")


                    for item in self.markData:
                        if int(line_data[1]) > self.markData[-1][0]:
                            line_proccesed = [line_data[0], int(line_data[1]), "Los puntos exceden la escala generada"]

                        if str(line_data[1]) == str(item[0]):
                            line_proccesed = [line_data[0], int(line_data[1]), item[1]]

                    self.lss_grades.append(line_proccesed)

                #Fin del dialogo
                self.btn_saveFile.set_sensitive(True)
            fileDialog.destroy()

        else:
            NoGenerated(self)

    def aboutShow(self, widget):
        About(self)

    def generate(self, widget):

        # Pasar a estado de YA SE PUEDE EVALUAR
        self.readyToLoad = True
        
        # Limpieza de datos anteriores
        self.lss_blue.clear()
        self.lss_red.clear()

        # Definición de parametros iniciales según el sistema de calificación
        if self.cbb_type.get_active() == 0:
            decimalSystem = False
            min_mark = 1
            aprob_mark = 4
            max_mark = 7
        
        if self.cbb_type.get_active() == 1:
            decimalSystem = False
            min_mark = 2
            aprob_mark = 4
            max_mark = 7
        
        if self.cbb_type.get_active() == 2:
            decimalSystem = True
            alfanumeric = False
            min_mark = 0
            aprob_mark = int(self.ent_passScore.get_text())/10
            max_mark = 10

        if self.cbb_type.get_active() == 3:
            decimalSystem = True
            alfanumeric = False
            min_mark = 0
            aprob_mark = int(self.ent_passScore.get_text())/10
            max_mark = 100

        if self.cbb_type.get_active() == 4:
            self.ent_passScore.set_text("60")
            decimalSystem = True
            alfanumeric = True
            min_mark = 0
            aprob_mark = int(self.ent_passScore.get_text())/100
            max_mark = 100


        # Calculo de puntaje de aprobacion
        self.realPassScore = int(self.ent_max.get_text()) * (int(self.ent_passScore.get_text())/100)

        # Para sistemas decimales [0/10 o 0/100]
        if decimalSystem:
            for points in range(int(self.ent_max.get_text())):
                mark = points/(int(self.ent_max.get_text())/100)
                if points < self.realPassScore:
                    if alfanumeric:
                        self.lss_red.append([(points), ("F")])
                    else:
                        self.lss_red.append([(points), (str(round(mark,1)))])
                else:
                    if alfanumeric:
                        if 60 <= round(mark,1) < 63:
                            grade = "D-"
                        
                        if 63 <= round(mark,1) < 66:
                            grade = "D"
                        
                        if 66 <= round(mark,1) < 69:
                            grade = "D+"
                        
                        if 69 <= round(mark,1) < 72:
                            grade = "C-"

                        if 72 <= round(mark,1) < 76:
                            grade = "C"

                        if 76 <= round(mark,1) < 79:
                            grade = "C+"

                        if 79 <= round(mark,1) < 82:
                            grade = "B-"

                        if 82 <= round(mark,1) < 86:
                            grade = "B"

                        if 86 <= round(mark,1) < 89:
                            grade = "B+"
                        
                        if 89 <= round(mark,1) < 92:
                            grade = "A"

                        if 92 <= round(mark,1) < 100:
                            grade = "A+"
                        
                        self.lss_blue.append([(points), (grade)])

                    else:
                        self.lss_blue.append([(points), (str(round(mark,1)))])


        # Para sistema no decimal [1/7 0 2/7]
        else:
            # Calculo de incrementos
            red_increment = (aprob_mark-min_mark)/self.realPassScore
            blue_increment = (max_mark-aprob_mark)/(int(self.ent_max.get_text())-self.realPassScore)

            # Calculo de nota
            for points in range(int(self.ent_max.get_text())+1):
                
                # Notas de desaprobación
                if points < self.realPassScore:
                    mark = red_increment*(points)+min_mark
                    if round(mark,1) < 4:
                        self.lss_red.append([(points), (str(round(mark,1)))])
                    else:
                        self.lss_blue.append([(points), (str(round(mark,1)))])
                
                # Notas de aprobación
                else:
                    mark = blue_increment*(points-self.realPassScore)+aprob_mark
                    self.lss_blue.append([(points), (str(round(mark,1)))])


        # Guardado de datos para asignación automática del archivo
        i = 0
        self.markData = []
        for row in self.lss_red:
            for values in row:
                if i%2 == 0:
                    pointsGenerated = values
                else:
                    markGenerated = values
                i = i + 1
            self.markData.append([pointsGenerated, markGenerated])

        for row in self.lss_blue:
            for values in row:
                if i%2 == 0:
                    pointsGenerated = values
                else:
                    markGenerated = values
                i = i + 1
            self.markData.append([pointsGenerated, markGenerated])


    # Guardar archivo de calificaciones generadas
    def saveFile(self, widget):
        print("save")
        # Creación del dialogo
        fileDialog = Gtk.FileChooserDialog(title="Selecciona donde guardar las calificaciones generadas",
                                        parent=self,
                                        action=Gtk.FileChooserAction.SAVE)
        
        fileDialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_SAVE,
            Gtk.ResponseType.OK,
        )
        # Filtros de archivos
        filter_csv = Gtk.FileFilter()
        filter_csv.set_name("Archivo pdf (.pdf)")
        filter_csv.add_pattern("*pdf")

        fileDialog.add_filter(filter_csv)

        # Ejecución del dialogo
        fileDialog.set_current_name("calificaciones")
        response = fileDialog.run()

        # Forzar la creación tipo .pdf del archivo
        if ".pdf" not in fileDialog.get_current_name():
            fileName = fileDialog.get_current_name() + ".pdf"
            fileDialog.set_current_name(fileName)

        if response == Gtk.ResponseType.OK:
            filePath = fileDialog.get_filename()

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size = 12)
            i = 1
            for row in self.lss_grades:
                line = row[0]+"   "+ ("puntos: " + str(row[1])) +"   nota: "+ row[2]
                pdf.cell(200, 10, txt = line,ln = i, align = 'L')
                i = i+1

            pdf.output(filePath)
                    

        fileDialog.destroy()
        print(filePath)


    
main = Core()
main.connect("destroy", Gtk.main_quit)
main.show_all()
Gtk.main()