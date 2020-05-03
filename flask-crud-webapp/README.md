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

Para construir a imagem Docker, digite: 

$ docker build -t flask-crud-webapp:latest .

Para construir a imagem Docker no Windows Server Core, digite:

$ docker build -f Dockerfile_windows -t flask-crud-webapp:latest .

Para criar o container, digite:

$ docker run --name dream-team -p 5000:5000 -d flask-crud-webapp:latest