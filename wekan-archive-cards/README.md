Install dependencies:

```
python -m pip install -r requirements.txt
```

Docker build:

```
docker build -t wekan-archive-cards:latest .
```

Docker run:

```
docker run --rm --net=host --env-file=envfile wekan-archive-cards:latest python wekan-archive-cards.py
```