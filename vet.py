from os import system
system('cls')

import pandas as pd
immport numpy as np

#crear menu principal


def menu():
    print("Bienvenido a la veterinaria")
    
    print("1. Ver lista completa de clientes")
    print("2. Seleccionar cliente")
    print("3. Agregar cliente")
    print("4. editar datos de cliente")
    print("5. asociar mascota a cliente")
    print("6. salir")
    opcion = input("Ingrese una opcion: ")
    return opcion
    ###

class Mascota:
    def __init__(self, nombre, tipo, edad, peso, sexo, raza, color, ):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.peso = peso
        self.sexo = sexo
        self.raza = raza
        self.color = color
        self.vacunas = []
        self.enfermedades = []
        self.tratamientos = []
        self.citas = []
        self.historia_clinica = []
        self.foto = []
        self.observaciones = []
        self.alergias = []
        self.alimentos = []
        self.esterilizado = False
        self.microchip = False
        self.adoptado = False
        self.fecha_esterilizacion = None
        self.fecha_adopcion = None
        self.fecha_microchip = None
        self.fecha_nacimiento = None
        self.fecha_fallecimiento = None
        self.fecha_ultima_cita = None
        self.fecha_ultima_vacuna = None
        self.fecha_ultima_enfermedad = None
        self.fecha_ultima_historia_clinica = None
        self.fecha_ultima_foto = None
        self.fecha_ultima_observacion = None
        self.fecha_ultima_alergia = None
        self.fecha_ultimo_alimento = None
        self.fecha_ultimo_tratamiento = None
        ###

    def agregar_vacuna(self, vacuna):
        self.vacunas.append(vacuna)
        self.fecha_ultima_vacuna = datetime.now()
        ###
    def agregar_enfermedad(self, enfermedad):
        self.enfermedades.append(enfermedad)
        self.fecha_ultima_enfermedad = datetime.now()
        ###
    def agregar_tratamiento(self, tratamiento):
        self.tratamientos.append(tratamiento)
        self.fecha_ultimo_tratamiento = datetime.now()
        ###
    def agregar_cita(self, cita):
        self.citas.append(cita)
        self.fecha_ultima_cita = datetime.now()
        ###
    def agregar_historia_clinica(self, historia_clinica):
        self.historia_clinica.append(historia_clinica)
        self.fecha_ultima_historia_clinica = datetime.now()
        ###
    def agregar_foto(self, foto):
        self.foto.append(foto)
        self.fecha_ultima_foto = datetime.now()
        ###

    def agregar_observacion(self, observacion):
        self.observaciones.append(observacion)
        self.fecha_ultima_observacion = datetime.now()
        ###
    def agregar_alergia(self, alergia):
        self.alergias.append(alergia)
        self.fecha_ultima_alergia = datetime.now()
        ###
    def agregar_alimento(self, alimento):
        self.alimentos.append(alimento)
        self.fecha_ultimo_alimento = datetime.now()
        ###
    def esterilizar(self):

        if self.esterilizado == False:
            self.esterilizado = True
            self.fecha_esterilizacion = datetime.now()
        else:
            print("La mascota ya esta esterilizada")
            ###
    def microchip(self):
            
            if self.microchip == False:
                self.microchip = True
                self.fecha_microchip = datetime.now()
            else:
                print("La mascota ya tiene microchip")
                ###
    

class Cliente:
    def __init__(self, nombre, apellido, cedula, direccion, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.mascotas = []
        self.fecha_nacimiento = None
        self.fecha_ultima_mascota = None
        ###

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
        self.fecha_ultima_mascota = datetime.now()
        ###
    def agregar_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento
        ###
    def agregar_fecha_ultima_mascota(self, fecha_ultima_mascota):
        self.fecha_ultima_mascota = fecha_ultima_mascota
        ###
    def agregar_fecha_ultima_cita(self, fecha_ultima_cita):
        self.fecha_ultima_cita = fecha_ultima_cita
        ###
    def agregar_fecha_ultima_vacuna(self, fecha_ultima_vacuna):
        self.fecha_ultima_vacuna = fecha_ultima_vacuna
        ###
    def agregar_fecha_ultima_enfermedad(self, fecha_ultima_enfermedad):
        self.fecha_ultima_enfermedad = fecha_ultima_enfermedad
        ###
    

class Veterinario:
    


        







