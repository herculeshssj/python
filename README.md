# python
Projetos desenvolvidos em Python para Web, Engenharia de Dados e Ciência de Dados

_*Requisitos*_
- Python 3.14
- PostgreSQL 15

Inicialize o ambiente de desenvolvimento com o seguinte comando:

```
python -m venv venv
```

Logo em seguida, ative o ambiente com o seguinte comando:

```
./venv/Scripts/activate
```

No Linux, ative o ambiente com o seguinte comando:

```
source ./venv/bin/activate
```

Install dependencies:

```
python -m pip install -r requirements.txt
```

Docker build:

```
docker build -t python-projects:latest .
```

Docker run:

```
docker run -d --name python-projects -p 8000:8000 --env-file=envfile python-projects:latest
```