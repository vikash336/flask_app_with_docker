FROM python:3.11.5

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python", "app.py"]
