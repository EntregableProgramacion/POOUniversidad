import pytest
import Universidad

def test_asignaturas():
    asignaturas = [Universidad.Asignatura("PCDD", 6), Universidad.Asignatura("SYS", 6), Universidad.Asignatura("AEM",6), Universidad.Asignatura("BBDD II",6), Universidad.Asignatura("ML I",6)]
    l = len(asignaturas)
    estudiante = Universidad.Estudiante(nombre="alberto", dni = "asda", direccion="aaaa", sexo= Universidad.Sexo.M)
    profesor = Universidad.Profesor()
    estudiante.add_asignatura(asignaturas)
    profesor.add_asignaturas(asignaturas)

    assert((l == len(estudiante.lista_asignaturas)) and (l == len(profesor.lista_asignaturas)))

def test_eliminar_estudiante_miembroDep():
    Uni = Universidad.Universidad()
    ProfAsociado = Universidad.Profesor_Asociado(nombre="Antonio Lobato", dni="wawedaw0", direccion = "Murcia desde luego no", sexo=Universidad.Sexo.M, nombre_departamento=Universidad.Nombre_Departamento.DIS)
    Uni.añadir_miembro_departamento(ProfAsociado)
    Uni.eliminar_miembro_departamento(dni="wawedaw0")

    estudiante = Universidad.Estudiante(nombre="alberto", dni = "asda", direccion="aaaa", sexo= Universidad.Sexo.M)
    Uni.añadir_estudiante(estudiante)
    Uni.eliminar_estudiante(estudiante.dni)
    assert((len(Uni.departamentos[Universidad.Nombre_Departamento.DIS]) == 0) and (len(Uni.estudiantes) == 0))


def test_add_estudiante_miembroDep():
    Uni = Universidad.Universidad()
    ProfAsociado = Universidad.Profesor_Asociado(nombre="a", dni="bb", direccion = "Murcia desde luego no", sexo=Universidad.Sexo.M, nombre_departamento=Universidad.Nombre_Departamento.DIS)
    estudiante = Universidad.Estudiante(nombre="vc", dni = "awdsd", direccion="aaaa", sexo= Universidad.Sexo.M)

    Uni.añadir_estudiante(estudiante)
    Uni.añadir_miembro_departamento(ProfAsociado)

    assert((ProfAsociado.dni in Uni.departamentos[ProfAsociado.departamento].keys()) and (estudiante.dni in Uni.estudiantes))

def test_cambio_dep():
    Uni = Universidad.Universidad()
    profTitular = Universidad.Profesor_Titular(nombre="Antonio Lobato", dni="wawedaw0", direccion = "Murcia desde luego no", sexo=Universidad.Sexo.M, nombre_departamento=Universidad.Nombre_Departamento.DIS, area_invest="F1")
    Uni.añadir_miembro_departamento(profTitular)
    Uni.cambiar_miembro_departamento(dni = profTitular.dni, new_dep=Universidad.Nombre_Departamento.DITEC)

    assert(profTitular.departamento == Universidad.Nombre_Departamento.DITEC)