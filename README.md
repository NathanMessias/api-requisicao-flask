# api-requisicao-flask
## Introdução
Esse projeto nasceu com o intuito de ajudar estudantes de front end, no estudo de consumo de API's, fornecedendo essa api simples e funcional para facilitar. 
Tive esse mesmo problema quando iniciei meus estudos nessa área. Não achava algo que fosse dedicado para isso, a maioria das soluções na internet, ou tinha muitas
configurações e downloads (o que tornava isso complicado para um iniciante), ou era apenas de consulta e não um CRUD, como essa.

Esse projeto não utilizada banco de dados (menos coisas para se preocupar \o/). Você terá que baixar apenas as dependências, e aconselho a configurar um ambiente virtual
do seu gosto para não prejudicar outras configurações que já possa ter em sua máquina. A forma que é salvo os registros é por meio de um arquivo .txt. Ele é criado, caso
ainda não tenha, na primeira requisição que fizer após iniciar o servidor e, caso já tenha, ele irá apenas atualizar as referências de quantidade e ids que tem no arquivo.
Todo o processo de CRUD é feito manipulando esse arquivo, então tome cuidado como irá mexer nele (já que não precisa msm ;)).

Decidi usar o flask pela sua potencialidade, simplicidade, e porque tem python! Convenhamos, melhor linguagem atualmente 😎 kkk &nbsp;
Além disso, já é algo que tenha familiaridade e convivência.

E essa api é para cadastro de livros, simulando uma biblioteca (ou então qualquer coisa que tenha cadastro de livros hahaha).

Chega de papo, mais abaixo você terá o detalhamento dos endpoints criado, o que ela retorna em cada um, e o que são aceitos para cadastro.

PS: Ah! Só pra constar. API é uma das coisas que mais gosto de fazer também 🥰

## Configuração e Execução
É essencial que você tenha o python instalado na sua máquina. A versão dele tem q ser igual ou superior a versão 3. 

Confirme se o seu python ja está com o pacote
PIP instalado (Digita pip dentro do interpretador e executa, se não der erro de import, ta sussa), de preferência a versão 3 também, com ele que iremos baixar as dependências.

Aconselho a usar uma máquina virtual também, porque as instalações ficarão apenas nesse projeto (isso ai tu vê um tutorial na internet).

Depois disso, vá para o diretório do projeto dentro do interpretador python e execute o seguinte comando:

>pip install -r requirements.txt

Isso fará com que ele instale o Flask e as dependências dele. É pouca coisa, mas necessário

Depois que tiver terminado de instalar, e hora de rodar o projeto. Execute o seguinte comando no mesmo lugar:

>python3 app.py

Tem que ser python3 mesmo, porque se não vai da erro logo no início!

Assim que executar, você ja pode ir para o navegador e digitar:

> localhost:5000

E nisso já verás um 'Hello World' indicando que o projeto ta on. Para utilizar os endpoints apresentados mais em baixo, basta colocar o exemplo de cada endpoint
na frente dessa url do navagador que será sucesso!

Bons Estudos! 😉

## Funcionamento e Endpoints
### Cadastro
Você enviará um formulário configurado com o método POST para o seguinte endpoint:

> /cadastro

É bem provavél que outro método colocado no seu formulário trará algum erro de requisição.
A tabela abaixo demonstra os names (eles devem estar em minúsculos mesmo) que deverão ter cada input do seu formulário, e serão cadastrados apenas esses mencionados na tabela, ok?
Ah! E é obrigatório ter dados preenchidos nesse campo, caso contrário ele retornará um json booleano False.

name       | descrição
-----------|-----------
nome       | Nome do livro que será cadastrado
autor      | Nome do autor do livro
ano        | Ano do livro
editora    | Editora do livro cadastrado

Caso dê tudo certo no cadastro, será retornado um json booleano True.
Caso contrário, json booleano False.

### Listar
Para retornar uma lista com todos os dados cadastrados no arquivo, utilize o seguinte endpoint com o método GET:

> /lista

Ele retornara um vetor json com todos os registro encontrados no arquivo. Exemplo de retorno:

```json
[
    {
        "ano": "2011",
        "autor": "Nathan",
        "editora": "Bandeirantes",
        "id": "1",
        "nome_li": "Livro1"
    }
]
```
### Consultar
A consulta está sendo feita com base no nome do livro. Para utilizar, bastante inserir o **nome** desejado no endpoint com o método GET:

>/consultar/**_nome_**

Caso haja o registro com o nome indicado, será retornado um todos os dados sobre ele, do contrário, será retornado um vetor em branco.

### Alterar
A alteração pode ser feita apenas em um único campo, dois campos ou até mesmo em todos existentes. Para alteração, envie um formulário de dados com os campos preenchidos que se deseja alterar, com o método PUT para o seguinte endpoint com o **id** do registro que se quer alterar:

>/alterar/**_id_**

Ah! Não se esqueça dos names nos campos viu? Se não, o resultado não dará certo.

name       | descrição
-----------|-----------
nome       | Nome do livro que será alterado
autor      | Nome do autor do livro
ano        | Ano do livro
editora    | Editora do livro alterado

Será retornado um json booleano True indicando que deu tudo certo.

### Excluir
Para excluir, basta passar o **id** do registro que se quer deletar para o seguinte endpoint com o método DELETE:

>/excluir/**id**

Será retornado um booleano json **True** indicando que deu tudo certo.

