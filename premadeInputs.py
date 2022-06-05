
from calculadora import *
import time
import timeit

start = timeit.default_timer()

# Descomente e comente de acordo com a operação que deseja realizar

#SOMA
x = 10**200000
# x = 10**300000
# x = 10**400000
# x = 10**500000
# x = 10**600000
# x = 10**700000
# x = 10**800000
# x = 10**900000
# x = 10**1000000
#x = 10**1100000
x = str(x)
N = soma(x, x)

end = timeit.default_timer()
# print(f'Tempo = {end-start} segundos')

#MULTIPLICAÇÃO
start = timeit.default_timer()
y = 10**600
# y = 10**800
# y = 10**1000
# y = 10**1200
# y = 10**1400
# y = 10**1600
# y = 10**1800
# y = 10**2000
# y = 10**2400
y = str(y)
Num = multiplicar(y, y)
end = timeit.default_timer()
print(f'Tempo = {end-start} segundos')