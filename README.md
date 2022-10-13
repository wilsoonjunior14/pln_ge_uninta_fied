# pln_ge_uninta_fied
Grupo de Estudos para coletar tweets e processamento de dados

# Colaboradores do Projeto
- Francisco Wilson (Email)
- André Luiz (andreluizmterceiro@gmail.com) (88994174976)
- Nalberty Meneses (nmenesessulino3@gmail.com) (88992567361)
- Victor Correia (victorcorreia88@gmail.com) (8894613479)
- Willian (Email)
- Danny Luan (Email) - Saiu do projeto 22-09-22

# Atividades
- [X] Criar cadastro na plataforma Twitter API V2 (08-09-2022) - (06/10/2022)
  - [twitter api v2](https://developer.twitter.com/en/docs/twitter-api)
- [X] Realizar requisições HTTP para api do twitter (22-09-2022)
  - [Passo a Passo HTTP request no Twitter](https://developer.twitter.com/en/docs/tutorials/step-by-step-guide-to-making-your-first-request-to-the-twitter-api-v2)
  - ![image](https://user-images.githubusercontent.com/19149664/189213185-b57323ce-9811-4176-b0e4-3b866529b828.png)
  - [X] Criar um arquivo isolado para realizar requisições HTTP (e.g.: request.py)
  - [X] Investigar bibliotecas para realizar essas requisições HTTP
    - https://www.w3schools.com/python/module_requests.asp
  - [ ] Investigar na documentação da API do twitter como enviar parâmetros para coletar tweets
    - https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all
    ```
      x = requests.get('https://api.twitter.com/2/users?     ids=2244994945&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,url,username,verified,withheld&expansions=pinned_tweet_id', headers=headers)
    ```
- [ ] Salvar os tweets (24-09-22)
  - [ ] MySQL
  - [ ] SQLite
  - [ ] Analisar as informações vindas dos tweets
  - [ ] Criar as tabelas do banco de dados
  - [ ] Persistir os dados no banco de dados
    - http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
    - https://acervolima.com/python-sqlite-criar-tabela/
    - https://www.tutorialspoint.com/hibernate/hibernate_examples.htm
    - https://pypi.org/project/orm/
- [ ] Processar alguns tweets, usando NLTK
  - https://www.nltk.org/
  - https://likegeeks.com/nlp-tutorial-using-python-nltk/
- [ ] App Destkop
  - https://pyforms.readthedocs.io/en/v4/
  - https://realpython.com/python-gui-tkinter/
  - https://pypi.org/project/PyQt5/ ou https://build-system.fman.io/pyqt5-tutorial
  - https://acervolima.com/introducao-ao-pysimplegui/
