from flask import Flask, jsonify, request

# Cria uma instância da aplicação Flask/ com nome da porta atual
app = Flask(__name__)

# Lista de dicionários representando postagens /simulando um banco de dados
postagens = [
    {'titulo': 'Minha historia', 'autor': 'Amanda Dias'},
    {'titulo': 'Novo Dispositivo', 'autor': 'Howard Stringer'},
    {'titulo': 'Lançamento do ano', 'autor': 'Eliane Vieira'}
]

# Definição da rota padrão ('/') para obter postagens
@app.route('/')
def obter_postagens():
    # Retorna as postagens como JSON
    return jsonify(postagens)

# Obter postagem com id - GET http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>',methods=['GET'])
def obter_postagem_por_indice(indice):
    return jsonify(postagens[indice])

# Criar uma nova  postagem -POST  http://localhost:5000/postagem
@app.route('/postagem', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)
    return jsonify(postagem,200)

#alterar a postagem existente-PUT http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>',methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)
    return jsonify(postagens[indice],200)


#excluir uma postagem  - DELETE - http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>',methods=['DELETE'])
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
           del postagens[indice]
           return jsonify(f'Foi excluido a postagem {postagens[indice]}',200)
    except:
        return jsonify('Nao foi possivel encontrar a postagem para exclusao',404)






# Executa a aplicação Flask no host 'localhost' e porta 5000
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
