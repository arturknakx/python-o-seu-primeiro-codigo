while True:
    opcao = int(input('Digite uma opção (1 ou 2): '))
    if opcao == 1:
        print('Opção 1 selecionada.')
        break
    elif opcao == 2:
        print('Opção 2 selecionada.')
        break
    else:
        print('Selecione uma opção válida.')
        continue

print('Loop finalizado.')
