import sqlite3

# Conexão com o banco de dados (ou criação do arquivo do banco de dados se não existir)
with sqlite3.connect('artistas.db') as conexao:
    # Criar um cursor para executar comandos SQL
    sql = conexao.cursor()

    # Verificar se a tabela 'banda' já existe
    cursor = sql.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='banda';")
    tabela_existe = cursor.fetchone()

    # Se a tabela não existir, criar a tabela 'banda'
    if not tabela_existe:
        sql.execute('CREATE TABLE banda (nome TEXT, estilo TEXT, membros INTEGER);')

    # Exemplo de inserção de dados na tabela 'banda'
    sql.execute('INSERT INTO banda (nome, estilo, membros) VALUES ("Banda 1", "Rock", 3)')

    # Exemplo de inserção de dados com entrada do usuário
    nome = input('Digite o nome da banda: ')
    estilo = input('Digite o estilo da banda: ')
    quantidade_membros = int(input('Quantidade de membros da banda: '))

    sql.execute('INSERT INTO banda VALUES (?, ?, ?)', (nome, estilo, quantidade_membros))

    # Salvar as alterações no banco de dados
    conexao.commit()

    # Exibir os dados da tabela 'banda' no console
    bandas = sql.execute('SELECT * FROM banda;')
    for banda in bandas:
        print(banda)
