def soma(number1string, number2string):
    #making numbers have the same lenght
    if len(number1string) > len(number2string):
        diference = len(number1string) - len(number2string)
        addZeros = ''
        for i in range(diference):
            addZeros += '0'
        aux = number2string
        number2string = addZeros + number2string

    elif len(number2string) > len(number1string):
        diference = len(number2string) - len(number1string)
        addZeros = ''
        for i in range(diference):
            addZeros += '0'
        aux = number1string
        number1string = addZeros + number1string

    #add
    size = len(number1string)
    resto = 0
    result = ''

    for i in range(size-1, -1, -1):
        add = int(number1string[i]) + int(number2string[i]) + resto
        add = str(add)
        resto = 0
        if len(str(add))>1:
            result += add[1]
            resto = int(add[0])
        else:
            result += add[0]
    if resto != 0:
        result += str(resto)
    result = result[::-1]
    
    #remove useless zeros
    # leftZero = True
    # answer = ''
    # for i in range(len(result)):
    #     if leftZero == True and result[i] == '0':
    #         pass
    #     else:
    #         leftZero = False
    #         answer += result[i]

    return result


#multiply 
# number1string = input()
# number2string = input()

def multiplicar(number1string, number2string):
    #making numbers have the same lenght
    if len(number1string) > len(number2string):
        diference = len(number1string) - len(number2string)
        addZeros = ''
        for i in range(diference):
            addZeros += '0'
        aux = number2string
        number2string = addZeros + number2string

    elif len(number2string) > len(number1string):
        diference = len(number2string) - len(number1string)
        addZeros = ''
        for i in range(diference):
            addZeros += '0'
        aux = number1string
        number1string = addZeros + number1string

    size = len(number1string)
    resto = 0
    result = ''
    toSum = []
    cont = 0

    #multiply number by number
    for i in range(size-1, -1, -1):
        result = ''
        for j in range(size-1, -1, -1):
            multiply = (int(number2string[i]) * int(number1string[j])) + resto
            multiply = str(multiply)
            resto = 0
            if len(multiply)>1:
                result += multiply[1]
                resto = int(multiply[0])
            else:
                result += multiply[0]
            # print(result)
            if j==0 and resto !=0:
                result += str(resto)
                resto = 0
        result = result[::-1]
        result += cont * '0'
        toSum.append(result)
        cont += 1

    #make all numbers the same lenght
    for i in range(len(toSum)):
        addZeros = ''
        diference = len(toSum[-1]) - len(toSum[i])
        for j in range(diference):
            addZeros += '0'
        aux = toSum[i]
        toSum[i] = addZeros + toSum[i]

    aux = ''
    for i in range(len(toSum)):
        if i==0:
            aux = toSum[0]
        else:
            res = soma(aux, toSum[i])
            aux = res

    #remove useless zeros
    cont = 0
    no = True
    result = ''
    for i in range(len(aux)):
        if aux[i] == '0' and no == True:
            cont += 1
        else:
            no = False
            result += aux[i]
    
    return result
