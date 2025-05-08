FROM python:3.12-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY my_bot /app/my_bot
ENV PYTHONPATH=/app
CMD ["python", "my_bot/main.py"]