import random

def generar_polinomio(s: int, k:int ) -> int:
    '''
        s: El secreto a ocultar.
        k: El umbral minimo de partes necesarias para recuperar el secreto.
        
        retorno: Lista con coeficientes del polinomio f(x).
    '''
    coeficientes = [s]
    for i in range(k-1):
        coeficientes.append(random.randint(0,256))
    return coeficientes

def escribir_polinomio(coeficientes: list) -> str:
    '''
        coeficientes: Coeficientes del polinomio p(x).
        
        retorno: Polinomio p(x) en formato de cadena.
    '''
    polinomio = f'p(x) = {coeficientes[0]}'

    for i in range(1, len(coeficientes)):
        polinomio += f' + {coeficientes[i]}x^{i}'

    return polinomio

def obtener_partes(valores_x: list, coeficientes: list) -> list:
    '''
        valores_x: Valores de x que se evaluaran en p(x) para generar las partes.
        coeficientes: Coeficientes del polinomio p(x).
        
        retorno: Lista de tuplas de la forma (x, p(x))
    '''
    partes = []

    for x in valores_x:
        print(f'x: {x}')
        y = 0
        y += coeficientes[0]

        for i in range(1, len(coeficientes)):
            y += coeficientes[i] * x ** i
            print(f'y: {y}')
        print('\n')

        partes.append((x, y))

    return partes

def interpolacion_lagrange(partes: list) -> int:
    '''
        partes: Lista de partes que se utilizaran para recuperar el secreto.
        
        retorno: El secreto recuperado.
    '''
    secreto = 0

    for i in range(len(partes)):
        producto = 1
        xi, yi = partes[i] # tupla de la forma  (x, f(x))
        print(xi, yi)

        for j in range(len(partes)):
            if i != j:
                xj = partes[j][0] # valor de x en la parte j
                producto *= (0 - xj) / (xi - xj) 

        producto *= yi
        secreto += producto

    return int(secreto)

def solicitar_x(n: int) -> list:
    '''
        n: Cantidad de valores de x que se solicitaran.
        
        retorno: Lista con los valores de x.
    '''
    valores_x = []

    for i in range(n):
        try:
            x_value = int(input(f'Ingrese el valor de x{i+1}: '))
            valores_x.append(x_value)
        except Exception as e:
            print('Ingrese un valor numerico.')

    return valores_x

def main():
    print('Secreto: valor que se desea compartir.')
    print('Umbral: numero minimo de partes necesarias para recuperar el secreto.')

    try:
        secreto = int(input('Ingrese el valor del secreto: '))
        umbral = int(input('Ingrese el umbral: '))
        print('\n')

        coeficientes = generar_polinomio(secreto, umbral)
        polinomio = escribir_polinomio(coeficientes)
        print(f'Polinomio: {polinomio}\n')

        cantidad_x = int(input('Ingrese la cantidad de valores de x que se utilizaran: '))
        
        if cantidad_x < umbral:
            print('La cantidad de valores de x es menor al umbral.')
            return
    
        valores_x = solicitar_x(cantidad_x)
        partes = obtener_partes(valores_x, coeficientes)
        print(f'\nPartes: {partes}\n')

        partes_interpolacion = []

        for i in range (umbral):
            partes_interpolacion.append(partes[i])

        secreto_recuperado = interpolacion_lagrange(partes_interpolacion)
        print(f'Secreto recuperado: {secreto_recuperado}')

            
    except Exception as e:
        print('Ingrese un valor numerico.')
        return

if __name__ == '__main__':
    main()

    
    
    

    