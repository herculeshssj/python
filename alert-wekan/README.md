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
./venv/bin/activate
```

Install dependencies:

```
python -m pip install -r requirements.txt
```

Docker build:

```
docker build -t alert-wekan:latest .
```

Docker run:

```
docker run --rm -it --net=host -e MONGO_URL="mongodb://root:root@localhost:27017" -e DISCORD_URL="<enter with discord webhook url>" alert-wekan:latest
```