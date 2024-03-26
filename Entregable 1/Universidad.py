# Realizado por:

### Zhuxun Dong | Sergio Gallego Nicolás ###

"""
Actualizacion 26/3/2024:

- Manejo de excepciones en: MiembroDepartamento, Departamento (para asegurar que el departamento existe), Persona (para asegurar que el sexo es correcto).
- Modificaciones multiples en el metodo __str__ de distintas clases.
- Nuevo atributo en Asignatura: creditos, y un método para su obtencion.
- Modificaciones en implementación del __init__ en Profesor y Estudiante, concretamente con el atributo lista_asignaturas.
- Nuevos metodos en Estudiante y Profesor, debido a la modificación en el atributo lista_asignaturas, para añadir, quitar o mostrar la lista de asignaturas.
- Modificacion en los testeos acorde a los cambios realizados.
"""

import copy
from enum import Enum
from abc import ABCMeta, abstractmethod

class TypeError(Exception):
    pass

class NotFoundError(Exception):
    pass

class RepeatedInstanceError(Exception):
    pass



class Nombre_Departamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3
    SIN_DEPARTAMENTO = 4

class Miembro_Departamento():
    def __init__(self, departamento:Nombre_Departamento):

        if not isinstance(departamento, Nombre_Departamento):
            raise TypeError("El departamento debe ser: DIIC, DITEC, DIS o SIN_DEPARTAMENTO")
        
        else: self.departamento = departamento

    def cambiar_departamento(self, new_dep):
        if isinstance(new_dep, Nombre_Departamento):
            self.departamento = new_dep

        else: raise TypeError("El departamento debe ser: DIIC, DITEC, DIS o SIN_DEPARTAMENTO")

    

class Departamento():
    def __init__(self, nombre_departamento:Nombre_Departamento, miembros:list):

        if not isinstance(nombre_departamento, Nombre_Departamento): #Added some exception management!
            raise TypeError("El departamento debe ser: DIIC, DITEC, DIS o SIN_DEPARTAMENTO")
        
        else:
            self.nombre_departamento = nombre_departamento
            self.miembros = miembros

class Sexo(Enum):
    V = 1
    M = 2
    O = 3

class Persona():
    def __init__(self, nombre:str, dni:str, direccion:str, sexo:Sexo):

        if not isinstance(sexo, Sexo):
            raise TypeError("El sexo es incorrecto")

        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

    
class Investigador(Persona, Miembro_Departamento):
    def __init__(self, nombre:str, dni:str, direccion:str, sexo:Sexo, nombre_departamento:Nombre_Departamento, area_invest:str):
        Persona.__init__(self, nombre, dni, direccion, sexo)
        Miembro_Departamento.__init__(self, nombre_departamento)
        self.area_invest = area_invest
    
    def __str__(self):
        return f"Nombre: {self.nombre} \nDNI:{self.dni} \nDireccion:{self.direccion} \nSexo:{self.sexo} \nDepartamento:{self.departamento} \nArea investigacion:{self.area_invest}"

class Asignatura():
    def __init__(self, nombre:str, creditos:int):
        self.nombre = nombre
        self.creditos = creditos

    def creditos(self): #Added a new attribute
        return self.creditos

class Estudiante(Persona): #Added more class methods and modified the __str__ method
    def __init__(self, nombre:str, dni:str, direccion:str, sexo:Sexo):
        super().__init__(nombre, dni, direccion, sexo)
        self.lista_asignaturas = []

    
    def add_asignatura(self, asignatura):
        if type(asignatura) == list or type(asignatura) == tuple:
            self.lista_asignaturas = copy.copy(asignatura) #Crar una copia para evitar que la lista de asignaturas de estudiantes diferentes tengan la misma referencia

        else: self.lista_asignaturas.append(asignatura)
    
    def rm_asignatura(self, asignatura):
        asig = None
        for i in self.lista_asignaturas:
            if i.nombre == asignatura:
                asig = i
                break
        if asig == None:
            raise NotFoundError("El estudiante no se encuentra matriculada en dicha asignatura!")
        self.lista_asignaturas.remove(asig)
    
    def mostrarAsignaturas(self):
        print("Estudiante: ", self.nombre)
        for i in self.lista_asignaturas:
            print("\t", i.nombre)

    def __str__(self):
        return f"Nombre: {self.nombre} \nDNI:{self.dni} \nDireccion:{self.direccion} \nSexo:{self.sexo}"

class Profesor(): #Added new class method, just like class Estudiante
    def __init__(self):
        self.lista_asignaturas = []
    
    def add_asignaturas(self, asignatura): #Here, asignatura is a either an instance of class Asignatura, or a list (tuple) of that class
        if type(asignatura) == list or type(asignatura) == tuple:
            self.lista_asignaturas = copy.copy(asignatura) #Crar una copia para evitar que la lista de asignaturas de estudiantes diferentes tengan la misma referencia

        else: self.lista_asignaturas.append(asignatura)

    def rm_asignatura(self, asignatura): #asignatura is a string, the name of the assignment we're looking for, not an instance of class Asignatura
        asig = None
        for i in self.lista_asignaturas:
            if i.nombre == asignatura:
                asig = i
                break

        if asig == None:
            raise NotFoundError("El Profesor en cuestion no imparte dicha asignatura!")
        
        self.lista_asignaturas.remove(asig)
    
    def mostrarAsignaturas(self):
        print("Profesor: ", self.nombre)
        for i in self.lista_asignaturas:
            print("\t", i.nombre)



class Profesor_Titular(Profesor, Investigador): #Modified some implementation of __init__ due to changes made in class Profesor
    def __init__(self, nombre: str, dni: str, direccion: str, sexo: Sexo, nombre_departamento:Nombre_Departamento, area_invest:str):
        Profesor.__init__(self) #Operations related to assignments can be done using methods defined in class Profesor (mostrar, add, remove)
        Investigador.__init__(self, nombre, dni, direccion, sexo, nombre_departamento, area_invest)
    
    def __str__(self):
        return f"Nombre: {self.nombre} \nDNI:{self.dni} \nDireccion:{self.direccion} \nSexo:{self.sexo} \nDepartamento:{self.departamento} \nArea investigacion:{self.area_invest}"


class Profesor_Asociado(Persona, Profesor, Miembro_Departamento):
    def __init__(self, nombre: str, dni: str, direccion: str, sexo: Sexo, nombre_departamento:Nombre_Departamento):
        Persona.__init__(self, nombre, dni, direccion, sexo)
        Miembro_Departamento.__init__(self, nombre_departamento)
        Profesor.__init__(self) #Operations related to assignments can be done using methods defined in class Profesor (mostrar, add, remove)
    
    def __str__(self):
        return f"Nombre: {self.nombre} \nDNI:{self.dni} \nDireccion:{self.direccion} \nSexo:{self.sexo} \nDepartamento:{self.departamento}"

class Universidad():
    def __init__(self, departamentos:dict = {}, estudiantes:dict = {}): #Como universidad solo va a haber 1, nos olvidamos del tema de las referencias
        self.departamentos = departamentos
        self.estudiantes = estudiantes
        for nombre_departamento in Nombre_Departamento:
            if nombre_departamento not in self.departamentos.keys():
                self.departamentos[nombre_departamento] = {}
        
    def añadir_miembro_departamento(self, miembro_departamento):
        self.departamentos[miembro_departamento.departamento][miembro_departamento.dni] = miembro_departamento
    
    def eliminar_miembro_departamento(self, dni:str):
        for nombre_departamento in Nombre_Departamento:
            for dni_escapista in self.departamentos[nombre_departamento].keys():
                if dni_escapista == dni:
                    del self.departamentos[nombre_departamento][dni_escapista]
                    break
                
    def cambiar_miembro_departamento(self, dni:str, new_dep:Nombre_Departamento):
        for nombre_departamento in Nombre_Departamento:
            if nombre_departamento != Nombre_Departamento.SIN_DEPARTAMENTO:
                for dni_traidor in self.departamentos[nombre_departamento].keys():
                    if dni_traidor == dni:
                        traidor = self.departamentos[nombre_departamento][dni_traidor]
                        traidor.cambiar_departamento(new_dep)
                        del self.departamentos[nombre_departamento][dni_traidor]
                        self.departamentos[new_dep][dni_traidor] = traidor
                        break
    
    def añadir_estudiante(self, estudiante:Estudiante):
            if estudiante.dni not in self.estudiantes.keys():
                self.estudiantes[estudiante.dni] = estudiante
            
            else:
                raise RepeatedInstanceError("Error: ya existe un estudiante con ese DNI")
        
    def eliminar_estudiante(self, dni:str):
        for dni_estudiante in self.estudiantes.keys():
            if dni_estudiante == dni:
                del self.estudiantes[dni]
                break
    
    def __str__(self): #Modified for a better presentation
        cadena = "Departamentos:\n"
        for i in self.departamentos.keys():
            cadena = cadena + "\t" + str(i) + ":\n"
            for j in self.departamentos[i].keys():
                cadena = cadena + "\t\t" + str(self.departamentos[i][j].nombre) + "\n"

        cadena = cadena + "Estudiantes:\n"
        for i in self.estudiantes.keys():
            cadena = cadena + "\t" + str(self.estudiantes[i].nombre) + "\n"

        return cadena
    
### TESTING ###

if __name__ == "__main__":
    Uni = Universidad()
    asignaturas = [Asignatura("PCDD", 6), Asignatura("SYS", 6), Asignatura("AEM",6), Asignatura("BBDD II",6), Asignatura("ML I",6)]

    estudiante = Estudiante(nombre="Zhuxun Dong", dni="69420KKK", direccion="Su casa", sexo=Sexo.M)
    profTitular = Profesor_Titular(nombre="Manuel Pulido", dni="idgaf123", direccion = "Murcia quizas", sexo = Sexo.M, nombre_departamento=Nombre_Departamento.DITEC, area_invest = "Optimizacion")
    profAsociado = Profesor_Asociado(nombre="Antonio Lobato", dni="wawedaw0", direccion = "Murcia desde luego no", sexo=Sexo.M, nombre_departamento=Nombre_Departamento.DIS)
    print(estudiante)
    print(profTitular)
    print(profAsociado)

    estudiante.add_asignatura(asignaturas)
    profTitular.add_asignaturas(asignaturas[0:2])
    profAsociado.add_asignaturas(asignaturas[3])
    estudiante.mostrarAsignaturas()
    profTitular.mostrarAsignaturas()
    profAsociado.mostrarAsignaturas()


    Uni.añadir_estudiante(estudiante)
    Uni.añadir_miembro_departamento(profTitular)
    Uni.añadir_miembro_departamento(profAsociado)
    print(Uni)

    
    Uni.cambiar_miembro_departamento(dni=profTitular.dni,new_dep=Nombre_Departamento.DIS)
    Uni.eliminar_estudiante(dni="69420KKK")
    Uni.eliminar_miembro_departamento(dni="wawedaw0")
    print(Uni)
