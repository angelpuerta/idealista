FROM python:slim

RUN apt-get update && apt-get install -y anacron
RUN pip install poetry
RUN echo "7     5   idealista-weekly    poetry -C /idealista run python /idealista/main.py" >> /etc/anacrontab

WORKDIR /idealista
COPY . /idealista
VOLUME /idealista/output

RUN poetry install

CMD sleep infinity

