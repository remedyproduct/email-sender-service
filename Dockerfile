FROM python:3.7-alpine
WORKDIR /app

COPY ./Pipfile* ./
RUN pip install pipenv
RUN pipenv install --system --deploy
COPY ./*.py ./
COPY ./senders ./senders

CMD ["rq", "worker", "-c", "settings"]
