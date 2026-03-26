# Ler a expressão como string
expressao = input("Digite dois valores inteiros separados por um operador (+, -, * ou /): ")

# Verificar qual operador está presente e separar os valores
if '+' in expressao:
    a, b = expressao.split('+')
    resultado = int(a) + int(b)

elif '-' in expressao:
    a, b = expressao.split('-')
    resultado = int(a) - int(b)

elif '*' in expressao:
    a, b = expressao.split('*')
    resultado = int(a) * int(b)

elif '/' in expressao:
    a, b = expressao.split('/')
    resultado = int(a) / int(b)

else:
    print("Operador inválido!")
    exit()

# Mostrar o resultado
print("O resultado da operação é", resultado)