FROM alpine:latest

WORKDIR /app
COPY . .

RUN apk update && apk upgrade
RUN apk add python3

CMD ["python3", "notebook_tests.py"]