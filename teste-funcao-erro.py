def tratarErro(inputTratamento='',tipo=''):
    '''
    Função para tratar erros:
    - Inteiro
    - String
    :param inputTratamento: Frase do sistema para o usuário
    :param tipo: Tipo string "str" ou tipo inteiro "int"
    '''
    try:
        if tipo == 'str':
            # Se o tipo a ser tratado for string
            if not isinstance(inputTratamento, str):
                raise ValueError("\033[31mErro! A entrada deve ser uma <string>.\033[m")

        
        elif tipo == 'int':
            # Se o tipo a ser tratado for inteiro
            if not inputTratamento.isdigit():
                raise ValueError("\033[31mErro: A entrada deve ser um número inteiro.\033[m")

        else:
            # Se o tipo a ser tratado for diferente de string ou int
            raise ValueError("\033[31mTipo inválido:! O tipo deve ser <string> ou <int>.\033[m")

    except Exception as e:
        print(f"Erro: {e}")



'''
Inputs que precisam de tratamento de erro 

- Linha 71: continuar = int(input('\nSelecione uma opção: '))

- Linha 165: resp = int(input('\nSelecione uma opção: '))

- Linha 215: duvida = int(input('\nQual é o número da sua dúvida? '))

- Linha 275: sug = input('\nDigite a sua sugestão: ')

- Linha 312: escolha_lixeira = int(input('\nQual lixeira você deseja verificar? '))

- Linha 404: perg = int(input('\nOpção: '))

'''


n = input(': ')
tratarErro(n, 'int')

