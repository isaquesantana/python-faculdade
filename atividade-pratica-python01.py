# ALGORÍTIMO DE DESCONTO EM PRODUTO

print('Bem-vindo à Loja do Isaque Gomes dos Passos Santana')

# Etapa onde serão solicitados os dados necessários e realizado o cálculo do valor a ser pago sem desconto.
valorProduto = float(input('Digite o valor unitário do produto: '))
qtdProduto = int(input('Digite a quantidade do produto: '))
valorSem = valorProduto * qtdProduto

print('Valor SEM desconto: R$ {:.2f}'.format(valorSem))

# Etapa em que a quantidade será verificada e o percentual de desconto será aplicado conforme a quantidade.
if (qtdProduto < 200):
    print('Não é aplicado nenhum desconto para compras com menos de 200 unidades.')
elif ((qtdProduto >= 200) and (qtdProduto < 1000)):
    valorDesconto = valorSem - (valorSem * 0.05)
    print('Valor COM desconto de 5%: R$ {:.2f}'.format(valorDesconto))
elif ((qtdProduto >= 1000) and (qtdProduto < 2000)):
    valorDesconto = valorSem - (valorSem * 0.1)
    print('Valor COM desconto de 10%: R$ {:.2f}'.format(valorDesconto))
else:
    valorDesconto = valorSem - (valorSem * 0.15)
    print('Valor COM desconto de 15%: R$ {:.2f}'.format(valorDesconto))
    