FROM python:3.13-slim-bookworm

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip3 install --no-cache-dir --requirement requirements.txt

COPY ./src/ /app/

CMD ["python3", "main.py"]
