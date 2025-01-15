Build the Docker image:

```sh
docker build -t streamlit .
```

Run the Docker container:

```sh
docker run -p 8501:8501 streamlit
```