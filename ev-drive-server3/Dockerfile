FROM python:2-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk update && apk add gcc musl-dev python3-dev libffi-dev openssl-dev freetype-dev libpng-dev

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python"]

CMD ["-m", "swagger_server"]
