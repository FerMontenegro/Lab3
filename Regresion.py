def string_a_numero(caracter):
    return {
        'crim':0,
        'zn':1,
        'indus':2,
        'chas':3,
        'nox':4,
        'rm':5,
        'edad':6,
        'dis':7,
        'rad':8,
        'impuesto':9,
        'ptratio':10,
        'b':11,
        'lstat':12,
        'medv':13
    }[caracter]

def pendienteNumerador(promedio1,promedio2,valor1,valor2,datos):
    suma = 0
    for i in range(len(datos)):
        suma = suma + ((float(datos[i][valor1])-promedio1)*(float(datos[i][valor2])-promedio2))
    return suma   

def pendienteDenominador(promedio1,datos,valor1):
    suma=0
    for i in range(len(datos)) :
        suma=suma + (float(datos[i][valor1])-promedio1)**2
    return suma

def sacarPromedio(valor1, valor2, datos):
    suma=0
    suma2=0
    promedio1 = 0
    promedio2 = 0
    for i in range(len(datos)):
        suma += float(datos[i][valor1])
        suma2 += float(datos[i][valor2])
    promedio1 = suma/len(datos)
    promedio2 = suma2/len(datos)
    return promedio1, promedio2

def calcular20PorCientoPromedioDistanciaDePuntos(pendiente,valor2,valor1,c,datos):
    suma = 0
    promedio = 0
    for i in range(len(datos)):
        distanciaActual = abs(float (datos[i][valor2]) - ((float(pendiente)*float(datos[i][valor1])) + float(c)))
        suma = distanciaActual + suma
        #print(suma)
        distanciaActual = 0
    promedio = suma/len(datos)
    veintePorCientoPromedio = promedio * 0.20
    return veintePorCientoPromedio

contents = open("housing.data").read()
datos = [item.split() for item in contents.split('\n')[:-1]]

columna1 = input("Ingrese columna 1: ")
columna2 = input("Ingrese columna 2: ")

valor1 = string_a_numero(columna1.lower())
valor2 = string_a_numero(columna2.lower())

valorPreguntado = input("Ingrese el valor X: ")

print(valor1, valor2)
#print("Len de datos:", len(datos))
for i in range(len(datos)):
    print(datos[i][valor2])

promedioColumna1, promedioColumna2 = sacarPromedio(valor1, valor2, datos)
formulaPendienteNumerador = pendienteNumerador(promedioColumna1, promedioColumna2, valor1, valor2, datos)
formulaPendienteDenominador = pendienteDenominador(promedioColumna1, datos, valor1)
pendiente = formulaPendienteNumerador/formulaPendienteDenominador
c= promedioColumna2 -(pendiente*promedioColumna1)
print("y = ", pendiente,"x + ", c)

Y =( (float(pendiente) * float(valorPreguntado)) + float(c))

print("el Y esperado es: ", Y)

promedioDistancia = calcular20PorCientoPromedioDistanciaDePuntos(pendiente, valor2, valor1, c, datos)
print(" 20%Promedio distancia: ", promedioDistancia)



