#ALGORÍTIMO DE CARDÁPIO DE SORVETE

print('Bem-vindo à Sorveteria do Isaque Gomes dos Passos Santana')
print('-' * 36, 'CARDÁPIO', '-' * 36)
print('| Nº DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |')
print('|      1      |         R$ 6,00        |       R$ 7,00      |       R$ 8,00       |')
print('|      2      |         R$ 10,00       |       R$ 12,00     |       R$ 14,00      |')
print('|      3      |         R$ 14,00       |       R$ 17,00     |       R$ 20,00      |')
print('----------------------------------------------------------------------------------')

acumulador = 0

while True:

    # Nesta etapa é solicitado ao usuário o sabor e a quantidade de bolas que deseja pedir, caso ele digite uma opção não disponível, ele fica preso em um loop até que digite uma opção válida.
    
    sabor = input('Escolha um sabor (tr/pr/es): ')
    while sabor not in ('tr', 'pr', 'es'):
        print('Sabor inválido. Digite um sabor disponível!')
        sabor = input('Escolha um sabor (tr/pr/es): ')

    print()
    qtdBolas = input('Quantas bolas de sorvete deseja (1/2/3): ')
    while qtdBolas not in ('1', '2', '3'):
        print('Quantidade não disponível. Digite uma quantidade válida!')
        qtdBolas = input('Quantas bolas de sorvete deseja (1/2/3): ')
    
    print()
    
    # Na etapa abaixo está sendo verificado qual sabor escolhido e a quantidade de bolas, e adicionado o respectivo valor à variável "acumulador".
    
    # Sabor Tradicional (tr) e suas quantidades
    if (sabor == 'tr') and (qtdBolas == '1'):
        print('Você escolheu o sabor Tradicional com 1 bola R$ 6,00')
        acumulador += 6
        
    elif (sabor == 'tr') and (qtdBolas == '2'):
        print('Você escolheu o sabor Tradicional com 2 bolas R$ 10,00')
        acumulador += 10

    elif (sabor == 'tr') and (qtdBolas == '3'):
        print('Você escolheu o sabor Tradicional com 3 bolas R$ 14,00')
        acumulador += 14

    # Sabor Premium (pr) e suas quantidades
    elif (sabor == 'pr') and (qtdBolas == '1'):
        print('Você escolheu o sabor Premium com 1 bola R$ 7,00')
        acumulador += 7
        
    elif (sabor == 'pr') and (qtdBolas == '2'):
        print('Você escolheu o sabor Premium com 2 bolas R$ 12,00')
        acumulador += 12

    elif (sabor == 'pr') and (qtdBolas == '3'):
        print('Você escolheu o sabor Premium com 3 bolas R$ 17,00')
        acumulador += 17

    # Sabor Especial (es) e suas quantidades
    elif (sabor == 'es') and (qtdBolas == '1'):
        print('Você escolheu o sabor Especial com 1 bola R$ 8,00')
        acumulador += 8
        
    elif (sabor == 'es') and (qtdBolas == '2'):
        print('Você escolheu o sabor Especial com 2 bolas R$ 14,00')
        acumulador += 14

    elif (sabor == 'es') and (qtdBolas == '3'):
        print('Você escolheu o sabor Especial com 3 bolas R$ 20,00')
        acumulador += 20

    print()
    resposta = input('Gostaria de adicionar mais um pedido?(s/n)')
    if (resposta == 's'):
        continue
    else:
        break

print('Pedido fechado!')
print('Total a Pagar: R$ {:.2f}'.format(acumulador))
