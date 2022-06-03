#Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

#8 3 4
#1 5 9
#6 7 2

#Faça uma função que receba uma matriz e sua ordem. Essa função deve informar se a matriz forma um quadrado mágico. Em seguida, faça um programa que:

#1 - Solicita ao usuário a ordem da matriz;
#2 - Faz a leitura da matriz;
#3 - Imprime a matriz;
#4 - Informa se a matriz digitada forma um quadrado mágico.

def ordem(matriz,ordem):
  for i in range(ordem):
    m.append([0] * ordem)

def leitura(matriz,ordem):
  for i in range(ordem):
    for j in range(ordem):
      print('\nM = [',i+1,',',j+1,']: ',end='')
      m[i][j] = int(input())

def imprime(matriz,ordem):
  print('Matriz informada:')
  for i in range(ordem):
    for j in range(ordem):
      print(m[i][j],end=' ')
    print()

def verifica(matriz,ordem):
  soma1 = 0
  soma2 = 0
  soma3 = 0
  soma4 = 0
  for i in range(ordem):
    for j in range(ordem):
      if i < ordem:
        soma1 = soma1 + m[i][j]/ordem
      if j < ordem:
        soma2 = soma2 + m[i][j]/ordem
      if i + j == ordem-1:
        soma3 = soma3 + m[i][j]
      if i == j:
        soma4 = soma4 + m[i][j]
      if soma1 == soma2 and soma2 == soma3 and soma3 == soma1 and soma1 == soma4 and soma4 == soma2 and soma3 == soma4:
        return True
  return False

n = int(input('digite a ordem da matriz: '))
m = []
ordem(m,n)
leitura(m,n)
imprime(m,n)
if verifica(m,n):
  print('Essa matriz é um quadrado mágico!')
else:
  print('Essa matriz NÃO é um quadrado mágico!')