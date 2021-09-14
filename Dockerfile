FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

EXPOSE 8000

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
