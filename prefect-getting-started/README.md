# Prefect Getting Started

Install:

```sh
pip install prefect
```

Verify the installation:

```
prefect version
```

Run example:

```sh
uv run 01_getting_started.py
```

Start a Docker server:

```sh
docker run -p 4200:4200 -d --rm prefecthq/prefect:3-latest -- prefect server start --host 0.0.0.0
```