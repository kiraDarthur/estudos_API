#como uasr 4 principais comandos(verbos) de uma API
import requests
from pprint import pprint

#get =» obter informaçoes de uma »»»API COMPLETA««««
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
#pprint(resultado_get.json())

#get com id =»  obter infomaçoes de uma API/ porem so vai retonar um dado espesifico
resultado_get_com_id = requests.get(
    'https://jsonplaceholder.typicode.com/todos/2')
#pprint(resultado_get_com_id.json())

#POST - Criar um novo recurso
nova_tarefa = {'completed': False,
 'title': 'lavar carro',
 'userId': 1}
resultado_post = requests.post(
    'https://jsonplaceholder.typicode.com/todos',nova_tarefa)
pprint(resultado_post.json())

# PUT - Alterar um recurso  existente
tarefa_alterada = {'completed': False,
 'title': 'lavar moto',
 'userId': 1}
resultado_put = requests.put(
    'https://jsonplaceholder.typicode.com/2',tarefa_alterada)
#pprint(resultado_put.json())

#deltar algum recurso
resultado_delete = requests.delete(
    'https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_delete.json())