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
docker run --rm -it --net=host alert-wekan:latest 
```