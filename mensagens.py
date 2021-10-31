import db
import os

MENU_INICIAL = 99

def exibir_cabecalho():
    '''imprimi o cabeçalho no terminal utilizando o tamanho maximo de 60 caracteres'''
    QTD_COLUNAS = 60
    print ("-" * QTD_COLUNAS)
    print ("{:^60}".format('TAREFAS'))
    print ("-" * QTD_COLUNAS)
    print ("{:^60}".format('tecle 99 volta para o menu inicial, [CTRL+C] para sair'))
    print ("-" * QTD_COLUNAS)

def exibir_tarefas():
    '''exibe a lista de tarefas cadastradas, com algumas formatações básicas'''
    for tarefa in db.get_tarefas():
        # check = \u2713 é o caracter unicode que representa o concluido
        check = u'\u2713' if tarefa[2] == 1 else ''
        '''
            os parâmetros passados para esse format() são o seguinte:
            {:>4}  = 4 posições, alinhado a direita
            {:<47} = 47 posições, alinhado a esquerda
            {:^3}  = 3 posições, centralizado
        '''
        t = f'- [{tarefa[0]:>4}] {tarefa[1]:<47} {check:^3}'
        print (t)
    print ('-' * 60)

def mostrar_opcao_nova_tarefa():
    texto_nova_tarefa = input('Descreva a tarefa -> ')
    print ('adicionando tarefa -> ' + str(texto_nova_tarefa))
    if texto_nova_tarefa != str(MENU_INICIAL):
        db.add_tarefa(texto_nova_tarefa)

def mostrar_opcao_concluir_tarefa():
    cd_tarefa = int(input('Qual tarefa deseja concluir? digite o código -> '))
    print ('Concluindo tarefa -> ' + str(cd_tarefa))
    if cd_tarefa != MENU_INICIAL:
        db.concluir_tarefa(cd_tarefa)

def mostrar_opcao_excluir_tarefa():
    cd_tarefa = int(input('Qual tarefa deseja excluir? digite o código -> '))
    print('Excluindo tarefa -> ' + str(cd_tarefa))
    if cd_tarefa != MENU_INICIAL:
        db.remover_tarefa(cd_tarefa)

def mostrar_opcao_apagar_tabela():
    db.apagar_tabela()
    os.system('cls')
