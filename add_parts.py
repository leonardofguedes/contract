from add_rules import add_rules
from parts import Parte

types_geral = {'Locação': ('Locatário','Locador'),
               'Trabalho':('Empregador','Empregado'),
               'Compra E Venda':('Comprador','Vendedor')
               }
types_list = []
contract = []

for n in types_geral.keys():
    types_list.append((f'{n}'))

def find_type_part(n):
    if n in types_geral.keys():
        return types_geral.get(n)


def receive_data(n):
        nome = str(input(f'Nome do {n}: ->')).title().strip()
        nacionalidade = str(input('Nacionalidade: ->')).capitalize().strip()
        es_civil = str(input('Estado Civil: ->')).capitalize().strip()
        profissao = str(input('Profissão: ->')).title().strip()
        cpf = int(input('CPF: ->'))
        residencia = str(input('Residencia: ->')).title().strip()
        person = Parte(n, nome, nacionalidade, es_civil, profissao, cpf, residencia)
        contract.append(person)


def show():
    ask = str(input('Deseja ver o contrato?[Y][N]')).title().strip()
    if ask == 'Y':
        for n in contract:
            print(n)
    if ask == 'N':
        pass
    else:
        pass


def receive_model():
    while True:
        modelo = str(input('Qual o modelo de contrato?')).title().strip()
        if modelo in types_list:
            n = find_type_part(modelo)
            print(f'Vamos cadastrar primeiro o {n[0]} e depois o {n[1]}.')
            receive_data(n[0])
            print(f'Agora o {n[1]}')
            receive_data(n[1])
            return show()
        else:
            print('Esse modelo não está cadastrado.')


def welcome():
    while True:
        type_of_contract = int(input('Se deseja ver os modelos, digite 1.\nSe já sabe sua escolha, digite 2.'
                                     '\nPara interromper o programa digite 9.'))
        if type_of_contract == 1:
            print(types_list)
            pass
        elif type_of_contract == 2:
            receive_model()
            for n in add_rules():
                contract.append(n) 
            break
        elif type_of_contract == 9:
            break
        else:
            print('Escolha uma das opções:\n1 -> Modelos de contrato \nou \n2 -> Escolher o contrato')
            print('*'*30)


def app():
    while True:
        welcome()
        show()






