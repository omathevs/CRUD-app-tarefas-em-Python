'''Iniciaremos com o módulo que fará a conexão com o banco de dados. 
Os principais métodos do sqlite utilizados são connect(), execute() e commit()

connect(path_arquivo) retorna uma conexão com o banco de dados sqlite que no nosso caso 
é o arquivo "todo-app.db" que será criado no diretório da aplicação.

conn.execute(sql, tupla) executa comandos sql utilizando a conexão ao banco. 
O primeiro argumento é o código sql e o segundo parametro (opcional) é uma tupla 
com as variáveis que serão usadas na consulta. Esse comando retorna um objeto cursor 
o qual podemos interar e ler os resultados da consulta.

conn.commit() comita (salva definitivamente) as alterações realizadas no banco de dados'''

import sqlite3

# conecta ao banco de dados 'todo-app'
# caso o banco não exista ele será criado
conn = sqlite3.connect('todo-app.db')

def criar_tabela_todo():
    '''cria a tabela 'tarefa' caso ela não exista'''
    cursor = conn.cursor()
    conn.execute('''
    create table if not exists tarefa(
        cd_tarefa integer primary key autoincrement,
        tarefa text,
        concluido integer
    )
    ''')

def add_tarefa(tarefa):
    '''adiciona uma nova tarefa'''
    conn.execute('insert into tarefa (tarefa, concluido) values (?, 0)', (tarefa, ))
    conn.commit()

def remover_tarefa(cd_tarefa):
    '''remove tarefa da tabela'''
    conn.execute('delete from tarefa where cd_tarefa = ?', (cd_tarefa, ))
    conn.commit()

def concluir_tarefa(cd_tarefa):
    '''marca a tarefa como concluída'''
    conn.execute('update tarefa set concluido = 1 where cd_tarefa = ?', (cd_tarefa, ))
    conn.commit()

def get_tarefas(): # retorna um cursor
    '''retorna a lista de tarefas cadastradas'''
    return conn.execute('select cd_tarefa, tarefa, concluido from tarefa')

def apagar_tabela():
    '''apaga a tabela inteira'''
    conn.execute('drop table tarefa')
