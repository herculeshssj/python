FROM python:3.12-slim

WORKDIR /app

COPY wiki-cfp-webscraping-api.py .

# Install dependencies
RUN pip install --no-cache-dir flask requests beautifulsoup4

EXPOSE 5000

CMD ["python", "wiki-cfp-webscraping-api.py"]