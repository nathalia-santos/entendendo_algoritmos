# Quanto tempo levaria, em notação Big O, para completar cada uma destas operações?

# 4.5 - Imprimir o valor de cada elemento de 1 array:
def imprimir(lista):
    for i in lista:
        if i != 'None':
            print(i)
        else:
            print('Tá estranho')
#print(imprimir([2, 18, 5, 19, 4, 7]))
# Tempo para completar: O(n)

# 4.6 - Duplicar o valor de cada elemento de um array:
def duplica(lista):
    lista_valores_duplicados = []
    for i in lista:
        multiplicacao = i * 2
        lista_valores_duplicados.append(multiplicacao)
    return lista_valores_duplicados

#print(duplica([2, 18, 5, 19, 4, 7]))
# Tempo para completar: O(n)

# 4.7 - Duplicar o valor apenas do primeiro elemento do array:
def duplicarFirst(lista):
    cont = 0
    lista_duplicado_first = []
    for i in lista:
        if cont == 0:
            multiplicacao = i * 2
            lista_duplicado_first.append(multiplicacao)
            cont += 1
        else:
            lista_duplicado_first.append(i)
    return lista_duplicado_first

print(duplicarFirst([2, 18, 5, 19, 4, 7]))
# Tempo para completar: O(n)
# Tempo para completar: O(n2)


