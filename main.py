
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

#Resultados
empate = 'EMPATE! *__*'
ganhou = 'Parabéns! Você GANHOUU!!! Uhuuuuuu ^^'
perdeu = 'Você PERDEUU! Tente novamente. :/'
erro = '''
Jogada Inválida! O.o
Tente novamente com números menores.'''


print('''\nDigite um número que corresponde à sua opção:\n
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\n''')

jogador = int(input('Me diz qual é a sua Jogada? '))
if jogador <= 2:
    print('J O ', end=' ')
    sleep(1)
    print('K E N ', end=' ')
    sleep(1)
    print('P Ô  ! ! !\n')
    print('-=' * 19)
    sleep(0.2)
    print('Computador jogou [ {} ]'.format(itens[computador]))
    print('Jogador jogou [ {} ]'.format(itens[jogador]))
    print('-=' * 19)

    if computador == 0:  # Computador jogou PEDRA
        if jogador == 0:
            print(empate)

        elif jogador == 1:
            print(ganhou)

        elif jogador == 2:
            print(perdeu)
        else:
            print(erro)

    elif computador == 1:  # Computador jogou PAPEL
        if jogador == 0:
            print(perdeu)

        elif jogador == 1:
            print(empate)

        elif jogador == 2:
            print(ganhou)
        else:
            print(erro)
    elif computador == 2:  # Computador jogou TESOURA
        if jogador == 0:
            print(ganhou)

        elif jogador == 1:
            print(perdeu)

        elif jogador == 2:
            print(empate)

        else:
            print(erro)
else:
    print(erro)
    print('-=' * 18)