def area(base, altura):
    return (base * altura)/2

def tipo_triangulo(base, altura, lado3):
    triangulo = ''
    if base == altura and base == lado3 and altura == lado3:
        triangulo = 'Equilatero'
    elif base != altura and altura == lado3:
        triangulo = 'Isoceles'
    elif  base != altura and base != lado3 and altura != lado3:
        triangulo = 'Escaleno'

    print(triangulo)

def uno():
    base = int(input('Base del triangulo: '))
    altura = int(input('Altura del triangulo: '))
    print(area(base, altura))
    print('-'*30)

    lado3 = int(input('Decime el lado restante del triangulo y te digo que tipo de triangulo es: '))
    tipo_triangulo(base, altura, lado3)
    


def ppt(nombre_jug1, nombre_jug2, vidas):
    contador_jug1 = 0
    contador_jug2 = 0

    mitad = vidas/2

    for i in range(vidas):
        print('-' * 30)
        jugador1 = str(input(f'¿{nombre_jug1}, Que elegis? ¿Piedra, Papel o Tijera?: ')).lower()
        jugador2 = str(input(f'¿{nombre_jug2}, Que elegis? ¿Piedra, Papel o Tijera?: ')).lower() 
        print('-' * 30)

        if jugador1 == 'piedra' and jugador2 == 'tijera':
            contador_jug1 += 1
            print(f'Ganó esta ronda el {nombre_jug1}')

        elif jugador1 == 'piedra' and jugador2 == 'papel':            
            contador_jug2 +=1
            print(f'Ganó esta ronda el {nombre_jug2}')

        elif jugador1 == 'piedra' and jugador2 == 'piedra':            
            print('Esta ronda fue empate, va de vuelta')

        elif jugador1 == 'papel' and jugador2 == 'tijera':            
            contador_jug2 +=1
            print(f'Ganó esta ronda el {nombre_jug2}')

        elif jugador1 == 'papel' and jugador2 == 'piedra':            
            contador_jug1 +=1
            print(f'Ganó esta ronda el {nombre_jug1}')            
        elif jugador1 == 'papel' and jugador2 == 'papel':            
            print('Esta ronda fue empate, va de vuelta')

        elif jugador1 == 'tijera' and jugador2 == 'tijera':            
            print('Esta ronda fue empate, va de vuelta')

        elif jugador1 == 'tijera' and jugador2 == 'papel':            
            contador_jug1 +=1
            print(f'Ganó esta ronda el {nombre_jug1}')
            
        elif jugador1 == 'tijera' and jugador2 == 'piedra':            
            contador_jug2 +=1
            print(f'Ganó esta ronda el {nombre_jug2}')

        if contador_jug1 > mitad:
            print(f'Ganó el juego, el jugador {nombre_jug1}')
            break

        elif contador_jug2 > mitad:
            print(f'Ganó juego, el jugador {nombre_jug2}')
            break

    if contador_jug1 <= mitad and contador_jug1 > contador_jug2:
        print(f'Ganó el juego, el jugador {nombre_jug1}')
        

    elif contador_jug2 <= mitad and contador_jug2 > contador_jug1:
        print(f'Ganó el juego, el jugador {nombre_jug2}')

    elif contador_jug2 == contador_jug1:
        print('Empate')

def dos():
    vidas = int(input('¿Cuántos juegos van a ser?: '))
    nombre_jug1 = str(input('Nombre del jugador n° 1: '))
    nombre_jug2 = str(input('Nombre del jugador n° 2: '))

    ppt(nombre_jug1, nombre_jug2, vidas)



def millas_a_km(millas):
    metros = millas / 0.0007183908045977
    print(metros)

def km_a_millas(km):
    milla = km * 0.0007183908045977
    print(milla)

def tres():
    seleccion = str(input("""Si queres pasar de milla a km, introducí la palabra 'milla'.
De ser al revés, introducí la palabra 'km': """))

    if seleccion == 'milla':
        millas = int(input('¿Cuántas millas querés convertir a km?: '))
        millas_a_km(millas)
    elif seleccion == 'km':
        km = int(input('¿Cuántos km querés convertir a millas?: '))
        km_a_millas(km)



def volumen_cilindro(radio, h):
    pi = 3.14159
    base = pi * (radio**2)

    volumen = base * h
    print(f'El volumen del cilindro es {volumen}')

def cuatro():
    radio = int(input('¿De que radio es la base del cilindro?: '))
    h = int(input('¿Cuál es la altura del cilindro?: '))

    volumen_cilindro(radio, h)



def rangos(limite_inf, limite_sup, comparativo):
    if comparativo in range(limite_inf, limite_sup):
        print(f'El número {comparativo} efectivamente está dentro del rango')
    
    elif comparativo not in range(limite_inf, limite_sup):
        print(f'El número {comparativo} no está dentro del rango')

def cinco():
    limite_inf = int(input('Ingresa el limite inferior del rango: '))  
    limite_sup = int(input('Ingresa el limite superior del rango: '))  
    comparativo = int(input('Ingresa el número a verificar si está dentro del rango, o no: '))
    print('-' * 35)

    rangos(limite_inf, limite_sup, comparativo)

def main():
    
    #1
    #uno()
    
    #2
    #dos()
    
    #3
    #tres()
    
    #4
    #cuatro()

    #5
    cinco()

if __name__ == '__main__':
    main()