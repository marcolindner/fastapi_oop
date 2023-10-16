FROM python:3.10

WORKDIR /code

COPY ./src/requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src .

CMD ["python", "main.py"]