from flask import Flask, jsonify, request
from estrutura_banco_de_dados import Autor,Postagem,app,db


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



@app.route('/autores')
def abter_autores():
    autores = Autor.query.all()
    lista_de_autores =[]
    for autor in autores:
        autor_atual = {}
        autor_atual  ['id_autor'] = autor.id_autor
        autor_atual ['nome'] = autor.nome
        autor_atual ['email'] = autor.email
        lista_de_autores.append(autor_atual)

    return jsonify({'autores':lista_de_autores})


@app.route('/autores/<int:id_autor>',methods=['GET'])
def obter_autor_por_id(id_autor):
    pass
@app.route('/autores',methods=['POST'])
def novo_autor():
    pass
@app.route('/autores/<int:id_autor>',methods=['PUT'])
def alterar_autor(id_autor):
    pass

@app.route('/autores/<int:id_autor>',methods=['DELETE'])
def excluir_autor(id_autor):
    pass




# Executa a aplicação Flask no host 'localhost' e porta 5000
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
