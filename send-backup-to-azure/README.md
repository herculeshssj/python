### Installation

Install dependencies:

```
python -m pip install -r requirements.txt
```

Docker build:

```
docker build -t send-backup-azure:latest .
```

Docker run:

```
docker run --rm --env-file=envfile -v "$PWD":/data send-backup-azure:latest python send-backup-to-azure.py teste.txt
```

### Warning

If your environment has more than one Docker network created, build the image with the --network=host parameter.

```
docker build --network=host -t send-backup-azure:latest .
```