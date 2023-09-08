#ALGORÍTIMO DE PREÇO PETSHOP

# Função cachorroPeso() | Responsável por retornar à variável "peso", o peso do cachorro.
def cachorroPeso():
    print('----------------- Menu 1 de 3 - Peso Cachorro -----------------')
    while (True):
        global peso

        # Nesta etapa é solicitado o peso do cachorro, se o dado informado não for um valor numérico, aparece uma mensagem informando e solicita novamente um valor válido.
        try:
            pesoCachorro = int(input('Digite o peso do Cachorro (kg): '))
            if (pesoCachorro < 3):
                print('Para cães com peso menor que 3 kg, o valor base é de 40 reais;')
                peso += 40
                return peso
            elif ((pesoCachorro >= 3) and (pesoCachorro < 10)):
                print('Para cães com peso igual ou maior que 3 kg e menor que 10 kg, o valor base é de R$ 50,00')
                peso += 50
                return peso
            elif ((pesoCachorro >= 10) and (pesoCachorro < 30)):
                print('Para cães com peso igual ou maior que 10 kg e menor que 30 kg, o valor base é de R$ 60,00')
                peso += 60
                return peso
            elif ((pesoCachorro >= 30) and (pesoCachorro <= 50)):
                print('Para cães com peso igual ou maior que 30 kg e menor que 50 kg, o valor base é de R$ 70,00')
                peso += 70
                return peso
            else:
                print('Infelizmente não aceitamos cachorros com mais de 50 kg')
                continue
        except ValueError: # Caso o usuário digite letras ao invés de números.
            print('Valor não numérico. Digite um peso válido')
            continue

# Função cachorroPelo() | Responsável por definir à variável "pelo", o tipo de pelo do cachorro.
def cachorroPelo():
    global pelo
    print('\n----------------- Menu 2 de 3 - Pelo Cachorro -----------------')
    print('c - Pelo Curto')
    print('m - Pelo Médio')
    print('l - Pelo Longo')

    while (True): 
        peloCachorro = input('\nInforme o tipo de pelo do cachorro (c/m/l): ')
        if (peloCachorro == "c"):
            print('Para cães com pelo curto (c), o multiplicador é 1')
            pelo += 1
            return pelo
        elif (peloCachorro == "m"):
            print('Para cães com pelo médio (m), o multiplicador é 1.5')
            pelo += 1.5
            return pelo
        elif (peloCachorro == "l"):
            print('Para cães com pelo longo (l), o multiplicador é 2')
            pelo += 2
            return pelo
        else:
            print('Tipo de pelo inválido!')
            continue

# Função cachorroExtra() | Responsável por calcular os extras solicitados e retornar à variável "extra", o total. 
def cachorroExtra():
    global extra
    acumuladorExtra = 0

    print('\n----------------- Menu 3 de 3 - Extras        -----------------')
    print('(1) Corte de Unhas           | R$ 10,00')
    print('(2) Escovar Dentes           | R$ 12,00')
    print('(3) Limpeza de Orelhas       | R$ 15,00')
    print('(0) Não desejo mais nada')
    
    # Nesta etapa é perguntado se o usuário quer adicionar mais algum serviço, enquanto não digitado o valor "0", continuará sendo solicitado um valor e somado ao valor escolhido anteriormente.
    while (True):
        extraPergunta = input('\nDeseja adicionar mais algum serviço? \nEscolha entre (1/2/3/0): ')
        if (extraPergunta == '1'):
            acumuladorExtra += 10
        elif (extraPergunta == '2'):
            acumuladorExtra += 12
        elif (extraPergunta == '3'):
            acumuladorExtra += 15
        elif (extraPergunta == '0'):
            print('Total de extra R$ {:.2f}'.format(acumuladorExtra))
            extra += acumuladorExtra
            return extra
        else:
            print('Opção inválida!')
            continue

# Programa Principal

# Variáveis usadas dentro das funções para ter um valor separado para cada informação solicitada ao usuário e poder mostrá-las de forma individual no demonstrativo do total.
peso = 0
pelo = 0
extra = 0

print('Bem-vindo ao petshop do Isaque Gomes dos Passos Santana!')
print('=' * 100)
cachorroPeso()
print('=' * 100)
cachorroPelo()
print('=' * 100)
cachorroExtra()
print('=' * 100)

print('=' * 100)
print('Valor Total do serviço R$ {:.2f} (peso {} * pelo: {} + adicional: {})'.format((peso * pelo + extra), peso, pelo, extra))
print('=' * 100)