from random import randrange

inicio = int(input('Digite o início do intervalo: '))
fim = int(input('Digite o fim do intervalo: '))

numero = randrange(inicio, fim)
chute = 0
tentativas = 0

while chute != numero:
    chute = int(input('\nAdivinhe o número aleatório do intervalo: '))

    if chute < inicio or chute > fim:
        print('Seu chute está fora do intervalo. Tente de novo.')
    elif numero == chute:
        print(f'Parabéns, você acertou o número em {tentativas} tentativas!')
    elif numero - chute > 3 or chute - numero > 3:
        if numero > chute:
            print('Muito longe! Tente um número maior.')
            tentativas += 1
        else:
            print('Muito longe! Tente um número menor.')
            tentativas += 1
    else:
        print('Quase lá! Tente de novo.')
        tentativas += 1
