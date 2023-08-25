
import matplotlib.pyplot as plt
import numpy as np


lista = np.array([1,2,3,4,5])


#print(lista)


mat1d = np.arange(10)
#print(mat1d)


x = np.array([1,2,3,4,5])
#print(x)

impar = mat1d[mat1d % 2 == 1]
#print(impar)

#arange(valor_inicial, valor_final, intervalo)
mat1d_seg = np.arange(5,11)
#print(mat1d_seg)

mat1d_seg = np.arange(5,20,2)
print('Sequencia de 5 até 20, variando de 2 em 2: ', mat1d_seg)


vet_zeros = np.zeros(10)
vet_ones = np.ones(10)
print("Valores de zeros: ", vet_zeros)
print("\nVetor de valores um: ", vet_ones)


#Selecionar elementos de vetores e matrizes
vetA = np.array(['a','b','c','d','e','f','g','h','i'])

print('Três primeiros elementos de vetA: ')
# print( vetA[0:3] )

print('\ntodos os valores após o Quinto elementos de vetA: ')
# print( vetA[5:] )

print('\nOs três ultimos valores de vetA: ')
# print( vetA[-3:] )

print('\nOs valores de vetA entre o 5 elemento até o penúltimo elemento: ')
# print( vetA[4:-2], 'ou', vetA[4:7] )


#selecionar vários subconjuntos de elementos de uma matriz
arrayA = np.array( [['1a','1b','1c','1d','1e','1f','1g','1h','1i'],
                    ['2a','2b','2c','2d','2e','2f','2g','2h','2i'],
                    ['3a','3b','3c','3d','3e','3f','3g','3h','3i'],
                    ['4a','4b','4c','4d','4e','4f','4g', '4h','4i']])

print('Matriz inteira: ')
print( arrayA )

print('\nTodos os elementos da coluna 3: ')
print( arrayA[:,2] )

print('\nTodos os elementos da linha 2: ')
print( arrayA[1,:] )

print('\nTodos os elementos das 2 primeiras colunas: ')
print( arrayA[:,0:2] )

print('\nTodos os elementos das 2 primeiras linhas: ')
print( arrayA[0:2,:] )

print('\nApenas os elementos das 2 primeiras linhas e das 2 primeiras colunas: ')
print( arrayA[0:2,0:2] )

print('\nApenas os elementos das 2 últimas linhas e das 4 últimas colunas: ')
print( arrayA[-2:,-4:] )

print('\nApenas os elementos das linhas 2 até 4 e das colunas 4 até 6: ')
print( arrayA[1:3,3:6] )


x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8, 9, 10])

print(x + y)
print(x - y)
print(y - x)
print(x * y)
print(x / y)
print(y / x)

np.sum(x)
np.max(x)
np.min(x)
np.mean(x)
np.median()

B = np.array( ([[1,2,3,4],[5,6,7,8]]) )
#Média dos valores de uma matriz.
print('B: ')
display(B)

# média das linhas de B
media1 = np.mean(B, axis = 1)
print('\nMédia das linhas de B: ')
display(media1)

# média das colunas de B
media2 = np.mean(B, axis = 0)
print('\nMédia das colunas de B: ')
display(media2)

# média de todos os valores de B
media3 = np.mean(B)
print('\nMédia de todos os valores de B: ')
display(media3)
