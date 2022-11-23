contador_de_plays = [156, 141, 35, 94, 88, 61, 111]

def buscaMaior(arr):
    maior = arr[0] #o maior e maior índice até então é o 0
    maior_indice = 0
    for i in range(0, len(arr)):
        if arr[i] > maior: #se o índice i do array for maior do que o valor da variável maior
            maior = arr[i] #a variável irá de atualizar com o novo valor
            maior_indice = i #a variável maior índice também irá se atualizar com o novo valor de i
    return maior_indice

def ordenacaoPorSelecao(arr): #tudo funcionando ok aqui
    novoArr = [] #criando um novo array que vai receber os itens ordenados do maior para o menor
    for i in range(len(arr)): #percorrendo o array antigo
        maior = buscaMaior(arr) #usando a função buscaMaior para encontrar o maior índice
        novoArr.append(arr.pop(maior)) #adicionando o maior índice ao novo array
    return novoArr


print(buscaMaior(contador_de_plays))