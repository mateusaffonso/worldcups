## Orientações do Projeto WorldCups

Você precisa ter o mysql instalado e executando.

Eu recomendo [criar uma virtual-env em python](https://docs.python.org/pt-br/3/library/venv.html) para installar o projeto

O projeto foi feito em python3, e você deve instala-lo com:

```sh
$ pip3 install -r requirements.txt
```

Você precisará restaurar o bancos de dados, para isso se conecte ao MySQL:

```sh
mysql> create database StarWars;
mysql> exit
$ mysql -u root -p  FIFA2 < FIFA.sql
```

*OBS: Pode ser necessário rodar os códigos de LOAD FILE LOCAL do arquivo FIFA.sql no seu prompt para popular o banco de dados*

Após isso mude as configurações do arquivo `config.yaml` com as configurações do seu banco.
OBS: Se você estiver usando um `host`ou uma porta diferente do padrão, apenas adicione junto com os outros campos um campo `host: "meu_novo_host"`e `port: XXXX`substituindo os valores pelos seus.

Após essas etapas, você pode rodar o projeto com :

```sh
$ python app.py
```

## Documentação está no link a seguir:

[Documentação](https://docs.google.com/document/d/17qOWRfYog9Y8ruOXzzrAD5BVnU_-JRKM/edit?usp=sharing&ouid=111957843050007930631&rtpof=true&sd=true)

Projeto desenvolvido pelos alunos: [Cristina Souza](https://www.linkedin.com/in/cris-tina/), [Thiago Barcelos](https://www.linkedin.com/in/thiago-barcellos), [Victor Lima](https://www.linkedin.com/in/victorplima/) e [Mateus Augusto](https://www.linkedin.com/in/mateusaffonso/) para a matéria de Banco de dados do Bacharelado em Ciência da Computação pela UFRJ.
