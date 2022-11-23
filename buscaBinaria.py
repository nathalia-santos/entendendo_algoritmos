def pesquisa_binaria(lista, item):
    menor = 0
    maior = len(lista) - 1
    meio = 0

    while menor <= maior:
        meio = (menor + maior) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))
