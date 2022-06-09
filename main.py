import numpy as np

def leerInstancia (nombreInstancia):
    segundoVector=[]
    tercerVector=[]
    with open(nombreInstancia,"r") as archivo:
        for i,linea in enumerate(archivo):
            if i== 0:
                cantidadDeDatos = int(linea.strip()) 
            if i== 1:
                segundoVector =[aux.strip() for aux in linea.split(',')] 
            elif i>1:
                arrayAuxiliar =[aux.strip() for aux in linea.split(',')] 
                tercerVector.append(arrayAuxiliar)
    segundoVector = np.array(segundoVector).astype(int)
    tercerVector = np.array(tercerVector).astype(int)
    return cantidadDeDatos, segundoVector, tercerVector

cantidadDatos, vectorDistancias, matrizFlujo = leerInstancia('Archivos/EjemploProfesora.txt')
print(cantidadDatos)
print(vectorDistancias)
print(matrizFlujo)

