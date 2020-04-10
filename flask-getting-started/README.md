Flask Getting Started
---------------------

Para executar o projeto, digite:

```
flask run
```

Para executar a aplicação em Docker, primeiro construa a imagem usando comando:

```
docker build -t flask-getting-started:latest .
```

Após a construção da imagem, execute o container usando:

```
docker run --name flask-app -p 5000:5000 -d flask-getting-started:latest
```