FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY test_app.py .

# За замовчуванням запускаємо програму (але контейнер буде виходити після виконання)
# Щоб контейнер "висів" у фоні (як сервер), можна змінити команду, 
# але для консольної утиліти ENTRYPOINT правильніше.
ENTRYPOINT ["python", "app.py"]