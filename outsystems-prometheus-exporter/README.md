Initialize virtual env:

```
python -m venv venv
```

Activate virtual env on Windows using Powershell script: 

```
.\venv\Scripts\Activate.ps1
```

Activate virtual env on Linux using Shell script: 

```
./venv/bin/activate
```

Install dependencies:

```
python -m pip install -r requirements.txt
```

Docker build:

```
docker build -t outsystems-exporter:latest .
```

Docker run:

```
docker run -d -p 9877:9877 outsystems-exporter:latest 
```