import random
from time import sleep

print('Vamos jogar um jogo?!\n')
sleep(1)
print('Sim?! Vamos começar!\n')
sleep(1)
print('Vai ser Jokenpô!!!\n')
sleep(1)

lista = ['PEDRA', 'PAPEL', 'TESOURA']

escolha_player = input('Escolha entre pedra, papel e tesoura: ').strip().upper()
escolha_computador = random.choice(lista)

print('JO!')
sleep(0.8)
print('KEN!')
sleep(0.8)
print('PO!')
sleep(0.8)

if escolha_player == 'PEDRA' and escolha_computador == 'TESOURA' and escolha_player == 'PAPEL' and escolha_computador == 'PEDRA' and escolha_player == 'TESOURA' and escolha_computador == 'PAPEL':
    print(f'Você escolheu {escolha_player} e o computador escolheu {escolha_computador}')
    print('Você venceu!!!')
elif escolha_player == escolha_computador:
  print(f'Você escolheu {escolha_player} e o computador escolheu {escolha_computador}')
  print('EMPATE!!!')
else:
  print(f'Você escolheu {escolha_player} e o computador escolheu {escolha_computador}')
  print('Você perdeu!!!')