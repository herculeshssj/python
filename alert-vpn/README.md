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
docker build -t alert-vpn-down:latest .
```

Docker run:

```
docker run --rm -it --net=host -e DISCORD_URL="<enter with discord webhook url>" alert-vpn-down:latest
```