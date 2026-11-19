n = int(input()); idades = list(map(lambda x: int(x), input().strip().split()))
if len(idades) != n: raise ValueError
ordem_idosos = sorted(filter(lambda x: x >= 60, idades)); ordem_idosos.reverse()
lista_tempos = []
for i in ordem_idosos: 
    contador = 0
    while idades.index(i) != ordem_idosos.index(i):
        indice = idades.index(i)
        anterior = idades[indice - 1]
        idades[indice - 1] = i
        idades[indice] = anterior
        contador += 1
    lista_tempos.append(contador)
#print(ordem_idosos)
#print(lista_tempos)
#print(idades)
print(f'Levaria {max(lista_tempos)} segundos!')