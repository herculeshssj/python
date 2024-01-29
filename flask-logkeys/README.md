Logkeys POST URL
================

Inicializar o ambiente virtual do Python:

```shell
python3 -m venv venv
```

Dar permissão de execução ao script que inicia o ambiente virtual:

```shell
chmod 755 venv/bin/activate
```

Iniciar o ambiente virtual:

```shell
./venv/bin/activate
```

Atualizar o pip:

```shell
python3 -m pip install --upgrade pip
```

Instalar as dependências:

```shell
python3 -m pip install -r requirements.txt
```

Base de dados: a base de dados precisa ficar no diretório __/data__. Crie o diretório e dê permissão para o usuário que irá executar o container Docker. Depois copie o arquivo logkeys.db para o diretório __/data__.


Executar a aplicação:

```shell
python3 app.py
```

Comando no terminal para coleta dos dados:

```shell
sudo logkeys -s --timestamp-every --post-http=http://logkeys-server:5000/receive_log --post-size=10k
```

Construção da imagem Docker:

```shell
docker build -t logkeys:latest .
```

Executar o container Docker:

```shell
docker run --name logkeys-container -p 5000:5000 -v /data:/data -d logkeys:latest
```