FROM python:3.7-slim

WORKDIR /app

COPY / /app

RUN pip3 install -r requirements.txt --no-cache-dir
RUN python3 manage.py migrate
RUN python3 manage.py loaddata fixtures.json

CMD ["python3", "manage.py", "runserver", "0:8000"]

ENV STRIPE_PUBLISHABLE_KEY=pk_test_51M5NQkHT4zKYfj3q3PbPxzrBvaipBZh4VYea6gcgHFM6ZWSQriKNnyBKF9CO4qzt0cRr9ym6NLFo0arV8HBlu5tw00Z0yvNuzs
ENV STRIPE_SECRET_KEY=sk_test_51M5NQkHT4zKYfj3qkKl81m0H5yoRmLYbLvnrjKqo21M3wi38QJGSb5bxwP4YToNQGWinmiIVQBw6lCGdlK0EZEum00vIEvqPHY
