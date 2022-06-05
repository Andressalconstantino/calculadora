from calculadora import *
import time

#Aqui você pode colocar seu próprio input :)

while True:
    operation = input('Para realizar soma digite A, para realizar multiplicação digite M e para sair digite X: ').upper()

    if operation == 'X': 
        break

    if operation == 'A':
        number1, number2 = map(str, input('Digite os dois números, separando com um espaço: ').split())
        start_time = time.time()
        resultado = soma(number1, number2)
        print(f'O resultado é: \n {resultado}')

    elif operation == 'M':
        number1, number2 = map( str, input('Digite os dois números, separando com um espaço: ').split())
        start_time = time.time()
        resultado = multiplicar(number1, number2)
        print(f'O resultado é: {resultado}')

    else:
        print('Digite uma letra valida')
        
        
    # print("%s segundos" % (time.time() - start_time))
    print(f'Tempo = {time.time()-start_time} segundos')