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

Ele retornara um vetor json com todos os registro encontrados no arquivo. Exemplo de retorn

"
"json
