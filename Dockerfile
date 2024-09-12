FROM python:alpine3.19

WORKDIR /webApp

RUN apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-connector-c-dev \
    python3-dev \
    libffi-dev \
    build-base
# libffi-dev y build-base podrian no ser necesarios, toca probar en la noche
COPY ./webApp .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "index.py"]
