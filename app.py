import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Quantidade de registros inseridos no arquivo e controle de ids
quantidade = None
ids = None

# Diretório de dados
diretorio = 'banco_de_dados/dados.txt'


# Função de inicialização
@app.before_first_request
def init():
    global quantidade, ids
    if not os.path.isdir('banco_de_dados'):
        os.mkdir('banco_de_dados')

    if not os.path.isfile(diretorio):
        quantidade = 0
        ids = 0
        arquivo = open(diretorio, 'w+')
        arquivo.writelines('quantidade = 0; ids = 0;')
        arquivo.close()
    else:
        arquivo = open(diretorio, 'r')
        linha = arquivo.readline()
        linhas = linha.split(';')
        quantidade = int(linhas[0].split(' ')[2])
        ids = int(linhas[1].split(' ')[3])
        arquivo.close()


# Função para alterar indicador de quantidade e ids de registros
def alterar_quantidade():
    global quantidade, ids

    with open(diretorio, 'r') as f:
        texto = f.readlines()

    texto[0] = 'quantidade = %s; ids = %s;\n' % (quantidade, ids)

    with open(diretorio, 'w') as f:
        f.writelines(texto)


# Apresentação inicial
@app.route('/')
def hello():
    return 'Hello World!'


# URL de cadastro
@app.route('/cadastro', methods=['POST'])
def cadastro():
    global quantidade, ids
    nome = request.form.get('nome')
    autor = request.form.get('autor')
    ano = request.form.get('ano')
    editora = request.form.get('editora')

    # print(quantidade)

    if '' or None in (nome, autor, ano, editora):
        return jsonify(False)

    else:
        quantidade += 1
        ids += 1
        lista_arquivos = ['\nid: ' + str(ids), '\nnome: ' + nome, '\nautor: ' + autor,
                          '\nano: ' + ano, '\neditora: ' + editora]

        with open('banco_de_dados/dados.txt', 'a+') as arquivo:
            arquivo.write('\n{')
            arquivo.writelines(lista_arquivos)
            arquivo.write('\n},')

        alterar_quantidade()

        return jsonify(True)


# URL de listagem
@app.route('/lista', methods=['GET'])
def lista():
    i = 0
    vetor = []
    with open(diretorio, 'r') as f:
        linhas = f.readlines()
        qtd_linhas = len(linhas)

    while i < qtd_linhas:
        if linhas[i].strip('\n') == '{':
            aux = {
                'id': linhas[i + 1].split(':')[1].split('\n')[0].replace(' ', ''),
                'nome_li': linhas[i + 2].split(':')[1].split('\n')[0].replace(' ', ''),
                'autor': linhas[i + 3].split(':')[1].split('\n')[0].replace(' ', ''),
                'ano': linhas[i + 4].split(':')[1].split('\n')[0].replace(' ', ''),
                'editora': linhas[i + 5].split(':')[1].split('\n')[0].replace(' ', ''),
            }

            vetor.append(aux)
        i += 1

    return jsonify(vetor)


# URL de consulta individual
@app.route('/consultar/<string:nome>', methods=['GET'])
def consultar(nome):
    i = 0
    vetor = []
    with open(diretorio, 'r') as f:
        linhas = f.readlines()
        qtd_linhas = len(linhas)

    while i < qtd_linhas:
        if 'nome: %s' % nome in linhas[i].strip('\n'):
            aux = {
                'id': linhas[i - 1].split(':')[1].split('\n')[0].replace(' ', ''),
                'nome_li': linhas[i].split(':')[1].split('\n')[0].replace(' ', ''),
                'autor': linhas[i + 1].split(':')[1].split('\n')[0].replace(' ', ''),
                'ano': linhas[i + 2].split(':')[1].split('\n')[0].replace(' ', ''),
                'editora': linhas[i + 3].split(':')[1].split('\n')[0].replace(' ', ''),
            }

            vetor.append(aux)
        i += 1

    return jsonify(vetor)


# URL de alteração
@app.route('/alterar/<int:id>', methods=['PUT'])
def alterar(id):
    i = 0

    nome = False
    autor = False
    ano = False
    editora = False

    if request.form.get('nome'):
        nome = request.form.get('nome')
    if request.form.get('autor'):
        autor = request.form.get('autor')
    if request.form.get('ano'):
        ano = request.form.get('ano')
    if request.form.get('editora'):
        editora = request.form.get('editora')

    with open(diretorio, 'r') as f:
        linhas = f.readlines()
        qtd_linhas = len(linhas)

    with open(diretorio, 'w') as f:
        while i < qtd_linhas:
            if linhas[i].strip('\n') == '{':
                f.write(linhas[i])

                if linhas[i + 1].strip('\n') == 'id: %s' % id:
                    f.write(linhas[i + 1])
                    i += 1

                    if nome:
                        f.write('nome: %s\n' % nome)
                    else:
                        f.write(linhas[i + 1])

                    if autor:
                        f.write('autor: %s\n' % autor)
                    else:
                        f.write(linhas[i + 2])

                    if ano:
                        f.write('ano: %s\n' % ano)
                    else:
                        f.write(linhas[i + 3])

                    if editora:
                        f.write('editora: %s\n' % editora)
                    else:
                        f.write(linhas[i + 4])

                    i += 4
            else:
                f.write(linhas[i])

            i += 1

    return jsonify(True)


# URL de excluir
@app.route('/excluir/<int:id>', methods=['DELETE'])
def excluir(id):
    global quantidade

    i = 0
    sinal_documento = False

    with open(diretorio, 'r') as f:
        linhas = f.readlines()
        qtd_linhas = len(linhas)

    with open(diretorio, 'w') as f:
        while i < qtd_linhas:
            if linhas[i].strip('\n') == '{':

                if linhas[i + 1].strip('\n') == 'id: %s' % id:
                    i += 6
                    quantidade -= 1
                    sinal_documento = True
                    print(i)
                    print(qtd_linhas)
                else:
                    f.write(linhas[i])
            else:
                f.write(linhas[i])
            i += 1

    if sinal_documento:
        alterar_quantidade()

    return jsonify(True)


app.run(debug=True)
