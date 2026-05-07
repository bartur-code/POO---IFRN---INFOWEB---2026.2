X = int(input())
Y = int(input())
Z = int(input())
lista = [X, Y, Z]

menor = min(lista)
maior = max(lista)
meio = sum(lista) - maior - menor
print(meio)

