# INTEGRANTES:
# MERO SARCOS CAROLINE THALIA
# QUIÑONEZ JAIME SERGIO AURELIO
# QUIÑONEZ RONQUILLO ODALYS RAQUEL

from dominio.Persona import Persona

class Estudiante(Persona):
    contador_estudiante = 0

    def __init__(self, cedula: str = None, nombre: str = None, apellido: str = None, email: str = None,
                 telefono: str = None, direccion: str = None,
                 numero_libros: int = 0, activo: bool = True, carrera: str = None, nivel: int = 1, estatura=None, peso=None):
        #Estudiante.contador_estudiante += 1

        self._id = 1
        self._nivel = nivel
        super(Estudiante, self).__init__(cedula=cedula, nombre=nombre, apellido=apellido, email=email,
                                         telefono=telefono, direccion=direccion, numero_libros=numero_libros,
                                         activo=activo, carrera=carrera,estatura=estatura, peso=peso)

    def __str__(self):
        return f' Estudiante : {self.__dict__.__str__()}'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @classmethod
    def pedir_libro(self) -> bool:
        pass

    @classmethod
    def devolver_libro(self) -> bool:
        pass


if __name__ == '__main__':
    e1 = Estudiante(cedula='0932548449', nombre='joseph', apellido='paez', email='josephsamuelpaez@gmail.com',
                    telefono='0984902300', direccion='mapasingue ', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)
    e2 = Estudiante(cedula='0915459077', nombre='viviana', apellido='caice', email='vcaicezuniga1978@gmail.com',
                    telefono='0979512906', direccion='centro sur', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)
    e3 = Estudiante(cedula='0953509502', nombre='alejandra', apellido='barrera',
                    email=' alejandrabarrera0207@gmail.com',
                    telefono='0979262951', direccion='daule', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)
    e4 = Estudiante(cedula='0952308245', nombre='jamilet', apellido='pillasagua', email='jamifernanda@gmail.com',
                    telefono='0989475023', direccion='sauces', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)

    print(e1)
    print(e2)
    print(e3)
    print(e4)