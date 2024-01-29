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


Comando no terminal:

```shell
sudo logkeys -s --timestamp-every --post-http=http://localhost:5000/receive_log --post-size=10k
```