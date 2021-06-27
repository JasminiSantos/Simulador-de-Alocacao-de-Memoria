import random

#função que gera a matriz
def gerar_matriz(l,c):
  matriz = [] #armazena linhas
  for i in range(0,l):
    linhas = [] #armazena espacos preenchidos e vazios
    for j in range(0,c):
      if random.random() > 0.5: #gera um valor entre 0 e 1
        linhas.append("X")
      else:
        linhas.append(" ")

    matriz.append(linhas) #matriz recebendo linha

  return matriz

def exibir_matriz(l,c,m):
  for i in range(0,l):
    for j in range(0,c):
      if m[i][j] == "X":
        print("X|", end = '')
      else:
        print(" |", end = '')
    print()

#função para receber variáveis globais
def receber_dados():
  global l
  global c
  global m
  l = int(input('Digite a quantidade de linhas:'))
  c = int(input('Digite a quantidade de colunas:'))
  while l <= 0 or c <= 0:
    print("Digite valores válidos!")
    l = int(input('Digite a quantidade de linhas:'))
    c = int(input('Digite a quantidade de colunas:'))

  m = gerar_matriz(l,c)

#função para alocação first fit
def first_fit(l,c,m,tamanho_memoria):
  contador_espacos = 0 #conta espaços vazios
  linha_inicial = 0 #armazena a linha inicial da memória que será alocada
  coluna_inicial = 0 #armazena a coluna inicial da memória que será alocada
  linha_final = 0 #armazena a linha final da memória que será alocada
  coluna_final = 0 #armazena a coluna final da memória que será alocada
  if tamanho_memoria <= 0:
    print("Valor inválido!")
  else:
    for i in range(0,l):
      for j in range(0,c):
        if m[i][j] == " ":
          contador_espacos = contador_espacos + 1
          if contador_espacos == 1:
            linha_inicial = i
            coluna_inicial = j
            
        elif m[i][j] == "X" and contador_espacos < tamanho_memoria:
          contador_espacos = 0

        if contador_espacos == tamanho_memoria: #espaco encontrado
          linha_final = i
          coluna_final = j

          for i2 in range(linha_inicial,linha_final+1):
            for j2 in range(coluna_inicial, c):
              m[i2][j2] = "X"
              if i2 == linha_final and j2 == coluna_final:
                print("Espaço ocupado com sucesso!")
                return m
            coluna_inicial = 0
    if contador_espacos < tamanho_memoria:
      print("Espaço indisponível na memória!")          

def worst_fit(l,c,m, tamanho_memoria):
  contador_espacos = 0 #conta espaços vazios
  espacos_vazios = [] #armazena o tamanho do maior espaço encontrado na matriz
  espaco_maior = 0
  if tamanho_memoria <= 0:
    print("Valor inválido!")
  else:
    for i in range(0,l): #laço para percorrer a matriz e encontrar o maior espaço disponível
      for j in range(0,c):
        if m[i][j] == " ":
          contador_espacos = contador_espacos + 1
          if i == l-1 and j == c-1 and contador_espacos >= tamanho_memoria: 
            espacos_vazios.append(contador_espacos)
            contador_espacos = 0            
        
        elif m[i][j] == "X" and contador_espacos >= tamanho_memoria:
          espacos_vazios.append(contador_espacos)
          contador_espacos = 0
        else:
          contador_espacos = 0

    if espacos_vazios == []: #condição que não encontra espaços para a memória
      print("Espaço indisponível na memória!")

    else: #caso encontre espaço para a memória
      for i in range(0, len(espacos_vazios)):
        if espacos_vazios[i] > espaco_maior:
          espaco_maior = espacos_vazios[i]

      for i in range(0,l):
        for j in range(0,c):
          if m[i][j] == " ":
            contador_espacos = contador_espacos + 1
          else:
            contador_espacos = 0
          
          if contador_espacos == espaco_maior: #espaço encontrado
            while espaco_maior != 0:
              if espaco_maior <= tamanho_memoria: #garante o preenchimento apenas do tamanho necessário
                m[i][j] = "X"
              espaco_maior = espaco_maior - 1
              if j == 0: #trocando de linha na matriz
                if i != 0:
                  i = i-1
                j = c-1
              else: #trocando de posição em uma linha
                j = j-1
            print("Espaço ocupado com sucesso!")
            return m      


def best_fit(l,c,m,tamanho_memoria):
  contador_espacos = 0 #conta espaços vazios
  espacos_vazios = [] #armazena os blocos de espaços disponíveis
  espaco_menor = l*c #armazena o melhor espaço disponível para a alocação

  if tamanho_memoria <= 0:
    print("Valor inválido!")
  else:
    
    for i in range(0,l):
      for j in range(0,c):

        if m[i][j] == " ":
          contador_espacos = contador_espacos + 1
          if i == l-1 and j == c-1 and contador_espacos >= tamanho_memoria: 
            espacos_vazios.append(contador_espacos)
            contador_espacos = 0            
        
        elif m[i][j] == "X" and contador_espacos >= tamanho_memoria:
          espacos_vazios.append(contador_espacos)
          contador_espacos = 0
        else:
          contador_espacos = 0
    
    if espacos_vazios == []: #condição que não encontra espaços para a memória
      print("Espaço indisponível na memória!")
    
    else: #caso encontre espaço para a memória
      for i in range(0, len(espacos_vazios)):
        if espacos_vazios[i] < espaco_menor:
          espaco_menor = espacos_vazios[i]

      for i in range(0,l):
        for j in range(0,c):
          if m[i][j] == " ":
            contador_espacos = contador_espacos + 1
          else:
            contador_espacos = 0
          
          if contador_espacos == espaco_menor and j != c-1 and m[i][j+1] == "X": #espaço encontrado
            while espaco_menor != 0:
              if espaco_menor <= tamanho_memoria: #garante o preenchimento apenas do tamanho necessário
                m[i][j] = "X"
              espaco_menor = espaco_menor - 1
              if j == 0: #trocando de linha na matriz
                if i != 0:
                  i = i-1
                j = c-1
              else: #trocando de posição em uma linha
                j = j-1
            print("Espaço ocupado com sucesso!")
            return m
          elif contador_espacos == espaco_menor and j == c-1 and i != l-1 and m[i+1][0] == "X": #espaço encontrado
            while espaco_menor != 0:
              if espaco_menor <= tamanho_memoria: #garante o preenchimento apenas do tamanho necessário
                m[i][j] = "X"
              espaco_menor = espaco_menor - 1
              if j == 0: #trocando de linha na matriz
                if i != 0:
                  i = i-1
                j = c-1
              else: #trocando de posição em uma linha
                j = j-1
            print("Espaço ocupado com sucesso!")
            return m
          
          #quando termina na última linha da última coluna
          elif contador_espacos == espaco_menor and j == c-1 and i == l-1 and m[l-1][c-1] == " ":
            while espaco_menor != 0:
              if espaco_menor <= tamanho_memoria: #garante o preenchimento apenas do tamanho necessário
                m[i][j] = "X"
              espaco_menor = espaco_menor - 1
              if j == 0: #trocando de linha na matriz
                if i != 0:
                  i = i-1
                j = c-1
              else: #trocando de posição em uma linha
                j = j-1
            print("Espaço ocupado com sucesso!")
            return m          

#função para desalocar espaço na memória
def desalocar(l,c,m):
    linha_inicial = int(input('Digite a coordenada da linha inicial:'))
    coluna_inicial = int(input('Digite a coordenada da coluna inicial:'))
    linha_final = int(input('Digite a coordenada da linha final:'))
    coluna_final = int(input('Digite a coordenada da coluna final:'))

    ''' 
      condições que invalidam a desalocação:
      linhas e colunas menores que zero
      posições de linhas e colunas maiores que os das linhas e colunas da matriz - 1
      posições de coluna inicial maior que coluna final em uma mesma linha
      posição de linha inicial maior que linha final
    '''
    if (linha_inicial < 0 or linha_inicial >= l) or (linha_final < 0 or linha_final >= l) or (coluna_inicial < 0 or coluna_inicial >= c) or (coluna_final < 0 or coluna_final >= c) or (coluna_inicial > coluna_final and linha_inicial == linha_final) or (linha_inicial > linha_final): #condições que invalidam a desalocação
      print("Coordenadas inválidas!")
    else:
      for i2 in range(linha_inicial,linha_final+1):
        for j2 in range(coluna_inicial, c):
          m[i2][j2] = " "
          if i2 == linha_final and j2 == coluna_final:
            print("Espaço liberado na memória!")
            return m
        coluna_inicial = 0

def menu():
  print("SIMULADOR DE ALOCAÇÃO DE MEMÓRIA")
  print('-' * 30)
  print('1 - Visualizar memória')
  print('2 - Alocação First Fit')
  print('3 - Alocação Best Fit')
  print('4 - Alocação Worst Fit')
  print('5 - Desalocação')
  print('6 - Gerar nova memória')
  print('7 - Sair')
  print('-' * 30)


receber_dados() 
while True:
    menu()
    opcao = int(input('Qual opcao vc deseja?'))
    if opcao == 1:
      exibir_matriz(l,c,m)
    elif opcao == 2:
      tamanho_memoria = int(input('Digite o tamanho da memória que será alocada:'))
      first_fit(l,c,m,tamanho_memoria)
    elif opcao == 3:
      tamanho_memoria = int(input('Digite o tamanho da memória que será alocada:'))
      best_fit(l,c,m,tamanho_memoria)
    elif opcao == 4:
      tamanho_memoria = int(input('Digite o tamanho da memória que será alocada:'))
      worst_fit(l,c,m,tamanho_memoria)
    elif opcao == 5:
      desalocar(l,c,m)
    elif opcao == 6:
      receber_dados()
    elif opcao == 7:
      #exit()
      break
    else:
      print('Digite algo valido!')