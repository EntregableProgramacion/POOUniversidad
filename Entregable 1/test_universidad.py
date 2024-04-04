import pytest
from Universidad import *

def test_asignaturas():
    asignaturas = [Asignatura("PCDD", 6), Asignatura("SYS", 6), Asignatura("AEM",6), Asignatura("BBDD II",6), Asignatura("ML I",6)]
    l = len(asignaturas)
    estudiante = Estudiante(nombre = "alberto", dni = "asda", direccion = "aaaa", sexo = Sexo.M)
    profesor = Profesor()
    estudiante.add_asignatura(asignaturas)
    profesor.add_asignaturas(asignaturas)

    assert((l == len(estudiante.lista_asignaturas)) and (l == len(profesor.lista_asignaturas)))


def test_add_estudiante():
    Uni = Universidad()
    estudiante = Estudiante(nombre = "vc", dni = "awdsd", direccion = "aaaa", sexo = Sexo.M)

    Uni.añadir_estudiante(estudiante)
    
    assert(estudiante.dni in Uni.estudiantes)


def test_add_miembroDep():
    Uni = Universidad()
    ProfAsociado = Profesor_Asociado(nombre = "a", dni = "bb", direccion = "Murcia desde luego no", sexo = Sexo.M, nombre_departamento = Nombre_Departamento.DIS)
    
    Uni.añadir_miembro_departamento(ProfAsociado)

    assert(ProfAsociado.dni in Uni.departamentos[ProfAsociado.departamento].keys())


def test_eliminar_estudiante():
    Uni = Universidad()
    estudiante = Estudiante(nombre = "alberto", dni = "asda", direccion = "aaaa", sexo = Sexo.M)
    Uni.añadir_estudiante(estudiante)
    
    Uni.eliminar_estudiante(estudiante.dni)
    
    assert(len(Uni.estudiantes) == 0)
    

def test_eliminar_miembroDep():
    Uni = Universidad()
    ProfAsociado = Profesor_Asociado(nombre = "Antonio Lobato", dni = "wawedaw0", direccion = "Murcia desde luego no", sexo = Sexo.M, nombre_departamento = Nombre_Departamento.DIS)
    Uni.añadir_miembro_departamento(ProfAsociado)
    
    Uni.eliminar_miembro_departamento(dni = "wawedaw0")
    
    assert(len(Uni.departamentos[Nombre_Departamento.DIS]) == 0)


def test_cambio_dep():
    Uni = Universidad()
    profTitular = Profesor_Titular(nombre = "Antonio Lobato", dni = "wawedaw0", direccion = "Murcia desde luego no", sexo = Sexo.M, nombre_departamento = Nombre_Departamento.DIS, area_invest = "F1")
    Uni.añadir_miembro_departamento(profTitular)
    
    Uni.cambiar_miembro_departamento(dni = profTitular.dni, new_dep = Nombre_Departamento.DITEC)

    assert(profTitular.departamento == Nombre_Departamento.DITEC)