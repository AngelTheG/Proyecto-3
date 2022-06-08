# Evaluatron

¿No resulta agotador el trabajo de corregir las pruebas, para después tener que tomar los puntajes, asignarles una calificación y finalmente hacer un archivo para publicar las notas? Pues Evaluatrón está aquí para ayudarte.

**Ya que puede:**
   + Generar escalas de notas en los siguientes sistemas de calificación:
      - Nota máxima 7, aprobación 4, Nota mínima 1 ó 2.
      - Sistema decimal.
      - Sistema Porcentual.
      - Sistema Alfabético. 
   + Autoevaluar un archivo separado por comas (.csv) usando el formato Alumno,Puntaje.
   + Importar la evaluación realizada automáticamente a un archivo pdf.


#### Requisitos:
  + **Librería [Gtk](https://www.gtk.org/docs/installations/linux/)**
  + **Librería [FPDF](http://www.fpdf.org/)** (También se puede instalar escribiendo **pip install fpdf** en la terminal)
  
### Ejecución
Para ejecutar el proyecto se debe abrir el archivo [core.py](https://github.com/AngelTheG/Proyecto-3/blob/master/core.py) desde la terminal siguiendo el ejemplo:

<a href="https://imgur.com/DgslPZI"><img src="https://i.imgur.com/DgslPZI.png" title="source: imgur.com" /></a>


## Primer Lanzamiento
Apenas se ejecute el proyecto se abrirá la ventana núcleo del proyecto.

<a href="https://imgur.com/2vi5l4r"><img src="https://i.imgur.com/2vi5l4r.png" title="source: imgur.com" /></a>

Los elementos que se logran ver son:
  
  **Botón Abrir**:
  
  * Este botón permite al usuario abrir un archivo para evaluar según la escala de calificación generada por medio de una ventana.
  * Si no hay una escala generada previamente en vez de abrir la ventana se abrirá un diálogo informandonos que debemos generar una tabla previamente
   
  **Botón Guardar**:
  * Este botón permite guardar la información de las evaluaciones de los alumnos en un archivo de formato **pdf**.
  * El botón permacerá deshabilitado hasta que se cargue un archivo.
  
  **Botón About**:
  
  * Este botón despliega un diálogo de información sobre el proyecto, además de contar con un botón que mostrará el perfil del creador en el navegador por defecto.
  
  **Tabla de puntos Reprobación**:
  
  * En este espacio se mostrarán los puntos pertenecientes a la nota de reprobación seleccionada.
  
  **Tabla de puntos Aprobación**:
  
  * En este espacio se mostrarán los puntos pertenecientes a la nota de aprobación seleccionada.
  
  **Puntos Máximos**:
  
  * En esta casilla se puede establecer los puntos máximos de la escala a generar.
  
  **Porcentaje de Aprobación**:
  
  * En esta casilla se puede establecer el porcentaje de aprobación o exigencia de la evaluación.
  
  **Tipo de Calificación**:
  
  * Aquí se puede seleccionar el sistema de calificación en el que se basará la escala de calificaciones.
  
  **Botón de Generar escala de calificación**:
  
  * Este botón generará las tablas de la escalas de calificación.

  **Tabla de archivo**:
  
  * Aquí se mostrarán los datos cargados y generados por el archivo.

## Metodología
El proyecto consta de 4 archivos de ejecución excluyendo archivos de prueba e imágenes.
Principalmente está el **core.py** el cual como indica su nombre es el núcleo del proyecto, este hereda las clases Numbify, NoGenerated y About. Por útimo consta de los siguientes métodos:

* **openFile**: Accionado por el botón Abrir, el método crea un dialogo de selección de archivo limitado a archivos .csv, una vez abierto procesará la información del archivo si es compatible y la cargará en la tabla (TreeView) en la parte inferior derecha. Es importante destacar que esto solo sucederá si se generó una tabla previamente ya que esto gatilla el proceso de evaluación automática, si se da el caso de accionar el botón sin antes haber generado una escala, se desplegará un dialogo en el que se indica la necesidad de crear una tabla previamente. Puede ocurrir que la tabla no cubra la totalidad de puntos del archivo, por lo que la calificación asignada en ese caso será "Los puntos exceden la escala generada".

* **aboutShow**: Despliega una ventana About llamando a la clase antes importada.

* **generate**: Calcula y muestra una tabla generada según los datos indicados.

* **saveFile**: Guarda los datos desplegados en la tabla, tras cargar un archivo, dentro de un archivo pdf.

### Desarrollado por **Angel Guerrero** y **Yostin Sepúlveda**

#### Gracias especiales a:
**[Ivo Wetzel](https://stackoverflow.com/users/170224/ivo-wetzel)** Por crear el archivo [numbify.py](https://github.com/AngelTheG/Proyecto-3/blob/master/numbify.py) y publicarlo en la página de ayuda de [stack overflow](https://stackoverflow.com/questions/2726839/creating-a-pygtk-text-field-that-only-accepts-number).
  
