FROM python:3.7

WORKDIR /app

COPY ./python/requirements.txt ./python/requirements.txt

RUN pip install -r ./python/requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:./python"

CMD python python/app.py
