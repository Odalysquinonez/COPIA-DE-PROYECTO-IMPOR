from statistics import mode

from PySide6 import QtGui
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox
from UI.Vtn_principal import Ui_VTNWindow
from datos.estudiante_dao import EstudianteDao
from dominio.Docente import Docente
from dominio.Estudiante import Estudiante



class PersonaPrincipal(QMainWindow):

    def __init__(self):
        super(PersonaPrincipal,self).__init__()
        self.ui = Ui_VTNWindow()
        self.ui.setupUi(self)
        self.ui.stb_menu_barra_estado.showMessage("Bienvenido",2000)
        self.ui.btn_Grabar.clicked.connect(self.grabar)
        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())
        self.ui.btn_buscar_cedula.clicked.connect(self.buscar_x_cedula)
        self.ui.btn_estatura.clicked.connect(self.calculos_estatura)
        self.ui.btn_peso.clicked.connect(self.calculos_peso)
        correo_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        validator = QRegularExpressionValidator(correo_exp, self)
        self.ui.txt_email.setValidator(validator)

    def grabar(self):
        tipo_persona = self.ui.cb_tipo_persona.currentText()
        if self.ui.txt_Nombre.text() == "" or self.ui.txt_Apellido.text() == "" \
                or len(self.ui.txt_cedula.text())  <10 or self.ui.txt_email.text() == "":
            print("Completar Datos")
            QMessageBox.warning(self, 'Advertencia', 'Falta de llenar los datos obligatorios')
        else:
            persona = None
            if tipo_persona == "Docente":
                persona = Docente()
                persona.nombre = self.ui.txt_Nombre.text()
                persona.apellido = self.ui.txt_Apellido.text()
                persona.cedula = self.ui.txt_cedula.text()
                persona.email = self.ui.txt_email.text()
                persona.carrera = self.ui.txt_carrera.text()
                persona.estatura = self.ui.sp_estatura_2.text()
                persona.peso = self.ui.sp_peso.text()
            else:
                persona = Estudiante()
                persona.nombre = self.ui.txt_Nombre.text()
                persona.apellido = self.ui.txt_Apellido.text()
                persona.cedula = self.ui.txt_cedula.text()
                persona.email = self.ui.txt_email.text()
                persona.carrera = self.ui.txt_carrera.text()
                persona.estatura = self.ui.sp_estatura_2.text()
                persona.peso = self.ui.sp_peso.text()
                #insertar en la base de datos al estudiante
                respuesta = None
                try:
                    respuesta = EstudianteDao.insertar_estudiante(persona)
                except Exception as e:
                     print(e)

            #archivo = None
            #try:
                #archivo = open("archivo.txt", mode="a")
                #archivo.write(persona.__str__())
                #archivo.write("\n")
            #except Exception as e:
                #print("No se pudo grabar")
            #finally:
                #if archivo:
                    #archivo.close()
            if respuesta['exito']:
                self.ui.txt_Nombre.setText("")
                self.ui.txt_Apellido.setText("")
                self.ui.txt_cedula.setText("")
                self.ui.txt_email.setText("")
                self.ui.txt_carrera.setText("")
                self.ui.sp_estatura_2.setValue(0)
                self.ui.sp_peso.setValue(0)
                self.ui.stb_menu_barra_estado.showMessage("Grabado con Éxito", 2000)
            else:
                QMessageBox.critical(self, 'Error', respuesta['mensaje'])
    def buscar_x_cedula(self):
        cedula = self.ui.txt_cedula.text()
        e = Estudiante(cedula=cedula)
        e = EstudianteDao.seleccionar_por_cedula(e)
        self.ui.txt_Nombre.setText(e.nombre)
        self.ui.txt_Apellido.setText(e.apellido)
        self.ui.txt_email.setText(e.email)
        self.ui.txt_carrera.setText(e.carrera)
        self.ui.cb_tipo_persona.setCurrentText('Estudiante')

    def calculos_estatura(self):
        global estudiante
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        suma_estaturas = 0
        estaturas= list()
        for estudiante in estudiantes:
            suma_estaturas += estudiante.estatura
            estaturas.append(estudiante.estatura)
        promedio_estatura = suma_estaturas // cantidad_estudiantes
        media_estatura = sorted(estaturas)[cantidad_estudiantes // 2]
        moda_estatura = mode(estaturas)
        minimo_estatura = min(estaturas)
        maximo_estatura = max(estaturas)
        print('')
        print(f'------------ESTATURA---------------------')
        print(f'Promedio de estaturas: {promedio_estatura}')
        print(f'Media de estaturas: {media_estatura}')
        print(f'Moda de estaturas: {moda_estatura}')
        print(f'Mínimo de estaturas: {minimo_estatura}')
        print(f'Máximo de estaturas: {maximo_estatura}')


    def calculos_peso(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        suma_pesos = 0
        pesos= list()
        for estudiante in estudiantes:
            suma_pesos += estudiante.peso
            pesos.append(estudiante.peso)
        promedio_peso = suma_pesos // cantidad_estudiantes
        media_peso = sorted(pesos)[cantidad_estudiantes // 2]
        moda_peso = mode(pesos)
        minimo_peso = min(pesos)
        maximo_peso = max(pesos)

        print('')
        print('------------PESO---------------------')
        print(f'Promedio de pesos: {promedio_peso}')
        print(f'Media de pesos: {media_peso}')
        print(f'Moda de pesos: {moda_peso}')
        print(f'Mínimo de pesos: {minimo_peso}')
        print(f'Máximo de pesos: {maximo_peso}')





