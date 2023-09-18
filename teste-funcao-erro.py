def tratarErro(input='',tipo=0):
    '''
    Função para tratar erros:
    - Inteiro
    - String
    :param input: Frase do sistema para o usuário
    :param tipo: Tipo string (1) ou tipo inteiro (2)  
    '''
    try:

        if tipo == 1:
            # Se o tipo a ser tratado for string

        elif tipo == 2:
            # Se o tipo a ser tratado for inteiro

        else:
            # Se o tipo a ser tratado for diferente de 1 e 2
            raise ValueError("\033[31mTipo inválido:! O tipo deve ser 1 (string) ou 2 (inteiro).\033[m")

    except Exception as e:
        print(f"Erro: {e}")
        resposta = None 


    return resposta


'''
Inputs que precisam de tratamento de erro 

Linha 71: continuar = int(input('\nSelecione uma opção: '))

Linha 165: resp = int(input('\nSelecione uma opção: '))

Linha 215: duvida = int(input('\nQual é o número da sua dúvida? '))

Linha 275: sug = input('\nDigite a sua sugestão: ')

Linha 312: escolha_lixeira = int(input('\nQual lixeira você deseja verificar? '))

Linha 404: perg = int(input('\nOpção: '))

'''




