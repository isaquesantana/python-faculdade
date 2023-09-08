# ALGORÍTIMO DE CADASTRO DE COLABORADORES

# ---------- Variáveis Globais ----------
listaColaborador = []
codigoColaborador = 0
# ---------------------------------------

# FUNÇÃO cadastrarColaborador()
def cadastrarColaborador(id):
    print('=' * 70 ) # Marcador inicio de secção
    print('            >>> MENU DE CADASTRO DE COLABORADOR <<< \n')
    

    while (True):
        print('O ID deste(a) colaborador(a): {}' .format(id))
        nome = input('Digite o NOME do Colaborador >>> ')
        setor = input('Digite o SETOR do Colaborador >>> ')
        pag = float(input('Digite o PAGAMENTO do Colaborador (R$) >>> '))
        
        dicioColaborador = {'id'        : id,
                            'nome'      : nome,
                            'setor'     : setor,
                            'pagamento' : pag}
        listaColaborador.append(dicioColaborador.copy())
        return    
# ------------------------------------------------------------------------    

# FUNÇÃO consultarColaborador()
def consultarColaborador():
    print('\n' + '=' * 70 ) # Marcador inicio de secção
    print('            >>> MENU DE CONSULTA DE COLABORADOR <<<')

    while (True):
        opcaoConsulta = input('\nEscolha a opção desejada:\n'+
                            '1 - Consultar Todos os Colaboradores\n'+
                            '2 - Consultar Colaborador por ID\n'+
                            '3 - Consultar Colaborador(es) por Setor\n'+
                            '4 - Retornar\n'+
                            '>>> ')   
    
        if (opcaoConsulta == '1'):
            print('Você escolheu consultar TODOS os colaboradores\n')
            
            # Nesta etapa "colaborador" vai varrer os conjuntos chave do dicionario "listaColaborador".
            for colaborador in listaColaborador:
                print('-------------------------')
                for key, value in colaborador.items():
                    print('{}: {}' .format(key, value))
                print('-------------------------')
            

        elif (opcaoConsulta == '2'):
            print('Você escolheu consultar Colaborador por ID')
            
            # Nesta etapa "colaborador" irá procurar dentro do dicionario "listaColaborador" um valor igual ao informado pelo usuário.
            campoID = int(input('Qual ID deseja consultar >>> '))
            for colaborador in listaColaborador:
                if (colaborador['id'] == campoID):
                    print('-------------------------')
                    for key, value in colaborador.items():
                        print('{}: {}' .format(key, value))
                    print('-------------------------')

        elif (opcaoConsulta == '3'):
            print('Você escolheu consultar Colaborador(es) por SETOR')
            setor = input('Qual setor deseja consultar >>> ')

            for colaborador in listaColaborador:
                if (colaborador['setor'] == setor):
                    print('-------------------------')
                    for key, value in colaborador.items():
                        print('{}: {}' .format(key, value))
                    print('-------------------------')

        elif (opcaoConsulta == '4'):
           break # Retorna para o menu principal
        else:
            print('Opção Inválida. Tente novamente!')
            continue
# ------------------------------------------------------------------------ 

# FUNÇÃO removerColaborador()
def removerColaborador():
    print('\n' + '=' * 100 ) # Marcador inicio de secção
    print('            >>> MENU DE REMOVER COLABORADOR<<<')

    # Nesta etapa "código" irá procurar dentro do dicionario "listaColaborador" um valor igual ao informado pelo usuário, e se encontrar, executar a remoção do cadastro.
    valorDesejado = int(input('Qual ID do Colaborador deseja remover >>> '))
    for codigo in listaColaborador:
        if (codigo['id'] == valorDesejado):
            listaColaborador.remove(codigo)
            print( 'Colaborador Removido')
# ------------------------------------------------------------------------ 

#Programa Principal

# -------------------- MENU --------------------
print('=' * 70 ) # Marcador inicio de secção
print('Bem-vindo ao programa de cadastro de Isaque Gomes dos Passos Santana')

while (True):
    print('=' * 70 ) # Marcador início de secção
    print('            >>> MENU PRINCIPAL <<<')

    opcaoPrincipal = input('\nEscolha a opção desejada:\n'+
                           '1 - Cadastrar Colaborador\n'+
                           '2 - Consultar Colaborador(es)\n'+
                           '3 - Remover Colaborador\n'+
                           '4 - Sair\n'+
                           '>>> ')
    
    if (opcaoPrincipal == '1'):
        codigoColaborador += 1
        cadastrarColaborador(codigoColaborador)
    elif (opcaoPrincipal == '2'):
        consultarColaborador()
    elif (opcaoPrincipal == '3'):
        removerColaborador()
    elif (opcaoPrincipal == '4'):
        print('Encerrando Programa...')
        break
    else:
        print('Opção Inválida. Tente novamente!')
        continue
    