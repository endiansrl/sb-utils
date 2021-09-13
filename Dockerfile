FROM alpine:latest 

RUN apk update && apk add py3-pip

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY src /app

ENTRYPOINT ["/app/sb-exec.py"]