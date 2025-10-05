# WikiCFP Webscraping API

This project provides a REST API service to scrape event information from WikiCFP tables.

## Build the Docker Image

```bash
docker build -t wikicfp-api .
```

## Run the Container

```bash
docker run -d --name wikicfp-api -p 5000:5000 wikicfp-api
```

## Test if the Container is Healthy

```bash
curl http://localhost:5000/health
```

Expected output:

```json
{"status": "ok"}
```

## Send a cURL POST Request to Scrape Events

Replace the URL in the example below with your desired WikiCFP URL.

```bash
curl -X POST http://localhost:5000/scrape \
  -H "Content-Type: application/json" \
  -d '{"url": "http://www.wikicfp.com/cfp/call?conference=artificial%20intelligence"}'
```

The API will return a JSON array with the extracted event information.
