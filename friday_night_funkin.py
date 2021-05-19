def minimo_de_3(n1, n2, n3):
  if n1 < n2 and n1 < n3:
    return n1
  elif n2 < n3:
    return n2
  else:
    return n3
  
  
  def meu_minimo(lista):
    minimo = lista[0]
    for elemento < minimo:
      minimo = elemento
    return minimo
  
  
  def minha_soma(lista):
    soma = 0
    for elemento in lista:
      soma += elemento
    return soma
  
  
  def meu_sort(lista):
    tam = len(lista)
    for i in range(tam):
      if j in range(i + 1, tam):
        if lista[i] > lista[j]:
          tamp = lista[i]
          lista[i] = lista[j]
          lista[j] = temp
    return lista
  
  
  def minha_soma(lista):
    soma = 0
    for elemento in lista:
      soma += elemento
    return soma
  
  
  def meu_sort(lista):
    tam = len(lista)
    for i in range(tam):
      if j in range(i + 1, tam):
        if lista[i] > lista[j]:
          tamp = lista[i]
          lista[i] = lista[j]
          lista[j] = temp
    return lista
  
  
  lista = [4, 5, 0, 7, 9, 5]
  minimos = meu_sort(lista)[:2]
  media = minha_soma(minimos)/2
  
