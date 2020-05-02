Para executar no terminal (cmd.exe):

$ set FLASK_CONFIG=development
$ set FLASK_APP=run.py
$ flask run

Comandos para inicializar a base:

$ flask db init
$ flask db migrate
$ flask db upgrade

Para rodar o teste, digite:

$ python tests.py