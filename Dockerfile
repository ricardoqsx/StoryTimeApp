FROM python:alpine

WORKDIR /webApp

RUN apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-connector-c-dev \
    python3-dev

COPY ./webApp .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "index.py"]
