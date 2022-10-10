Initialize virtual env:

```
python -m venv venv
```

Activate virtual env on Windows using Powershell script: 

```
.\venv\Scripts\Activate.ps1
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
docker run --rm -it --net=host alert-wekan:latest 
```