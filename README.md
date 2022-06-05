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

[ ===== IMAGEN ===== ]


## Primer Lanzamiento
Apenas se ejecute el proyecto se abrirá la ventana núcleo del proyecto.

[ ===== IMAGEN ===== ]

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

### Desarrollado por **Angel Guerrero**

#### Gracias especiales a:
**[Ivo Wetzel](https://stackoverflow.com/users/170224/ivo-wetzel)** Por crear el archivo [numbify.py](https://github.com/AngelTheG/Proyecto-3/blob/master/numbify.py) y publicarlo en la página de ayuda de [stack overflow](https://stackoverflow.com/questions/2726839/creating-a-pygtk-text-field-that-only-accepts-number).
  
