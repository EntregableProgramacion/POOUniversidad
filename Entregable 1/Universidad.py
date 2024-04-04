# Realizado por:

### Zhuxun Dong | Sergio Gallego Nicolás ###

import copy
from enum import Enum


class TypeError(Exception):
    """Excepción causada por un error de escritura."""
    pass

class NotFoundError(Exception):
    """Excepción causada por la ausencia de un elemento de búsqueda."""
    pass

class RepeatedInstanceError(Exception):
    """Excepción causada por un error de sobreescritura."""
    pass



class Nombre_Departamento(Enum):
    """Enumeración que identifica los 3 departamentos existentes y la posibilidad de no pertenecer a ningun departamento."""
    DIIC = 1
    DITEC = 2
    DIS = 3
    SIN_DEPARTAMENTO = 4


class Miembro_Departamento():
    """Clase destinada a usarse con herencia en Investigador y Profesor Asociado.\nLas instancias de esta clase
       forman parte de un departamento."""
    
    def __init__(self, departamento:Nombre_Departamento):
        """Se inicializa un parámetro: una instancia de la enumeración <Nombre_Departamento> que identifica el 
           departamento del que es miembro esta instancia."""
        
        if isinstance(departamento, Nombre_Departamento):
            self.departamento = departamento
        
        else:
            raise TypeError("El departamento debe ser: DIIC, DITEC, DIS o SIN_DEPARTAMENTO")

    def cambiar_departamento(self, new_dep):
        """Cambiar de departamento a un Miembro de Departamento.\nEl nuevo departamento debe ser una instancia de
           la enumeración <Nombre_Departamento>."""
        
        if isinstance(new_dep, Nombre_Departamento):
            self.departamento = new_dep

        else: 
            raise TypeError("El departamento debe ser: DIIC, DITEC, DIS o SIN_DEPARTAMENTO")


class Departamento():
    """Clase destinada a modelar los distintos departamentos de la Universidad."""
    
    def __init__(self, nombre_departamento:Nombre_Departamento, miembros:list):
        """Se inicializan dos parámetros: una instancia de la enumeración <Nombre_Departamento> que identifica el 
           departamento, y una lista de <Miembro_Departamento> que contiene los miembros de este departamento."""
        
        if isinstance(nombre_departamento, Nombre_Departamento):
            self.nombre_departamento = nombre_departamento
            self.miembros = miembros
        
        else:
            raise TypeError("El departamento debe ser: DIIC, DITEC, DIS o SIN_DEPARTAMENTO")


class Sexo(Enum): #Eliminada la opción "O" para ajustarse a los requisitos del programa.
    """Enumeración que identifica los 2 sexos."""
    V = 1
    M = 2


class Persona():
    """Clase destinada a usarse con herencia en: Investigador, Profesor Titular, Profesor Asociado y Estudiante."""
    
    def __init__(self, nombre:str, dni:str, direccion:str, sexo:Sexo):
        """Se inicializan cuatro parámetros: un string que se corresponde con el nombre de la persona, otro string
        que se corresponde con el DNI de la misma (8 dígitos y 1 letra), un último string que se corresponde con
        la dirección de la persona en cuestión, y una instancia de la enumeración <Sexo>, que identifica el sexo
        de la persona."""
        
        if isinstance(sexo, Sexo):
            self.nombre = nombre
            self.dni = dni
            self.direccion = direccion
            self.sexo = sexo
        else:
            raise TypeError("El sexo es incorrecto")


class Investigador(Persona, Miembro_Departamento):
    """Permite la instanciación de investigadores ordinarios y de profesores titulares mediante herencia."""
    
    def __init__(self, nombre:str, dni:str, direccion:str, sexo:Sexo, nombre_departamento:Nombre_Departamento, area_invest:str):
        """Se emplea herencia de las clases <Persona> y de <Miembro_Departamento>, por lo que se requieren los 
           atributos de éstas para instanciar esta clase.\nAdemás se inicializa un parámetro: un string que se
           corresponde con el área de investigación del investigador."""
        
        Persona.__init__(self, nombre, dni, direccion, sexo)
        Miembro_Departamento.__init__(self, nombre_departamento)
        self.area_invest = area_invest
    
    def __str__(self):
        """Modificación del método nativo de impresión por pantalla para facilitar la comprensión."""
        
        return f"Nombre: {self.nombre} \nDNI:{self.dni} \nDireccion:{self.direccion} \nSexo:{self.sexo} \nDepartamento:{self.departamento} \nArea investigacion:{self.area_invest}"

class Asignatura():
    """Para la instanciación de las distintas asignaturas que se cursan con la intención de permitir extensibilidad."""
    
    def __init__(self, nombre:str, creditos:int):
        """Se inicializan 2 parámetros: un string que identificará la asignatura y un int que se corresponde con 
           el número de créditos de la misma."""
        
        self.nombre = nombre
        self.creditos = creditos

    def get_creditos(self):
        """Devuelve los créditos de la asignatura."""
        
        return self.creditos


class Estudiante(Persona):
    """Usuario de la Universidad que cursa alguna asignatura."""
    
    def __init__(self, nombre:str, dni:str, direccion:str, sexo:Sexo):
        """Se emplea herencia de la clase <Persona>, por lo que se requieren los atributos de ésta para instanciar
           esta clase.\nAdemás se inicializa un parámetro: una lista vacía que se corresponde con las asignaturas
           que cursa el estudiante."""
        
        super().__init__(nombre, dni, direccion, sexo)
        self.lista_asignaturas = []

    
    def add_asignatura(self, asignatura):
        """Dada una lista/tupla de asignaturas, se tratará a dicha lista/tupla como la totalidad de las asignaturas
           que cursa el estudiante.\nDada una única asignatura, en formato string, se añadirá dicha asignatura al 
           listado de asignaturas que cursa el estudiante."""
        
        if type(asignatura) == list or type(asignatura) == tuple:
            self.lista_asignaturas = copy.copy(asignatura) #Crar una copia para evitar que la lista de asignaturas de estudiantes diferentes tengan la misma referencia

        elif type(asignatura) == str:
            self.lista_asignaturas.append(asignatura)
        
        else:
            TypeError(f"Error: Las asignaturas deben tener formato <string>, <list> o <tuple>.\nNo se acepta el formato <{type(asignatura)}>.")
    
    def rm_asignatura(self, asignatura:str):
        """Dado el nombre de una asignatura, si el estudiante la estaba cursando dejará de reflejarse este hecho
           en la lista de asignaturas que curse. Si se el estuidiante no estaba cursando dicha asignatura, se
           devuelve una excepción: <NotFoundError>."""
        
        asig = None
        for i in self.lista_asignaturas:
            if i.nombre == asignatura:
                asig = i
                break
        
        if asig == None:
            raise NotFoundError("El/La estudiante no se encuentra matriculado/a en dicha asignatura!")
        else:
            self.lista_asignaturas.remove(asig)
    
    def mostrarAsignaturas(self):
        """Muestra por pantalla la totalidad de las asignaturas que está cursando el estudiante."""
        
        print("Estudiante: ", self.nombre)
        for i in self.lista_asignaturas:
            print("\t", i.nombre)

    def __str__(self): #Modificado para facilitar la comprensión.
        """Modificación del método nativo de impresión por pantalla para facilitar la comprensión."""
        
        return f"Estudiante: <{self.nombre}> \nDNI: <{self.dni}> \nDirección: <{self.direccion}> \nSexo: <{self.sexo.name}>"

class Profesor():
    """Clase destinada a usarse con herencia en: Profesor Titular y Profesor Asociado."""
    
    def __init__(self):
        """Se inicializa un parámetro: una lista que se corresponde con las asignaturas que imparte el profesor."""
        
        self.lista_asignaturas = []
    
    def add_asignaturas(self, asignatura):
        """Dada una lista/tupla de asignaturas, se tratará a dicha lista/tupla como la totalidad de las asignaturas
           que imparte el profesor.\nDada una única asignatura, en formato string, se añadirá dicha asignatura al 
           listado de asignaturas que imparte el profesor."""
        
        if type(asignatura) == list or type(asignatura) == tuple:
            self.lista_asignaturas = copy.copy(asignatura) #Crar una copia para evitar que la lista de asignaturas de estudiantes diferentes tengan la misma referencia

        else: self.lista_asignaturas.append(asignatura)

    def rm_asignatura(self, asignatura:str):
        """Dado el nombre de una asignatura, si el profesor la estaba impartiendo dejará de reflejarse este hecho
           en la lista de asignaturas que imparta. Si se el profesor no estaba impartiendo dicha asignatura, se
           devuelve una excepción: <NotFoundError>."""
        
        asig = None
        for i in self.lista_asignaturas:
            if i.nombre == asignatura:
                asig = i
                break

        if asig == None:
            raise NotFoundError("El Profesor en cuestion no imparte dicha asignatura!")
        else:
            self.lista_asignaturas.remove(asig)
    
    def mostrarAsignaturas(self):
        """Muestra por pantalla la totalidad de las asignaturas que está impartiendo el profesor."""
        
        print("Profesor: ", self.nombre)
        for i in self.lista_asignaturas:
            print("\t", i.nombre)


class Profesor_Titular(Profesor, Investigador):
    """Profesores que realizan tereas de investigación."""
    
    def __init__(self, nombre: str, dni: str, direccion: str, sexo: Sexo, nombre_departamento: Nombre_Departamento, area_invest: str):
        """Se emplea herencia de las clases <Profesor> e <Investigador>, por lo que se requieren los atributos de 
           éstas para instanciar esta clase."""
        
        Profesor.__init__(self)
        Investigador.__init__(self, nombre, dni, direccion, sexo, nombre_departamento, area_invest)
    
    def __str__(self): #Modificado para facilitar la comprensión.
        """Modificación del método nativo de impresión por pantalla para facilitar la comprensión."""
        
        return f"Profesor Titular: <{self.nombre}> \nDNI: {self.dni} \nDirección: <{self.direccion}> \nSexo: <{self.sexo.name}> \nDepartamento: <{self.departamento.name}> \nÁrea Investigación: <{self.area_invest}>"


class Profesor_Asociado(Persona, Profesor, Miembro_Departamento):
    def __init__(self, nombre: str, dni: str, direccion: str, sexo: Sexo, nombre_departamento:Nombre_Departamento):
        """Se emplea herencia de las clases <Persona>, <Profesor> y <Miembro_Departamento>, por lo que se 
           requieren los atributos de éstas para instanciar esta clase."""
        
        Persona.__init__(self, nombre, dni, direccion, sexo)
        Profesor.__init__(self)
        Miembro_Departamento.__init__(self, nombre_departamento)
    
    def __str__(self): #Modificado para facilitar la comprensión.
        """Modificación del método nativo de impresión por pantalla para facilitar la comprensión."""
        
        return f"Profesor Asociado: {self.nombre} \nDNI: {self.dni} \nDireccion: {self.direccion} \nSexo: {self.sexo.name} \nDepartamento: {self.departamento.name}"

class Universidad():
    """Gestor de Estudiantes y Miembros de Departamento."""
    
    def __init__(self):
        """Se inicializan dos diccionarios: el que contendrá a los estudiantes referenciados por sus respectivos 
           dni, y el de los departamentos, que contendrá cada una de las instancias de Departamento referenciadas 
           por sus respectivos nombres."""
        
        self.departamentos = {}
        self.estudiantes = {}
        
        for nombre_departamento in Nombre_Departamento:
            if nombre_departamento not in self.departamentos.keys():
                self.departamentos[nombre_departamento] = {}
    
    def añadir_miembro_departamento(self, miembro_departamento):
        """Dado un miembro de departamento, que puede ser una instancia de: <Profesor_Titular>, <Investigador> o 
           <Profesor_Asociado>. Se añade la nueva instancia al departamento correspondiente"""
        
        if isinstance(miembro_departamento, Profesor_Titular) or isinstance(miembro_departamento, Investigador) or isinstance(miembro_departamento, Profesor_Asociado):
            self.departamentos[miembro_departamento.departamento][miembro_departamento.dni] = miembro_departamento
        
        else:
            raise TypeError("El nuevo miembro de departamento debe ser: <Profesor_Titular>, <Investigador> o <Profesor_Asociado>")
    
    def eliminar_miembro_departamento(self, dni:str):
        """Dado un string llamado "dni", elimina al miembro de departamento para el que el atributo DNI coincida
           con el string proporcionado.\nEn caso de no encontrar ningun miembro de departamento con ese DNI, 
           devuelve una excepción: <NotFoundError>."""
        
        Error = True
        
        for nombre_departamento in Nombre_Departamento:
            for dni_escapista in self.departamentos[nombre_departamento].keys():
                if dni_escapista == dni:
                    Error = False
                    del self.departamentos[nombre_departamento][dni_escapista]
                    break
        
        if Error:
            raise NotFoundError(f"No existe ningun miembro de departamento con el dni: <{dni}>!")
                
    def cambiar_miembro_departamento(self, dni:str, new_dep:Nombre_Departamento):
        """Dado un string llamado "dni" y una instancia de <Nombre_Departamento>, busca al miembro de departamento
           para el que el atributo DNI coincida con el string proporcionado y ejecuta el método "cambiar_departamento"
           implementado en <Miembro_Departamento> para cambiar el valor del atributo "Departamento" de dicho miembro
           de departamento.\nEn caso de no encontrar ningun miembro de departamento con ese DNI, devuelve una 
           excepción: <NotFoundError>."""
        
        Error = True
        
        for nombre_departamento in Nombre_Departamento:
            if nombre_departamento != Nombre_Departamento.SIN_DEPARTAMENTO:
                for dni_traidor in self.departamentos[nombre_departamento].keys():
                    if dni_traidor == dni:
                        Error = False
                        traidor = self.departamentos[nombre_departamento][dni_traidor]
                        traidor.cambiar_departamento(new_dep)
                        del self.departamentos[nombre_departamento][dni_traidor]
                        self.departamentos[new_dep][dni_traidor] = traidor
                        break
        
        if Error:
            raise NotFoundError(f"No existe ningun miembro de departamento con el dni: <{dni}>!")
    
    def añadir_estudiante(self, estudiante:Estudiante):
        """Dada una instancia de la clase <Estudiante>, si no hay ninguna otra instancia con el mismo valor
           para DNI (qué no debería, puesto que es un identificador), se añade la instancia al diccionario 
           de estudiantes."""
        
        if estudiante.dni not in self.estudiantes.keys():
            self.estudiantes[estudiante.dni] = estudiante
        
        else:
            raise RepeatedInstanceError("Error: ya existe un estudiante con ese DNI")
        
    def eliminar_estudiante(self, dni:str):
        """Dado un string llamado "dni", elimina al estudiante para el que el atributo DNI coincida con el string 
           proporcionado.\nEn caso de no encontrar ningun estudiante con ese DNI, devuelve una 
           excepción: <NotFoundError>."""
        
        Error = True
        
        for dni_estudiante in self.estudiantes.keys():
            if dni_estudiante == dni:
                Error = False
                del self.estudiantes[dni]
                break
        
        if Error:
            raise NotFoundError(f"No existe ningun estudiante con el dni: <{dni}>!")
    
    def __str__(self): #Modificado para facilitar la comprensión.
        """Modificación del método nativo de impresión por pantalla para facilitar la comprensión."""
        
        cadena = "Departamentos:\n"
        for i in self.departamentos.keys():
            cadena = cadena + "\t" + str(i.name) + ":\n"
            for j in self.departamentos[i].keys():
                cadena = cadena + "\t\t" + " <" + str(self.departamentos[i][j].__class__.__name__) + "> " + str(self.departamentos[i][j].nombre) + "   DNI: " + str(self.departamentos[i][j].dni) + "\n"

        cadena = cadena + "Estudiantes:\n"
        for i in self.estudiantes.keys():
            cadena = cadena + "\t" + str(self.estudiantes[i].nombre) + "   DNI: " + str(self.estudiantes[i].dni) + "\n"

        return cadena
    
### TESTING ###

if __name__ == "__main__":
    Uni = Universidad()
    asignaturas = [Asignatura("PCDD", 6), Asignatura("SYS", 6), Asignatura("AEM",6), Asignatura("BBDD II",6), Asignatura("ML I",6)]

    estudiante = Estudiante(nombre="Zhuxun Dong", dni="69420KKK", direccion="Su casa", sexo=Sexo.M)
    profTitular = Profesor_Titular(nombre="Manuel Pulido", dni="idgaf123", direccion = "Murcia quizás", sexo = Sexo.M, nombre_departamento=Nombre_Departamento.DITEC, area_invest = "Optimización")
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
    print(Uni)
    Uni.eliminar_estudiante(dni="69420KKK")
    print(Uni)
    Uni.eliminar_miembro_departamento(dni="wawedaw0")
    print(Uni)
