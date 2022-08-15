import random
from math import e
import matplotlib.pyplot as plt
import time

class Dato:
    def __init__(self,distancia,indice):
        self.distancia = int(distancia)
        self.indice = int(indice)

#Se lee instancia
def leerInstancia (nombreInstancia,vectorDistancias,matrizFlujo):
    with open(nombreInstancia,"r") as archivo:
        for i,linea in enumerate(archivo):
            if i== 0:
                cantidadDatos = int(linea.strip())
            if i== 1:
                auxVectorDistancias =[aux.strip() for aux in linea.split(',')]
            elif i>1:
                arrayAuxiliar =[aux.strip() for aux in linea.split(',')]
                for j in range (len(arrayAuxiliar)):
                    arrayAuxiliar[j] = int(arrayAuxiliar[j])
                matrizFlujo.append(arrayAuxiliar)
        [int(i) for i in vectorDistancias]
        for j in range (cantidadDatos):
            datoNuevo = auxVectorDistancias[j]
            indexAux = j
            datoAux = Dato(datoNuevo,indexAux)
            vectorDistancias.append(datoAux)
        return cantidadDatos

#Se selecciona instancia a leer
def seleccionarInstancia():
    print('Elige archivo:')
    print('1-QAP_sko56_04_n')
    print('2-QAP_sko100_04_n')
    opcion = input()
    if(opcion == '1'):
        return 'QAP_sko56_04_n.txt'
    elif(opcion == '2'):
        return 'QAP_sko100_04_n.txt'
    else:
        print('Opcion no valida')

def leerTemperatura():
    print('Ingrese temperatura deseada (Mayor a 0.2)')
    temp = int(input())
    while(temp < 0):
        print('Ingrese una temperatura valida')
        temp = input()
    return temp

def leerAlpha():
    print('Ingrese alpha deseada (Mayor a 0 y menor a 1)')
    alphaAux = float(input())
    while(alphaAux < 0 or alphaAux > 1):
        print('Ingrese un alpha valida')
        alphaAux = input()
    return alphaAux

def calcularDistancia(vector,posPrimero,posSegundo):
    distancia = 0.0
    for i in range(posPrimero+1,posSegundo):
        distancia += vector[i].distancia
    distancia = distancia + ((vector[posPrimero].distancia)/2 + (vector[posPrimero].distancia)/2)
    return distancia

def calcularFuncionObjetivo(vector,matriz,cantDatos):
    total = 0.0
    for i in range (cantDatos):
        for j in range (i+1,cantDatos):
            total += calcularDistancia(vector,i,j) * matriz[vector[i].indice][vector[j].indice]
    return total

def generarVector(vectorObjetos):
    arrAux = []
    for i in vectorObjetos:
        arrAux.append((i.indice)+1)
    return arrAux

def swap(vector):
    
    while(True):
        i = random.randrange(cantidadDatos)
        j = random.randrange(cantidadDatos)
        if(i != j):
            break
    aux = vector[i]
    vector[i]=vector[j]
    vector[j]=aux

def calcularSolucionInicial(vector,matriz,cantDatos):
    arrAux = []
    solucionGenerada = calcularFuncionObjetivo(vector,matriz,cantDatos)
    arrAux.append(solucionGenerada)
    arrAux.append(generarVector(vector))
    return arrAux

def calcularCriterioMetropolis(mejorSolucionActual,nuevaSolucion,temp):
    deltaS= nuevaSolucion - mejorSolucionActual
    p = e**((-deltaS)/temp)
    return p

def simulated_annealing(bestSolution,vector,matriz,cantDatos,alpha,temp,iteraciones):
    iteracion = 0
    while (temp > 0.2):
        vecino = vector.copy()
        swap(vecino)
        print('')
        solucionVecino = calcularFuncionObjetivo(vecino, matriz, cantDatos)
        if (solucionVecino < bestSolution[0]):
            bestSolution[0] = solucionVecino
            bestSolution[1] = generarVector(vecino)
            vector = vecino
        else:
            if (random.random() < calcularCriterioMetropolis(bestSolution[0], solucionVecino, temp)):
                bestSolution[0] = solucionVecino
                bestSolution[1] = generarVector(vecino)
                vector = vecino
        temperaturas.append(temp)
        soluciones.append(bestSolution[0])
        temp = temp * alpha
        print('Iteracion numero: ',iteracion)
        print('Mejor Solucion Actual: ', bestSolution[0], bestSolution[1])
        print('Temperatura actual: ', temp)
        print('')
        iteraciones.append(iteracion)
        iteracion += 1
    #plt.plot(iteraciones,temperaturas,'ro',lw='0.5')
    #plt.ylabel('Temperatura')
    #plt.xlabel('Iteraciones') 
    #plt.show()

vectorDistancias = []
matrizFlujo = []
temperaturas = []
soluciones = []
iteraciones = []
nombreInstancia = seleccionarInstancia()
temperatura = leerTemperatura()
alpha = leerAlpha()
cantidadDatos = leerInstancia(nombreInstancia,vectorDistancias,matrizFlujo)
for dato in vectorDistancias:
    print(dato.distancia,end='')
#print(matrizFlujo)
random.shuffle(vectorDistancias)
for dato in vectorDistancias:
    print(dato.distancia,end='')
print('')
start_time = time.time()
mejorSolucion = calcularSolucionInicial(vectorDistancias,matrizFlujo,cantidadDatos)
print('Solucion Inicial: ',mejorSolucion[0],mejorSolucion[1])
simulated_annealing(mejorSolucion,vectorDistancias,matrizFlujo,cantidadDatos,alpha,temperatura,iteraciones)
print('')
print('La mejor solucion encontrada',mejorSolucion[1])
print('Costo: ',mejorSolucion[0])
print('Total iteraciones: ',len(iteraciones)-1)
print('Total evaluaciones: ',len(iteraciones)-1)
print('Tiempo total de ejecucion: ',(time.time()-start_time))
