# Práctica 5 Manejo de métodos
# Jesús Preciado

# Manipulación de las luces exteriores e interores en 60 minutos

# 4 tiempos 15 min
# 4 tonos
# 2 colores

# trigger

# Declaración de Variables

varLapso = 15

varColorI = "#f7ff87"
varColorF = "#FFF"

varTono1 = .25
varTono2 = .5
varTono3 = .75
varTono4 = 1

# declaracion de funciones

def inicio():
    etapaUno()
    
def finalizar():
    print("Luces encendidas a todo color.")
       
def timer(minutos):
    print("Inicio conteo de 15" + str(minutos))
    #falta funcion que cuente los 15 minutos
    print("Finaliza conteo de 15 minutos")
    
def luces(tono, color):
    print("Se establece el color:")
    print("Color establecido y el tono")
    print("Se establece el color a: " + color)
    print("Tono estaclecido a: " + str(tono))
    
def etapaUno():
    print("Etapa Uno iniciada")
    timer(varLapso)
    luces(varTono1, varColorI)
    print("Etapa Uno finalizada")
    etapaDos()

def etapaDos():
    print("Etapa Dos iniciada")
    timer(varLapso)
    luces(varTono2, varColorI)
    print("Etapa Dos finalizada")
    etapaTres()

def etapaTres():
    print("Etapa Tres iniciada")
    timer(varLapso)
    luces(varTono3, varColorF)
    print("Etapa Tres finalizada")
    etapaCuatro()

def etapaCuatro():
    print("Etapa Cuatro iniciada")
    timer(varLapso)
    luces(varTono4, varColorF)
    print("Etapa Cuatro finalizada")
    finalizar()
    
# Trigger Inicial
print("Inicio de Manipulación de luces")

# etapaUno()
inicio()