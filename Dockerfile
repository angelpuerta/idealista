FROM python:slim

RUN pip install poetry

WORKDIR /idealista
COPY . /idealista
VOLUME /idealista/output

RUN poetry install

CMD ["poetry", "run", "python", "idealista/main.py"]

