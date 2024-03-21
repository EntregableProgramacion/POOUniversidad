# Realizado por:

### Zhuxun Dong | Sergio Gallego Nicolás ###



from enum import Enum
from abc import ABCMeta, abstractmethod

class Nombre_Departamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3
    SIN_DEPARTAMENTO = 4

class Miembro_Departamento():
    def __init__(self, departamento:Nombre_Departamento):
        self.departamento = departamento

class Departamento():
    def __init__(self, nombre_departamento:Nombre_Departamento, miembros:list):
        self.nombre_departamento = nombre_departamento
        self.miembros = miembros

class Sexo(Enum):
    V = 1
    M = 2
    O = 3

class Persona():
    def __init__(self, nombre:str, dni:str, direccion:str, sexo:Sexo):
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
        return f"[{self.nombre}, {self.dni}, {self.direccion}, {self.sexo}, {self.departamento}, {self.area_invest}]"

class Asignatura():
    def __init__(self, nombre:str):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre:str, dni:str, direccion:str, sexo:Sexo, asignaturas:list = []):
        super().__init__(nombre, dni, direccion, sexo)
        self.lista_asignaturas = asignaturas
    
    def __str__(self):
        return f"[{self.nombre}, {self.dni}, {self.direccion}, {self.sexo}, {self.lista_asignaturas}]"

class Profesor():
    def __init__(self, lista_asignaturas:list = []):
        self.lista_asignaturas = lista_asignaturas

class Profesor_Titular(Profesor, Investigador):
    def __init__(self, nombre: str, dni: str, direccion: str, sexo: Sexo, nombre_departamento:Nombre_Departamento, area_invest:str , asignaturas: list = []):
        Profesor.__init__(self, asignaturas)
        Investigador.__init__(self, nombre, dni, direccion, sexo, nombre_departamento, area_invest)
    
    def __str__(self):
        return f"[{self.nombre}, {self.dni}, {self.direccion}, {self.sexo}, {self.departamento}, {self.area_invest}, {self.lista_asignaturas}]"


class Profesor_Asociado(Persona, Profesor, Miembro_Departamento):
    def __init__(self, nombre: str, dni: str, direccion: str, sexo: Sexo, nombre_departamento:Nombre_Departamento, asignaturas: list = []):
        Persona.__init__(self, nombre, dni, direccion, sexo)
        Miembro_Departamento.__init__(self, nombre_departamento)
        Profesor.__init__(self, asignaturas)
    
    def __str__(self):
        return f"[{self.nombre}, {self.dni}, {self.direccion}, {self.sexo}, {self.departamento}, {self.lista_asignaturas}]"

class Universidad():
    def __init__(self, departamentos:dict = {}, estudiantes:dict = {}):
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
                        del self.departamentos[nombre_departamento][dni_traidor]
                        self.departamentos[new_dep][dni_traidor] = traidor
                        break
    
    def añadir_estudiante(self, estudiante:Estudiante):
        try:
            if estudiante.dni not in self.estudiantes.keys():
                self.estudiantes[estudiante.dni] = estudiante
        except:
            raise Exception("Error: ya existe un estudiante con ese dni")
        
    def eliminar_estudiante(self, dni:str):
        for dni_estudiante in self.estudiantes.keys():
            if dni_estudiante == dni:
                del self.estudiantes[dni]
                break
    
    def __str__(self):
        return f"{self.departamentos}\n___\n{self.estudiantes}\n"
    
### TESTING ###

if __name__ == "__main__":
    Uni = Universidad()
    
    print(Uni)
    estudiante = Estudiante(nombre="Zhuxun Dong", dni="69420KKK", direccion="Su casa", sexo=Sexo.O, asignaturas=[Asignatura("PCDD"), Asignatura("SYS"), Asignatura("AEM"), Asignatura("BBDD II"), Asignatura("ML I")])
    print(estudiante)
    Uni.añadir_estudiante(estudiante)
    print(Uni)
    miembro_departamento = Investigador(nombre="Dominga", dni="78933X", direccion="Av. Pinos 1224", sexo=Sexo.M, nombre_departamento=Nombre_Departamento.DITEC, area_invest="Huevos")
    print(miembro_departamento)
    Uni.añadir_miembro_departamento(miembro_departamento)
    print(Uni)
    Uni.cambiar_miembro_departamento(dni="78933X",new_dep=Nombre_Departamento.DIS)
    print(Uni)
    Uni.eliminar_estudiante(dni="69420KKK")
    print(Uni)
    Uni.eliminar_miembro_departamento(dni="78933X")
    print(Uni)
    
    