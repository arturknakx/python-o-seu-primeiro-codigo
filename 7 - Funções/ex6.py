def adicao(x, y):
    print('Resultado:', x + y)


def subtracao(x, y):
    print('Resultado:', x - y)


def multiplicacao(x, y):
    print('Resultado:', x * y)


def divisao(x, y):
    print('Resultado:', x / y)


# Código principal:

print('OPÇÕES:')
print('----------------------')
print('(1) Adição')
print('(2) Subtração')
print('(3) Multiplicação')
print('(4) Divisão')
print('----------------------')

while True:
    opcao = int(input('Selecione uma opção: '))
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    if opcao == 1:
        adicao(num1, num2)
        repetir = input('Deseja realizar outra operação? ')
        if repetir == 'sim' or repetir == 'Sim':
            continue
        else:
            break

    elif opcao == 2:
        subtracao(num1, num2)
        repetir = input('Deseja realizar outra operação? ')
        if repetir == 'sim' or repetir == 'Sim':
            continue
        else:
            break

    elif opcao == 3:
        multiplicacao(num1, num2)
        repetir = input('Deseja realizar outra operação? ')
        if repetir == 'sim' or repetir == 'Sim':
            continue
        else:
            break

    elif opcao == 4:
        divisao(num1, num2)
        repetir = input('Deseja realizar outra operação? ')
        if repetir == 'sim' or repetir == 'Sim':
            continue
        else:
            break

print('Encerrando programa...')


