FROM python:3.12-slim

RUN apt-get update && apt-get install -y build-essential
RUN pip install poetry

WORKDIR /idealista
COPY . /idealista
VOLUME /idealista/output

RUN poetry install

CMD ["poetry", "run", "python", "idealista/main.py"]

