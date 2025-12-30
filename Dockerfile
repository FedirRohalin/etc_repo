FROM alpine:latest

WORKDIR /app
COPY . . 
RUN apk update && apk uograde 
RUN apk add python3

CMD ["python3", "app_tests.py"]
