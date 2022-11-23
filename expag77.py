# 4.1 - Escreva o código para a função soma, vista anteriormente:

def soma(lista):
    total = 0
    for i in lista:
        total += i
    return total

#print(soma([2,5,7]))

# 4.2 - Escreva uma função recursiva que conte o número de itens em uma lista:

def contagemItens(lista):
    total_itens = 0
    if lista == []:
        return 0
    if lista != []:
        for i in lista:
            total_itens += 1
    return total_itens

#Resposta livro:
def conta(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

#print(conta([2, 7, 19, 22, 51, 17]))

# 4.3 - Encontre o valor mais alto em uma lista

def maiorValor(lista):
    maior = 0
    for i in lista:
        if i > maior:
            maior = i
    return maior

#print(maiorValor([2, 7, 19,22, 51, 17]))

# 4.4 - Você se lembra da pesquisa binária do Capítulo 1? Ela também é um algoritmo do tipo dividir para conquistar.
# Você consegue determinar o caso-base e o caso recursivo para a pesquisa binária?
# Resposta: Caso-base: uma lista vazia ou com 1 elemento apenas.
# Caso recursivo: código da pesquisa binária.
